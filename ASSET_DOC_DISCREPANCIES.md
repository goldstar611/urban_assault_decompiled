# Asset Doc Discrepancies

Discrepancies found while verifying `assets/docs/*.md` against the decompiled
C++ source in `/Users/af/Downloads/UA_source/src`. Built incrementally, one doc
at a time.

## ADES.md

- **Claim:** the engine loads the list iteratively at `src/base.cpp:121`.
  **Actual:** `NC_STACK_base::ReadIFFTagADES` is at `base.cpp:133`, with the
  child loop at lines 135–158. Line 121 is `SetPosition(pos);` inside a
  different reader (`ReadIFFTagSWS`-style).
- **Claim:** "`[[STRC]]` count observed: 8 in `VPfBRGR1.bas.json`".
  **Actual:** not reproducible as stated — set1's
  `assets/sets/set1/objects/vehicles/VPfBRGR1.bas.json` contains 48 `STRC`
  occurrences, 18 `OBJT`, and 1 `ADES`.
- **Confirmed:** `FORM ADES` carries no payload/CLID of its own, only child
  `OBJT`s; unknown chunks are skipped via `mfile->skipChunk()`
  (`base.cpp:155`).

## ADE.md

- **Claim:** `src/ade.cpp:75` is where `NC_STACK_ade::LoadingFromIFF` parses
  the `STRC`.
  **Actual:** `LoadingFromIFF` starts at `ade.cpp:53`; line 75 is the
  `FORM ROOT` → `NC_STACK_nucleus::LoadingFromIFF` call. The `STRC` branch is
  at `ade.cpp:80–102`.
- **Claim:** ADES iteration is at `base.cpp:121`.
  **Actual:** same as ADES.md — `ReadIFFTagADES` is at `base.cpp:133`.
- **Confirmed:** `ADE_STRC` is 10 bytes (version 2 + `_nu1` 1 + flags 1 +
  point 2 + poly 2 + `_nu2` 2); bit 1 (`ADE_FLAG_DPTHFADE` = 2) = depth-fade,
  bit 2 (`ADE_FLAG_BKCHECK` = 4) = back-face check; no `KIDS` in ADE.

## Verified clean (no discrepancies)

- AMSH.md — `amesh.cpp:87–131` matches: `ATTS` = `TAG_SIZE / 6`, fields
  `polyID/colorVal/shadeVal/tracyVal/pad`; `OLPL` = `s16` count + byte UVs
  (`byte / 256.0`), saved as `uv.tu * 256.0` (`amesh.cpp:175–176`).
  `particle.class` ATTS is indeed a different layout (`particle.cpp:454`,
  `ReadIFFAtts`). Real bytes confirmed: 10 `poly_id` entries in set1
  `VPfBRGR1.bas.json`.

## AREA.md

- **Claim:** `STRC_AREA` layout is `version`(0) / `flags`(2) / `polflags`(4) /
  `clrVal`(6) / `trcVal`(7) / `shdVal`(8).
  **Actual:** the struct at `area.cpp:91–100` has an extra `_un1` byte at
  offset 6; the real offsets are `version`(0) / `flags`(2) / `polflags`(4) /
  `_un1`(6) / `clrVal`(7) / `trcVal`(8) / `shdVal`(9) — 10 bytes total.
- **Claim:** real bytes `01 00 00 00 00 8a 00 00 80 00` are
  `color=138, tracy=0, shade=128`.
  **Actual:** big-endian decode gives `version=256`, `flags=0`,
  `polFlags=138`, `_un1=0`, `clrVal=0`, `trcVal=128`, `shdVal=0`. The `138`
  is `polFlags`, not color; `trcVal` is 128, not 0; `shdVal` is 0, not 128.
  Confirmed by set1 `VPfBRGR1.bas.json` (`"polFlags": 138`, `"trcVal": 128`,
  `"clrVal": 0`, `"shdVal": 0`, `"version": 256`).
