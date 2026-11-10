# SEN2: skeleton sensor points

*Optional `[[SKLT]]` child: per-point `float32 x/y/z` with the same
12-byte stride as `[[POO2]]`. Used for weapons/sensor anchor positions in
vehicle skeletons.*

## Related format documents

- `[[SKLT]]` — owner skeleton.
- `[[POO2]]` — the shape it mirrors.

## Layout

```
    53 45 4e 32 00 00 00 18                  SEN2....
    ...12 bytes per point...
```

- No count; `N = chunk_size / 12`.
- Absence is normal — most building skeletons have no `SEN2`.

### Legacy variant

`SENS` v1 stored `s16 x/y/z` (6 bytes/point). The engine still reads both
(`src/sklt.cpp:78/173` style readers — `skeleton_read_senX`); modern
assets are all `SEN2`.
