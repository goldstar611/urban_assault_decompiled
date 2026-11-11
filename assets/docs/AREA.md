# AREA: textured plane (part of a mesh)

*`area.class` node: a `[[ADE]]` with surface settings plus its texture
source. This is the format that gives a `[[SKLT]]` polygon UVs and a
bitmap.*

## Related format documents

- `[[ADE]]` — superclass.
- `[[STRC]]` — the second 10-byte flavor (`version 256` when read as ADE).

  **Where the surface settings live**: the AREA's 10-byte header
  (version/flags/polFlags/clrVal/trcVal/shdVal) is the payload of the
  AREA's own `STRC` chunk, *not* of the `ADE` subform. The engine reads it
  in `area_func5__sub0` (`src/area.cpp:89-122`), dispatched from the
  `STRC` chunk branch of `NC_STACK_area::LoadingFromIFF`
  (`src/area.cpp:190-192`). The `ADE` subform only carries its own
  `STRC_ADE` bytes (point/poly index) — see `[[ADE]]`.
- `[[CIBO]]` — texture-plane bitmap reference (`NAM2`/`[[OTL2]]`).
- `[[SKLC]]` — skeleton link.
- `[[AMSH]]` — the other texture-plane source (animated mesh).
- `[[POO2]]`/`[[POL2]]` — geometry behind `point`/`poly`.

## Layout

```
FORM ... AREA
    ADE [ROOT/NAME, STRC <STRC_ADE bytes>]   # geometry anchor
    STRC <10 bytes STRC_AREA>                # surface settings
    OBJT ...                                 # bits: [[CIBO]]/[[SKLC]] bitmap refs
```

### STRC_AREA payload — `src/area.cpp:89-122`

```
 0  int16  version (=256, i.e. 0x0100 on disk; engine only tests >= 1)
 2  uint16 flags       (bit 1 dpthfade, bit 2 backcheck — same bits as ADE)
 4  uint16 polFlags (bit meaning — src/area.h:33-66:)
        0x0001   SCANLN  scanline orientation: 0 = vertical, 1 = horizontal
        0x0002+0x0004 mapping (MAPBIT1|MAPBIT2):
                 00 = NONMAPPED, 01 = LINEARMAPPED (0x2), 11 = DEPTHMAPPED (0x6)
        0x0008   TEXBIT  textured when set
        0x0010+0x0020 shading (SHADEBIT1|SHADEBIT2):
                 00 = NOSHADE, 01 = FLATSHADE (0x10), 10 = LINESHADE (0x20),
                 11 = GRADIENTSHADE (0x30)
        0x0040+0x0080 tracy (TRACYBIT1|TRACYBIT2):
                 00 = NOTRACY, 01 = CLEARTRACY (0x40), 10 = FLATTRACY (0x80),
                 11 = TRACYMAPPED (0xC0)
        0x0100   TRACYBIT3: 0 = DARK, 1 = LIGHT (0x100)
 6  byte   clrVal   # palette-ish color when not mapped
 7  byte   trcVal   # transparency value
 8  byte   shdVal   # shade amount (shade factor = 1 - shdVal/256)
```

Real bytes (a typical exhaust/glow plane from `VPfJET1`, set 1):

```
    01 00 00 00 00 8a 00 00 80 00    version 256, flags 0,
                                     polFlags 0x008a = 138
                                     (LINEARMAPPED|TEXBIT|FLATTRACY),
                                     clrVal 0, trcVal 0, shdVal 128
```

(`compile.py` exposes these as the parsed fields `Strc.polFlags`,
`Strc.clrVal`, `Strc.trcVal`, `Strc.shdVal`.)

## Tracy render modes — how the engine actually blends

`NC_STACK_area::GenMesh` (`src/area.cpp:263-294`) masks off SCANLN, TEXBIT
and TRACYBIT3 and matches the remaining (mapped, shade, tracy) triple
against a table of GFX render modes:

| tracy mode | render mode | engine blend (`src/system/gfx.cpp:1038-1068`) |
| --- | --- | --- |
| `NOTRACY` | plain `RFLAGS_TEXTURED` (+`RFLAGS_SHADED` if gradient) | opaque, alpha-tested |
| `CLEARTRACY` | `+ RFLAGS_ZEROTRACY` | alpha-test keyed pixels |
| `FLATTRACY` | `+ RFLAGS_LUMTRACY` | whole-polygon translucency (LUMTRACY) |

LUMTRACY (the FLATTRACY triple `LINEARMAPPED|NOSHADE|FLATTRACY`, plus the
gradient-shade variant):

- every vertex of the polygon gets the **same global alpha** =
  `gfx.alpha` (default **192/255 ≈ 0.75**, `src/system/inivals.cpp:12`,
  read via `src/area.cpp:299-302`).
- blending is `GL_ONE`/`GL_ONE` additive when the hardware supports
  destblend, otherwise `GL_SRC_ALPHA`/`GL_ONE_MINUS_SRC_ALPHA`
  (`src/system/gfx.cpp:1038-1068`), with a stippling fallback.
- `gfx.zbuf_when_tracy` off ⇒ z-write disabled for these polys.

**Per-pixel transparency is keyed, not computed**: the only keyed color in
the engine is exact palette RGB (255,255,0) yellow → alpha 0
(`ConvAlphaPalette`, `src/system/gfx.cpp:2202-2208`). White and every
other color keep alpha 255; their translucency comes solely from the
LUMTRACY polygon alpha above. The luminance-as-alpha palette conversion
(`gfx.cpp:2211-2229`) applies **only** to the `fx1`/`fx2`/`fx3.ilbm` glow
resources (`src/ilbm.cpp:423-457`), not to AREA textures.

Real-world sanity check: vehicle `VPfJET1` (SET.BAS set 1) has 21 areas;
17 are LUMTRACY (all exhaust/afterburner anims `2002970A/B/C.ANM`,
`HOTSHOT1/2.ANM`), 4 are `NOTRACY|GRADIENTSHADE`.

### OBJT children

`area_func5__sub1` (`area.cpp:126`) loads exactly one `bitmap.class`
object per `OBJT` (`[[CIBO]]` or inline) and routes it:

- `polFlags & 0x8` (TEXBIT, non-tracy) → texture image,
- `polFlags == 0xC0` (TRACYMAPPED only) → transparency image,

because the texture bitmap used by this `AREA` is loaded through
`LoadObjectFromIFF` from the following form.

## Viewer notes

The uv source for `AREA` static textures is `amsh.olpl_points` semantics —
see `[[OLPL]]` for the byte-for-byte mapping. For `[[AMSH]]`-driven
animation, each frame's `vbmp_coords` defines its own uvs (`[[VANM]]`).
