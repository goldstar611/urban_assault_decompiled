# POL2: skeleton polygons

*Per-polygon vertex-index list for a `[[SKLT]]`: a u32 count followed by
`u16 vertex-count` + `u16 vertex ids` per polygon.*

## Related format documents

- `[[SKLT]]` — the skeleton this belongs to.
- `[[POO2]]` — the points these indices refer to.
- `[[AREA]]`/`[[ADE]]` — `STRC_ADE`'s `point`/`poly` fields index into this
  list.
- `[[AMSH]]` — `ATTS.poly_id` also refers to skeleton polys.

## Layout

```
    50 4f 4c 32 00 00 00 32                  POL2...2    # size 0x32 = 50
    00 00 00 05                              ....        # 5 polygons
    # poly 0: triangle (vertices 0, 4, 8)
    00 03 00 00 00 04 00 08                  ...
    # poly 1: quad (1, 0, 4, 5)
    00 04 00 01 00 00 00 04 00 05
    ...
```

- Count = `u32` big-endian.
- Per polygon: `u16 num_vertices`, then `num_vertices × u16` indices into
  `[[POO2]]`.
- Triangles (3 verts) and quads (4 verts) are the only shapes in the
  shipped sets; more are technically representable.

## Engine reading

`src/sklt.cpp:173` `skeleton_read_pol2` — count first, then per-poly
2-byte vertex-count + sum indices. Every polygon's plane is recomputed
from vertices `v0–v2` *in file order* (`sklt.cpp:214`); the winding
decides which side faces the camera, so reordering vertices inside a poly
changes rendering.

## Caveats for tools

- Index 0 is a real vertex — never sentinel. Skeletons whose `POL2` is
  empty (see `BEEBOX.BAS`) are the "points-only" case.
- Our viewer draws the poly-0 case through the
  `getattr(strc, "poly", None) is not None` check, not a truthiness test —
  a historical bug worth knowing about.