- **Confirmed:** `area_func5__sub1` at `area.cpp:126`; `polflags` bit meanings
  match `area.h:33–66`; `FORM AREA` children (`ADE`/`STRC`/`OBJT`) match
  `area.cpp:183–206`.

- ATTS.md — Layout 1 matches `amesh.cpp:87–103` (6 bytes/poly:
  `polyID/colorVal/shadeVal/tracyVal/pad`). Layout 2 matches the particle
  save side `particle.cpp:502–519` and loader `ReadIFFAtts`
  (  `particle.cpp:363–419`): `s16 version` + 4 × vec3d (3 big-endian floats,
  `tform.h:92–107`) + `s32` fields. Clean.

## BANI.md

- **Claim:** "no `CLID` — `bmpanim.class` is implied by the engine's
  `NC_STACK_bmpanim::LoadingFromIFF` (the form type decides the class)."
  **Actual:** false. `LoadObjectFromIFF` (`nucleas.cpp:172–187`) looks the
  class up from the `CLID` chunk via `Nucleus::ClassList.find(classname)`;
  without `CLID` it never resolves a class. Shipped assets do carry
  `CLID: bmpanim.class` (e.g. set1 `VPfBRGR1.bas.json`).
- **Claim:** `anmName = buf[offset - 6]` is at `bmpAnm.cpp:79`.
  **Actual:** that assignment is at `bmpAnm.cpp:67`.
- **Claim:** STRC payload is at `src/bmpAnm.cpp:46`.
  **Actual:** line 46 is the `version` local declaration; the `STRC` read is
  at `bmpAnm.cpp:58–68`.
- **Claim:** `rsrc:rsrcpool/<name>` is opened at `bmpAnm.cpp:255`.
  **Actual:** the `uaOpenFile(std::string("rsrc:rsrcpool/") + name, "rb")`
  call is at `bmpAnm.cpp:252`.
- **Confirmed:** field order/offsets (`version`/`offset`/`animType`/name),
  real bytes, and `offset = 6` semantics match `bmpAnm.cpp:60–68`.

## BASE.md

- **Claim:** `src/base.cpp:225` onwards is where `TAG_STRC` is handled.
  **Actual:** line 225 is inside the `FORM ROOT` block; the `TAG_STRC` branch
  is at `base.cpp:239`.
- **Claim:** `fadeStart`/`fadeLength` engine defaults are filled at
  `base.cpp:234`.
  **Actual:** lines 236–237 (`_renderMsg.fadeStart = 3496.0;`
  `_renderMsg.fadeLength = 600.0;`). Line 234 is
  `_transform.MakeScaleRotationMatrix();`.
- **Claim:** the embedded `FORM/OBJT` child is loaded at `base.cpp:253`.
  **Actual:** line 253 is `if (obj_ok)` inside the `OBJT` branch; the
  `_embed = LoadObjectFromIFF(mfile)` call is at `base.cpp:266`.
- **Claim:** "Unnamed `ROOT` (empty, 4-byte chunk)".
  **Actual:** `ROOT` is a `FORM` container (12-byte IFF header, no fixed
  4-byte size); it holds a `NAME` chunk when named (`nucleas.cpp:100–110`).
- **Confirmed:** `STRC_BASE` is 62 bytes; `ReadIFFTagSTRC` at `base.cpp:77`;
  `KIDS` loop at `base.cpp:161–190`; the embed-vs-skeleton `OBJT` behavior
  (`base.cpp:250–268`) is consistent with the documented child order.

- BMHD.md — layout matches `ilbm.cpp:289–301` field-for-field; writer
  `flags = 0x80` at `ilbm.cpp:515`. Clean.

## BODY.md

- **Claim:** "One byte per pixel, palette indices" and "No compression".
  **Actual:** true for `VBMP` (`ilbm.cpp:357–363` reads `width` bytes per
  row), but `ILBM` `BODY` is bitplane data (`ilbm.cpp:187–195`) and *does*
  support RLE compression (`bmhd->compression`, `ilbm.cpp:149–186`). The doc
  lists `ILBM` as an owner, so the blanket "no compression" is wrong.

