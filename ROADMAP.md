# Roadmap

## Byte-exact SET.BAS builds

Done for sets 1-6 *and* the expansion-pack variants 1_xp-6_xp:
`decompile_set_bas.py` extracts the original EMBD resources from a given
`SET.BAS` path and writes the per-set manifest `resource_order.json`
(exact original EMRS names/order, plus the sha256 and portable source path
of the SET.BAS as provenance); `compile.build_set()` replays it and
`Vbmp.load_image()` loads palette BMPs losslessly. `build_set(n)` /
`build_set("n_xp")` output is byte-identical with the originals
`DATA/SETn/OBJECTS/SET.BAS` and `dataxp/Setn/Objects/SET.BAS`
(golden sha256 table in test/test_compile.py).

Remaining:

- dataxp Set46 variant (`dataxp/Set46/Objects/SET.BAS` — decompile its
  tree assets; the non-xp set46 build is already golden-tested).

## Other game assets

Planned for decompilation into the repo (SKLT/ILBM pipelines exist):
1. ~~`DATA/WIRELESS` — 121 `.SKL` gauge/radar skeletons → `.skl.json`~~
   done: `assets/wireless/` (121 skeletons, byte-exact via
   `assets/wireless/manifest.json` sha256 table, tested in
   test/test_compile.py)
2. `dataxp/Mc2Res/SKELETON` — xp mc2res skeletons → `.skl.json`
3. `MC2RES/REMAP` (`SHADERMP.ILB`, `TRACYRMP.ILB`) — shader/tracy remap
   luts → lossless indexed bitmaps + a `REMAP.md` in `assets/docs/`
4. UI bitmap pages — `MC2RES/POINTERS` (12 `.ILB`), `Disk320/512/640.ilb`
   (menu backdrops at three resolutions), and the set-level pages
   (`LEGO*.ILB`, `FONTPAGE.ILB`, `ICONPAGE.ILB`, `MB.ILB`,
   `MAPCUR64.ILB`, `UNUSED.ILB`) — lossless indexed bitmaps; no extra
   format semantics beyond ILBM/VBMP, so archival value only

Out of scope (documented, not planned for decompilation):
5. `DATA/SOUNDS` + `MOV/*.mpg` — binary media, store sha256 only
6. text/config copies (`world.ini`, `SETTINGS/LANGUAGE`, `LEVELS`,
   `dataxp/Scripts`) — copyable without parsing, no decompile value
7. `FONTS`/`HFONTS` font pages — font-page ILB bitmaps, parser exists but
   no consumer in the toolchain today
