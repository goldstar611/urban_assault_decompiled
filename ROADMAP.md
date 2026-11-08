# Roadmap

## Form validation

## Remove conversion shims

## Test coverage

## Byte-exact SET.BAS builds

Done for sets 1-6 *and* the expansion-pack variants 1_xp-6_xp:
`decompile_set_bas.py` extracts the original EMBD resources from a given
`SET.BAS` path and writes the per-set manifest `resource_order.json`
(exact original EMRS names/order, plus the sha256 and portable source path
of the SET.BAS as provenance); `compile.build_set()` replays it and
`Vbmp.load_image()` loads palette BMPs losslessly. `build_set(n)` /
`build_set("n_xp")` output is byte-identical with the originals
`DATA/SETn/OBJECTS/SET.BAS` and `dataxp/Setn/Objects/SET.BAS`
(golden sha256 table in test/test_compile.py). Remaining: SET46 + its
dataxp variant (needs object assets first).