## CIBO.md

- **Claim:** `src/ilbm.cpp:91` reads the `CIBO` children.
  **Actual:** line 91 only dispatches on `TAG_EXTENSION == TAG_CIBO`; the
  `NAM2`/`OTL2` child reads are in `ilbm_func5__sub0` (`ilbm.cpp:42–61`).
  Otherwise confirmed: `NAM2` reads 256 bytes, `OTL2` reads 128 bytes with
  `count = TAG_SIZE / 2` and byte/256 UVs.

## CLID.md

- **Claim:** the table lists "Class ids that appear in set assets".
  **Actual:** `ade.class` and `bitmap.class` are listed but do not occur as
  `CLID` values anywhere under `assets/` (scan of all `class_id` values:
  `area.class`, `bmpanim.class`, `ilbm.class`, `amesh.class`, `sklt.class`,
  `base.class`, `particle.class`, `embed.class` only).
- **Claim:** "`gui`'s `RENDERABLE_CLID_CLASSES` allow-list" exists in
  `bastoolsgui3.py`.
  **Actual:** no such symbol exists anywhere in the repo (searched
  `bastoolsgui3.py` and all `*.py`); the viewer's renderability test is
  `is_renderable_unit` (`bastoolsgui3.py:124–135`), which requires
  `base.class` + a direct `ADES`.
- **Confirmed:** all ten `__ClassName` line references are exact
  (`base.h:207`, `embed.h:23`, `sklt.h:22`, `area.h:118`, `ade.h:85`,
  `amesh.h:57`, `particle.h:119`, `bmpAnm.h:107`, `bitmap.h:58`,
  `ilbm.h:60`); the 11-byte `base.class\0` example checks out.

## CMAP.md

- **Claim:** palette files are "sizes 896 = 24-byte header + 768 for
  `STANDARD.PAL` and 828 for the SET46 variant".
  **Actual:** inverted/wrong. Every `standard.pal`/`STANDARD.PAL` in the repo
  is 828 bytes and is a `FORM ILBM` (`BMHD` + `CMAP` + `CAMG`); the 896-byte
  palettes (e.g. `blau.pal`) add an `ANNO` chunk. The bytes before `CMAP` is
  40 (8-byte `FORM` + 4-byte `ILBM` + 28-byte `BMHD`), not 24. No `set46`
  palette directory exists to check the "SET46 variant".
- **Claim:** `src/ilbm.cpp:323` collects the palette.
  **Actual:** line 323 is `mfil->parse();`; the `TAG_CMAP` branch is
  `ilbm.cpp:325–344`.
- **Confirmed:** 3 bytes/entry (r,g,b) with alpha hard-set to 255
  (`ilbm.cpp:336–339`),   256 entries = 768 bytes.

## DATA.md

- **Claim:** the example is "4 polygons, 8 frames".
  **Actual:** the example lists 5 polygons (`poly 0` … `poly 4`); the
  matching `compile.py:494–498` docstring also has 5. The frame count (8) is
  correct.
- **Claim:** `0019` is the "len poly table".
  **Actual:** it is the count of 2-byte shorts (`polygons_len = 2 * 25 = 50`
  bytes, `compile.py:541–543`); the engine's `ReadTexCoords`
  (`bmpAnm.cpp:185–219`) walks exactly that many shorts via `i += ttmp`.
- **Claim:** `t=4000` is a "loop marker".
  **Actual:** no such special case in the engine — `FrameTime` is just a
  per-frame duration (`bmpAnm.cpp:577–604`); looping/ping-pong is controlled
  by `_animType` (`bmpAnm.cpp:589–597`). No `4000` constant exists in
  `bmpAnm.cpp` or the Python tooling.
- **Claim:** `LoadFromFile` is at `bmpAnm.cpp:255`.
  **Actual:** `LoadFromFile` starts at `bmpAnm.cpp:244` (line 255 is
  `fil.readU32B()` inside it). The reader range `128–240` is roughly right
  (actual `126–242`).
