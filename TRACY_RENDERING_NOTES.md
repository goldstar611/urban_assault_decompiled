# Tracy (FLATTRACY/LUMTRACY) rendering — research log and state

Branch: `tracy-rendering` (work-in-progress commit `e76c170` on top of
`24fff71`). Not merged into master; user reports the visual result still
does not match the in-game look.

## Goal
Render `VPfJET1`'s afterburner/exhaust animations the way Urban Assault's
engine does: a soft, translucent heat glow (white-hot core + yellow), not
hard opaque white pixels.

## Ground truth from the decompiled engine (/Users/af/Downloads/UA_source/src)

All of the following was verified against source and real SET.BAS data:

1. **PolFlags live in the AREA's STRC chunk.** An AREA form is
   `ADE ` + `STRC` + `OBJT`; the engine reads the flat 10-byte header
   (version, flags, polFlags, pad, clrVal, trcVal, shdVal) in
   `area_func5__sub0` (area.cpp:89-122), dispatched from the STRC chunk
   (area.cpp:190-192). In our parse this is the `STRC_AREA`-flavored Strc
   instance (`compile.Strc.polFlags`); the `STRC_ADE` flavor carries the
   poly index; `STRC_BANI` carries the animation name. Watch out: all
   three have `polFlags` and `poly` attributes — only `STRC_AREA`'s
   polFlags and `STRC_ADE`'s poly are meaningful.

2. **polFlags bit meanings** (area.h:33-66):
   - SCANLN 0x1; MAPBIT1 0x2, MAPBIT2 0x4 (NONMAPPED / LINEARMAPPED 0x2 /
     DEPTHMAPPED 0x6); TEXBIT 0x8; SHADEBIT1 0x10, SHADEBIT2 0x20
     (NOSHADE / FLATSHADE / LINESHADE / GRADIENTSHADE 0x30);
     TRACYBIT1 0x40, TRACYBIT2 0x80 (NOTRACY / CLEARTRACY 0x40 /
     FLATTRACY 0x80 / TRACYMAPPED 0xC0); TRACYBIT3 0x100 (DARK/LIGHT).

3. **Render mode mapping** (area.cpp:263-294): the (mapped, shade, tracy)
   triple selects GFX render flags. `LINEARMAPPED|NOSHADE|FLATTRACY` →
   `RFLAGS_LUMTRACY`; CLEARTRACY → `RFLAGS_ZEROTRACY`; NOTRACY → plain /
   shaded. Example verified from data: VPfJET1 has 21 areas, **17 are
   LUMTRACY** (all exhaust anims 2002970A/B/C.ANM, HOTSHOT1/2.ANM), 4 are
   NOTRACY|GRADIENTSHADE. VPfFLUG1: 2 LUMTRACY, 8 ZEROTRACY, 1 NOTRACY.
   VPdFLUG1: 18 LUMTRACY, 2 ZEROTRACY.

4. **LUMTRACY blending** (system/gfx.cpp:1038-1068, area.cpp:299-302,355):
   whole polygon gets a global vertex alpha `GFX::Engine.GetAlpha()` =
   `gfx.alpha` ini, **default 192/255 ≈ 0.75** (inivals.cpp:12).
   - destblend HW (`gfx.blending=1`): `SrcBlend=GL_ONE, DstBlend=GL_ONE`
     — pure additive.
   - srcblend HW (default `gfx.blending=0`, inivals.cpp:23):
     `SrcBlend=GL_SRC_ALPHA, DstBlend=GL_ONE_MINUS_SRC_ALPHA` — plain
     alpha blend at 0.75.
   - stippling fallback (`gfx.blending=2`).
   - Zwrite disabled for tracy when `!_zbuf_when_tracy` (gfx.cpp:1040-1041).

5. **Per-pixel transparency is exact-yellow only.** The engine's
   `ConvAlphaPalette` (system/gfx.cpp:2202-2208) keys ONLY palette RGB
   (255,255,0) → alpha 0 (and rgb zeroed). Every other pixel keeps
   alpha 255. The luminance-as-alpha conversion (rgb normalized to max
   channel, alpha = max component, gfx.cpp:2211-2229) applies ONLY to the
   `fx1/fx2/fx3.ilbm` glow resources (ilbm.cpp:423-457 picks the
   hi/alpha|beta|gamma variant by HW capability). VANM/ANM frames load
   with `transp=0` (transp = reassignName != 0, ilbm.cpp:496 — only fx*
   names get reassigned).

6. **Texture filtering** (gfx.cpp:930-946, gfx.h:339, gfx.cpp:1011,1080):
   `LinearFilter` comes from the `gfx.filter` ini which **defaults to
   false** (ini.cpp:15-32, KT_BOOL default false) → NEAREST for
   everything; ZEROTRACY forces NEAREST explicitly (gfx.cpp:1080).
   LUMTRACY does not force linear. Our viewer already uses NEAREST —
   matches stock engine config.

7. **TexBlend MODULATEALPHA** = 1 in the enum (gfx.cpp:1046 etc.);
   with fixed-function GL this corresponds to GL_MODULATE so vertex
   color (including alpha) scales the texture.

