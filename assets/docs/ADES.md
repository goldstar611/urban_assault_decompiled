# ADES: list of detail parts

*Wrapper that groups the `[[ADE]]`/`[[AREA]]` nodes of one model. No
payload of its own — only child `OBJT`s.*

## Related format documents

- `[[ADE]]`, `[[AREA]]` — parts.
- `[[OBJT]]`, `[[CLID]]` — children.
- `[[BASE]]` — where an `ADES` appears in a vehicle tree (typically one
  `ADES` per mesh cluster).

## Layout

```
FORM ... ADES
    OBJT [CLID ade.class,  ADE  [ROOT/NAME, STRC]]   # untextured part
    OBJT [CLID area.class, AREA [ADE, STRC, OBJT]]   # textured part
    ...                                                (~8 in the sets)
```

`[[STRC]]` count observed: 8 in `VPfBRGR1.bas.json` — engine loads the
list iteratively (`src/base.cpp:121`) and does not cap it.

## Serialization notes for writers

- Child order is render/attachment order; don't sort.
- `ADES` chunks have no `CLID` — they are *containers*, not classes.
- The engine tolerates unknown children (`mfile->skipChunk()`), but our
  byte-exact rebuilds depend on the original order — see
  `test/test_compile.py` set-1..set-46 golden builds.