- **Confirmed:** class-id/names/poly/frame field order and the `s32/s16/s16`
  frame layout match `bmpAnm.cpp:126–242`; all 283 set1 `.ANM.json` files use
  `class_id = "ilbm.class"`.

## EMBD.md

- **Claim:** the engine's extra `U8(0)` pad is at `src/embed.cpp:114-116`.
  **Actual:** `mfile->writeU8(0)` is at `embed.cpp:119` (the `EMRS` push is
  at 116).
- **Claim:** the resource is resolved via `PIFFFILE` at `embed.cpp:84-92`.
  **Actual:** `RSRC_ATT_PIFFFILE, mfile` is passed at `embed.cpp:80`.
- **Confirmed:** `EMRS` split-at-first-NUL + trailing-NUL strip
  (`embed.cpp:62–75`), `TRYSHARED` init (`embed.cpp:77–80`), example byte
  count (`0x1f` = 11 + 19 + 1), and empty `ROOT` in set1 `beebox.bas.json`.

## EMRS.md

- **Claim:** the class string is `sklt.class`, `ilbm.class`, or
  `bmpanim.class` "in all shipped sets".
  **Actual:** scanning every `EMRS` in the repo's JSON assets finds only
  `sklt.class` (16 occurrences); no `ilbm.class`/`bmpanim.class` `EMRS`.
- **Claim:** name prefixes include `rsrcpool/…` and `(none)` (e.g. `FOOM`).
  **Actual:** only `Skeleton/` (14) and `skeleton/` (2) occur in the repo;
  the `rsrcpool/` and bare-name cases are not present in the JSON assets.
- **Claim:** "trim **additional** trailing `\0`s".
  **Actual:** the engine strips at most one trailing NUL per string
  (`embed.cpp:72–75`).
- **Claim:** the writer's extra `0x00` is at `embed.cpp:114-116`.
  **Actual:** `writeU8(0)` is at `embed.cpp:119`.
- **Confirmed:** case sensitivity is real — both `Skeleton/` and `skeleton/`
  appear in set1; the 31-byte example and resolution rules match
  `embed.cpp:60–89`.

- FORM.md — `FORM <size> <extension>` layout, size semantics, and odd-payload
  pad all match `IFFile.cpp:62–190`; `TAG_*` via `MKTAG` confirmed in
  `utils.h:18–68`. Clean.

- FORMATS.md — index/container graph consistent with the verified loaders;
  `visproto.lst`/`set.sdf`/`slurps.lst` exist under `assets/sets/*/scripts/`.
  Clean.

- HEAD.md — 6-byte `HEAD` layout and reader at `ilbm.cpp:313–315` confirmed;
  `vbmp.flags` is read but never used elsewhere in `src/`. Clean.

## ILBM.md

- **Claim:** `SETn/PALETTE/STANDARD.PAL` is 896 bytes (24-byte header + 768)
  and `SET46`'s is 828.
  **Actual:** same error as CMAP.md — repo `STANDARD.PAL` files are 828
  bytes (`FORM ILBM` + `BMHD` + `CMAP` + `CAMG`); the 896-byte palettes add
  an `ANNO` chunk. No `set46/palette` directory exists.
- **Claim:** `BMD_ATT_CONVCOLOR` is at `ilbm.cpp:75`.
  **Actual:** line 75 is `if ( has_nam2 )`; the flag is set at `ilbm.cpp:79`.
- **Confirmed:** `TAG_ILBM`/`TAG_VBMP` form-level check at `ilbm.cpp:262–265`
  and the shared per-chunk parser (`ilbm.cpp:272–418`).

- KIDS.md — pure `OBJT` list confirmed (`base.cpp:161–190`); slot order
  0=vehicles/1=buildings/2=ground confirmed in `compile.py:1293–1298` and
  `1314–1316`. Clean.

## MC2.md

