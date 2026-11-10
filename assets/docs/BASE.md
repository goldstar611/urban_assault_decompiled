# BASE / ROOT / KIDS: the object tree

*`base.class` payload: transform, light, and children.*

## Related format documents

- `[[OBJT]]` — owner form.
- `[[STRC]]` — transform chunk; the `STRC_BASE` 62-byte flavor lives here.
- `[[KIDS]]` — children container.
- `[[MC2]]` — the set-level application of the same schema.
- `[[EMBD]]` — a base node's resource store (sibling `OBJT` with
  `embed.class`).
- `[[NAME]]` — node name (`ROOT/NAME`).

## Layout

`BASE` children, in order:

```
FORM ... BASE
    ROOT                       # empty, or NAME naming the node
    OBJT [CLID embed.class, EMBD ...]   # optional resource store
    STRC <62 bytes>            # [[STRC]] STRC_BASE flavor
    KIDS                       # sub-objects / the three slots
```

Unnamed `ROOT` (empty, 4-byte chunk) is normal for skeleton-bearing roots;
named `ROOT` carries a `NAME` chunk.

## Engine reading

`src/base.cpp:225` onwards: a `TAG_STRC` chunk calls
`NC_STACK_base::ReadIFFTagSTRC` (`base.cpp:77`) which reads the 62 bytes
described in `[[STRC]]` and applies position/scale/euler plus
`followParent`-flag, `visLimit` and `ambientLight` — note `fadeStart`/
`fadeLength` are NOT in the chunk; the engine fills them as defaults
(`base.cpp:234`). A subsequent `FORM/OBJT` child is loaded recursively
as its embedded store (`base.cpp:253`).

## KIDS slots

Sub-objects live in `KIDS`. For the set-root, the three slots are a
vehicles slot, a buildings slot, and a ground slot — see `[[MC2]]`. LEAF
slots' number is fixed by that root only; object sub-trees beyond the set
root can nest freely.

## HEAD-like caveats

- A `base.class` tree without `STRC` renders with engine defaults only —
  behavior guarded upstream (`STRC` presence is required for meaningful
  transforms).
- `KIDS` container count in the *set root* is 3, honored in
  `compile.Mc2.init_mc2`.