## What was implemented (branch tracy-rendering, bastoolsgui3.py)

- `Animation.map_yellow_to_alpha` rewritten: exact-yellow keying only
  (`rgb == 0x00FFFF00` in LE ARGB32 → alpha 0), falloff removed
  (previous `YELLOW_KEY_RADIUS_SQ = 90*90` near-yellow ramp deleted).
  Unit-verified: synthetic image 63/63 yellow px keyed, white kept;
  real exhaust frame 2002970C.ANM frame 0: 36336 yellow px keyed
  (== 36336 yellow rgb px), 33 white px opaque.
- `MyQTreeWidgetItem.POLFLAG_FLATTRACY = 0x80`,
  `LUMTRACY_ALPHA = 192/255.0`.
- `animated_areas()` now returns `(anim_name, poly_index, luminance)`;
  `_bani_reference_for_area` reads luminance from the `STRC_AREA` flavor
  and poly from the first STRC that defines it (`STRC_ADE`).
- `_area_alpha()` for direct AREA/FARE selection.
- Per-poly alpha plumbed through `selection_changed` into
  `GLWidget.play_animations` groups as `(poly_index, animation, alpha)`;
  `animation_tick` and `draw_animation` updated; status message unpack
  fixed accordingly.
- `_bind_frame_texture`: `GL_REPLACE` → `GL_MODULATE` so
  `glColor4f(1,1,1,alpha)` scales the fragment.
- `_draw_textured_polygon(..., alpha=1.0)`: for alpha<1 (FLATTRACY)
  uses `glBlendFunc(GL_SRC_ALPHA, GL_ONE)` — classic additive glow,
  emulating the engine's destblend path; else plain
  `(SRC_ALPHA, ONE_MINUS_SRC_ALPHA)`.
- Verified headless: VPfJET1 unit selection → 17/20 animated polys with
  alpha 0.75; test_compile.py OK (56 tests).

## Previous attempts / history (master commits)

- Near-yellow falloff keying (commits `5f35bf5`, `402c6f3`, `a9cb7e2`)
  fixed the "OBJT 55 propeller renders black" bug — yellow-dominant VANM
  frames (e.g. 36336/65536 px keyed) needed partial keying *as judged
  then*; superseded by exact keying + tracy alpha approach.
- Renderable unit gate rework (`2749967`): unit = OBJT with
  CLID=base.class with direct ADES in its BASE; containers with >1 unit
  render nothing (status hint instead) — fixed the "MC2 /OBJT loads
  30k frames" slowness.
- Docs for all of the above committed as `24fff71` (AREA/STRC/ADE/BODY).

## Why it still looks wrong (open problem)

User: "still see white pixels instead of blurred translucent pixels."
Hypotheses, in order of likelihood:

1. **Qt GL limitation suspicion (user's own).** Possibly
   `glColor4f`+`GL_MODULATE`+`glBlendFunc` in the immediate-mode
   (compatibility profile) path used by `GLWidget` does not actually
   blend the way we expect on this driver/Qt build, or the widget's
   surface format lacks something needed. Not yet diagnosed:
   - Try a minimal offscreen QOpenGLWidget test that draws an
     ARGB32-textured quad with MODULATE + alpha blend over a known
     background and reads pixels back (glReadPixels) to prove whether
     alpha blending/color modulation works at all.
   - Check the QSurfaceFormat requested for the widget (alpha bits,
     profile). `QOpenGLWidget` composites via FBO — blending of the
     final FBO onto the window uses premultiplied-alpha semantics; a
     mismatch can make translucent textures look wrong.
   - Alternative implementation routes: use QOpenGLShaderProgram with
     a simple shader (uniform alpha), or pre-multiply the frame alpha
     into the image per frame (CPU cost per frame change only).
2. **Reference mismatch.** The stock engine default (srcblend, 0.75
   alpha) may simply not be the look the user remembers from gameplay —
   in-game the exhaust sits over bright terrain/sky; over our dark
   viewer background a 75% white still reads "white". The additive
   (destblend) variant was applied as the closer-looking option, but
   user still unhappy — consider a visible toggle (alpha vs additive)
   and/or rendering over a representative bright background.
3. **Depth/interference.** Wireframe lines and opaque polys drawn in the
   same pass may z-fight or occlude the glow; engine disables Zwrite for
   tracy (`gfx.cpp:1040`). We do not disable depth writes for the glow
   polys — worth trying `glDepthMask(GL_FALSE)` for alpha<1 polys.
4. Frame textures are 256x256 with big polygon UV spans; Nearest
   filtering is stock-engine-correct, but the user might prefer the
   `gfx.filter=1` linear look for the glow only.

## Next steps if work resumes

1. Prove/disprove the Qt GL blending path with a glReadPixels probe.
2. Add `glDepthMask(GL_FALSE)` for tracy polys (engine parity).
3. Try premultiplied-alpha frame upload or a shader with uniform alpha.
4. Offer a GUI toggle: tracy blend = additive / alpha, and optionally
   linear filtering for tracy polys only.
