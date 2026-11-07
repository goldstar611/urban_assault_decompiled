# Roadmap

## Form validation

## Remove conversion shims

## Test coverage

## Byte-exact SET.BAS builds

Done for sets 1-6: `decompile_set_bas.py` extracts the original EMBD resources and
writes the per-set manifest `assets/sets/setN/resource_order.json`
(exact original EMRS names/order, plus the sha256 of the source SET.BAS as
provenance); `compile.build_set()` replays it and
`Vbmp.load_image()` loads palette BMPs losslessly. `build_set(n)` output is
byte-identical with the game's originals `DATA/SETn/OBJECTS/SET.BAS` for
n=1..6 (golden sha256 table in test/test_compile.py). Remaining: run
`decompile_set_bas.py` for SET46 (needs its object assets first) and the
dataxp remaster variants (different bytes).

