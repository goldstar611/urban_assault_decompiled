# MC2: set container (SET.BAS)

*Top-level form of each `DATA/SETn/OBJECTS/SET.BAS`. One `MC2` form per set,
containing the set's whole object tree.*

## Related format documents

- `[[FORM]]` — container framing this form.
- `[[OBJT]]` — the single child form.
- `[[BASE]]`, `[[STRC]]`, `[[KIDS]]` — the object-tree spine.
- `[[EMBD]]` — where VBMP/SKLT/VANM resources live.

## Layout

`MC2` always wraps exactly one `OBJT` form that is
`CLID=`[[base.class|CLID]] plus a `[[BASE]]`:

```
FORM ... MC2 FORM ... 04 OR
FORM 00004014 MC2                     # form size 0x4014 (16 KB, set46 size)
    FORM 00004008 OBJT                # one object node
        CLID 0000000B ...             # [[CLID]] class_id = "base.class"
        FORM 00003FE8 BASE ...        # [[BASE]] spine
```

The `BASE`'s children, in order, are:

1. `ROOT` — empty; the set tree has no name.
2. `OBJT` with `CLID = embed.class` and the storehouse `[[EMBD]]`.
3. `STRC` — a `STRC_BASE`-flavor [[STRC]] chunk (version 1, scale 1
   and `ambient_light=255`,`att_flags=72`,`vis_limit=4096`).
4. `KIDS` — exactly three children (see `[[BASE]]` for the slots).
   Slot count is fixed; missing vehicles/buildings/ground appear as
   empty sub-`[[KIDS]]` containers.

## The three KIDS slots and the script sources

| slot | children per | source file |
| --- | --- | --- |
| 0 | vehicles | `visproto.lst` → one vehicle per line |
| 1 | buildings | `set.sdf` → first entry per line = .bas name |
| 2 | ground | `slurps.lst` → one ground object per line |

Order inside each slot's children must match the script file order —
sorting breaks byte-exactness (see `test/test_compile.py`).

## Engine reading

`src/base.cpp` `NC_STACK_base::LoadingFromIFF` reads the `OBJT` and its
children; see `[[BASE]]` and `[[OBJT]]` for the recursion.

## Special case: SET46 (shell set)

`SET46` is generated as the game's UI shell, and its whole content
(a dummy `base.class` "Your Personal AMOK" with 72 skinned sub-objects)
lives *inside the single top-level `OBJT`*, with no per-slot `KIDS`
nesting; resources are `[[SKLT]]`-only and the vehicle slot links
`Skeleton/DUMMY.sklt` directly as leaf-children. Our rebuild path
short-circuits this shape (`compile.build_set`, `shell.bas.json`).