- **Claim:** SET46 has "no per-slot `KIDS` nesting".
  **Actual:** false — `set46/objects/buildings/shell.bas.json` has two
  `KIDS` chunks: the top-level 3-slot `KIDS` plus a nested `KIDS` in slot 2
  containing 72 children.
- **Claim:** the SET46 content is a dummy `base.class` "Your Personal AMOK".
  **Actual:** no such name in the JSON; the two named slot-0/1 roots are
  `AMIGA4EVER` and the 72 slot-2 sub-objects are named `dummy`.
- **Confirmed:** `MC2` → one `OBJT` (`CLID base.class` + `BASE`); BASE child
  order `ROOT`/`OBJT embed.class`+`EMBD`/`STRC`/`KIDS`; `STRC_BASE` defaults
  (version 1, scale 1, ambient 255, att_flags 72, vis_limit 4096); top-level
  `KIDS` has exactly 3 slots; `SKLT`-only `EMBD` (3 `EMRS`); 72 `dummy`
  sub-objects; slots 0/1 each link `Skeleton/DUMMY.sklt` via `SKLC`.

## NAME.md

- **Claim:** resource `NAME` inside `SKLC` is "13 bytes:
  `Skeleton/DUMMY.sklt\0`".
  **Actual:** `Skeleton/DUMMY.sklt` is 19 chars + NUL = 20 bytes, not 13.
- **Confirmed:** all 23307 `ROOT/NAME` chunks are `zero_terminated: false`;
  all 8205 `SKLC/NAME` chunks are `zero_terminated: true`; the `NAM2`
  example and `ilbm.cpp:42`/`44` (256-byte read) check out; every `NAM2`
  name in the repo ends in `.ILBM`.

- NAM2.md — 13-byte `AIR1TXT.ILBM\0` example and `ilbm.cpp:44` confirmed.
  Clean.

## OBJT.md

- **Claim:** the `base.class` `STRC`/sub-`OBJT` switch is at `base.cpp:225`.
  **Actual:** line 225 is inside the `FORM ROOT` block; the switch
  (`if (STRC_readed) … else _embed = …`) is at `base.cpp:250–268`.
- **Confirmed:** `CLID`-driven dispatch (`nucleas.cpp:172–187`), the three
  listed shapes, and the `FORM OBJT` + `CLID` byte example all match the
  assets/`LoadingFromIFF` readers.

## OLPL.md

- **Claim:** "No global count: the chunk is a list … until the chunk size runs
  out."
  **Actual:** the engine reads exactly `polyCnt` lists, where `polyCnt` comes
  from `ATTS` (`amesh.cpp:91`, `111`); it does not use the chunk size to
  bound the list.
- **Claim:** "`TAG` order between `ATTS`/`OLPL` does not matter for the
  engine".
  **Actual:** it does — `OLPL` before `ATTS` sees `polyCnt == 0`
  (`amesh.h:60`) and skips all UV data (`amesh.cpp:111`). `ATTS` must come
  first.
- **Claim:** the byte/256 mapping is at `amesh.cpp:110`.
  **Actual:** line 110 is `if (obj_ok)`; the mapping is at `amesh.cpp:125–126`.
- **Confirmed:** `s16` count + `count` byte pairs, `tu = x/256.0`,
  `tv = y/256.0`.

- OTL2.md — no count prefix, `ilbm.cpp:119` size write, and the 128-byte
  (`dst[128]`) read bound at `ilbm.cpp:51–53` confirmed. Clean.

## POO2.md

- **Claim:** example bytes `43 e1 00 00` = `x = 490.0f` and `44 3b 80 00` =
  `z = 756.0f`.
  **Actual:** big-endian float32 decode gives `450.0` and `750.0`
  respectively.
- **Confirmed:** 12 bytes/point, `N = TAG_SIZE / 12`, `readFloatB` ×3
  (`sklt.cpp:120–128`); legacy `POOL` v1 = 6 bytes/point int16
  (`sklt.cpp:87–118`); `skeleton_read_pooX` at `sklt.cpp:78`.

