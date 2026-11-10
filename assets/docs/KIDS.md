# KIDS: children container

*Pure list container — no payload of its own, just nested `OBJT` forms.*

## Related format documents

- `[[BASE]]` — main consumer.
- `[[MC2]]` — the set-root slot ordering matters here.
- `[[OBJT]]` — children forms.

## Layout

```
    4b 49 44 53 .. .. .. ..                   KIDS....  (whole payload is
    FORM OBJT ...                             # children, nothing else
    FORM OBJT ...
    ...
```

Anything non-`FORM/OBJT` between children is skipped by the engine, but is
preserved by our parser in the assets JSON rebuild order so that
byte-exact rebuilds stay possible.

## Order-warning for writers

The `KIDS` children order determines visible layering (first child drawn
first), and the set-root slots *must* remain vehicles/buildings/ground —
the golden set-build tests (`test/test_compile.py`) enforce the same order
as the original scripts (`set.sdf`, `visproto.lst`, `slurps.lst`).
