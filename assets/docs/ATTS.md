# ATTS: per-polygon attributes

*Two different layouts share the `ATTS` chunk id depending on owner
class — a real trap.*

## Related format documents

- `[[AMSH]]` — owner of the common (mesh) layout.
- `[[AREA]]`, `[[POL2]]` — `poly_id` here indexes skeleton polygons.
- `[[OLPL]]` — pairs with the mesh layout as its uv table.

## Layout 1: `amesh.class` (the common one) — `src/amesh.cpp:87`

Six bytes per polygon, `count = chunk_size / 6`:

```
    00 00 00 0b 80 00    poly_id 0,   color 11, shade 128, tracy 0
    00 01 00 00 80 00    poly_id 1,   color  0,  shade 128, tracy 0
    00 02 00 00 80 00    poly_id 2,   ...
```

```
 0  int16  poly_id     # index into the parent skeleton's [[POL2]]
 2  byte   color_val
 3  byte   shade_val
 4  byte   tracy_val
 5  byte   pad
```

## Layout 2: `particle.class` — `src/particle.cpp:502`

Same chunk id, but a *different* binary scheme:

```
 0  int16  version (=1)
 2  float  accel_start (vec3f)
 ... float accel_end, float magnify_start, ... magnify_end
```

Our parser keeps `is_particle_atts` flag and reuses entry parsing only
when the owner is `amesh.class`; see `compile.Atts`.

## Caveats for writers

- Never re-emit particle ATTS through the amesh writer path.
- Per the engine loaders, an `ATTS` inside `[[AMSH]]` where
  `poly_id == num_polys` is valid — the value is an index, not a count.