## POL2.md

- **Claim:** "Triangles (3 verts) and quads (4 verts) are the only shapes in
  the shipped sets".
  **Actual:** false — scanning every `POL2.edges` polygon in the repo gives
  lengths 4 (113735), 3 (96090), 2 (2202), 6 (632), 5 (564), 0 (229), 8 (32),
  9 (12), 7 (8), 1 (7).
- **Claim:** the plane is recomputed at `sklt.cpp:214`.
  **Actual:** line 214 is in `skeleton_read_senX`; the plane math is at
  `sklt.cpp:256–285` (using `v0`,`v1`,`v2` in file order, as documented).
- **Confirmed:** `skeleton_read_pol2` at `sklt.cpp:173`; count-prefixed
  `u16` vertex counts + `u16` indices; `BEEBOX.BAS` has a `POO2`-only `SKLT`
  with no `POL2`; the 50-byte example is self-consistent (5 polys, 18 verts).

## ROOT.md

- **Claim:** the on-disk example is `52 4f 4f 54 00 00 00 00` (a `ROOT` leaf
  chunk, size 0).
  **Actual:** the engine matches `FORM`/`ROOT` (`base.cpp:219`,
  `nucleas.cpp:51`), so on disk it is `FORM <size≥4> ROOT`; a bare `ROOT`
  leaf tag would not be recognised.
- **Confirmed:** `ROOT` body is ignored except for `NAME`
  (`nucleas.cpp:100–110`); empty `ROOT` present in `EMBD`/`MC2` assets.

## SEN2.md

- **Claim:** the legacy/modern readers are at `src/sklt.cpp:78/173`.
  **Actual:** those are `skeleton_read_pooX`/`skeleton_read_pol2`; the sensor
  reader `skeleton_read_senX` is at `sklt.cpp:198` (v1 `SENS` = 6 bytes
  int16, v2 `SEN2` = 12 bytes float, `sklt.cpp:206–232`).
- **Confirmed:** 12-byte stride, `N = TAG_SIZE / 12`, 24-byte example, and
  `SEN2` presence in vehicle/weapon skeletons.

## SKLC.md

- **Claim:** `src/sklt.cpp:36` is `NC_STACK_sklt::rsrc_func64`.
  **Actual:** line 36 is inside `NC_STACK_sklt::LoadingFromIFF` (starts at
  `sklt.cpp:20`); `rsrc_func64` is at `sklt.cpp:415`.
- **Claim:** the viewer treats a `sklt.class` `OBJT` as the "renderable
  skeleton entry gate" via `RENDERABLE_CLID_CLASSES`.
  **Actual:** `RENDERABLE_CLID_CLASSES` does not exist in the repo; the
  viewer's `is_renderable_unit` (`bastoolsgui3.py:124–135`) requires
  `base.class` + a direct `ADES`, and its docstring says "Skeleton-only links
  (SKLC, no ADES) draw nothing and are skipped".
- **Confirmed:** `FORM/SKLC` with a single `NAME` child; save path pushes
  `FORM/SKLC` + `NAME` at `sklt.cpp:66–74`; reader resolves via
  `NC_STACK_skeleton::Init` with `RSRC_ATT_NAME` (`sklt.cpp:51–57`).

## SKLT.md

- **Claim:** the example is `Skeleton/S00H.sklt`, "5 points / 5 polys".
  **Actual:** every `S00H.skl.json` in the repo has 10 points and **no**
  `POL2` (POO2-only), e.g. `set1/Skeleton/S00H.skl.json`.
- **Claim:** the `POL2` example (`count = 5`, size `0x32 = 50`) belongs to
  that dump.
  **Actual:** inconsistent — it shows 6 polygon entries (counts 3,4,5,5,2,3),
  which totals 60 bytes, not 50; and `S00H` has no `POL2` at all.
