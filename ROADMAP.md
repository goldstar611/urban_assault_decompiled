# Roadmap

## Form validation

## Remove conversion shims

## Test coverage

## Byte-exact SET.BAS builds

Done for set1: `decompile_set_bas.py` extracts the original EMBD resources and
writes the per-set manifest `assets/sets/setN/resource_order.json`
(exact original EMRS names/order); `compile.build_set()` replays it and
`Vbmp.load_image()` loads palette BMPs losslessly. `build_set("1")` output is
byte-identical with the game's original `DATA/SET1/OBJECTS/SET.BAS`
(sha256 cf1b7051108542d8892cde8c689141249c90069d9a00c97af230d2c5315ea5b5,
golden test updated). Remaining: run `decompile_set_bas.py` for the other
sets (fixtures only cover SET1/SET46 so far).