- **Claim:** the parse loop is `NC_STACK_sklt::rsrc_func64` at
  `sklt.cpp:305`.
  **Actual:** line 305 is inside `sklt_func64__sub0` (`sklt.cpp:297`);
  `rsrc_func64` is at `sklt.cpp:415`.
- **Claim:** the plane recompute is `sklt_func64__sub0__sub0` at
  `sklt.cpp:214`.
  **Actual:** the function is at `sklt.cpp:247` (math `256–285`), called
  from `sklt.cpp:408–409`.
- **Confirmed:** tag dispatch `POOL/POO2/POLY/POL2/SENS/SEN2`
  (`sklt.cpp:321–396`); missing/empty `POL2` is legal — `set46/beebox.bas.json`
  has `POO2` only.

## STRC.md

- **Claim:** ADE real bytes `00 01 00 04 00 00 00 0a 00 00` are
  "flags 0, point 4, poly 10".
  **Actual:** decode is `version=1, _nu1=0, flags=4, point=0, poly=10,
  _nu2=0` (matches set1 `VPfBRGR1.bas.json` `"flags": 4, "point": 0`).
- **Claim:** AREA real bytes are "clrVal 0, trcVal 0, shdVal 128".
  **Actual:** `clrVal=0, trcVal=128, shdVal=0` — trcVal/shdVal swapped
  (same error as AREA.md).
- **Claim:** the `STRC_BASE` hex dump is a 62-byte chunk.
  **Actual:** the dump is 57 bytes (12+12+12+12+9) and the trailing
  `10 00 00 00 00 ff` neither matches big-endian `vis_limit=4096`
  (`00 00 10 00`) + `ambient_light=255` (`00 00 00 ff`) nor is 8 bytes.
- **Claim:** ADE layout is at `src/ade.cpp:75`.
  **Actual:** line 75 is the `FORM ROOT` call; the `STRC` branch is
  `ade.cpp:80–102`.
- **Claim:** BANI layout is at `src/bmpAnm.cpp:46`.
  **Actual:** line 46 is the `version` local; the `STRC` read is
  `bmpAnm.cpp:58–68`.
- **Claim:** `fadeStart`/`fadeLength` defaults are at `base.cpp:234`.
  **Actual:** `base.cpp:236–237`.
- **Claim:** the toolchain inference ends with "otherwise `STRC_UNKNOWN`
  (kept verbatim)".
  **Actual:** `Strc.set_binary_data` raises `ValueError` for unrecognised
  data (`compile.py:1416`, `1421`); `STRC_UNKNOWN` is not a fallback there.
- **Confirmed:** all four layouts/offsets, `FLAG_FOLLOWPARENT = 0x40`
  (`base.h:151`), the `version >= 1` gating, and the BANI real bytes.

## VANM.md

- **Claim:** the concrete `FX2.ILBM` example has "4 frames".
  **Actual:** the example's frame count is `00 08` = 8 (same error as
  DATA.md).
- **Claim:** `00 19` is the "total polygon table length (u16, bytes)".
  **Actual:** it is the count of 2-byte shorts (25 shorts = 50 bytes), per
  `compile.py:541–543` and `bmpAnm.cpp:185–219`.
- **Claim:** the byte/256 division is at `bmpAnm.cpp:200`.
  **Actual:** line 200 reads the per-poly vertex count; the division is at
  `bmpAnm.cpp:212–213`.
- **Claim:** `LoadFromFile` is at `bmpAnm.cpp:240`.
  **Actual:** `bmpAnm.cpp:244` (line 240 is `return true;` in another
  function).
- **Claim:** "`bmpanim.class` and `ilbm.class` are the only known values of
  the `class_id`".
  **Actual:** all 283 set1 `.ANM.json` files use `ilbm.class`; no
  `bmpanim.class` class-id is present in the repo.
- **Confirmed:** raw `.ANM` = `DATA` payload; `s32/s16/s16` frames;
  `rsrc:rsrcpool/<name>`; `BANM_ATT_ANIMTYPE` from the BANI `STRC`.
