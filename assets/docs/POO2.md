# POO2: skeleton points

*Per-point 3-vector payload of a `[[SKLT]]`, big-endian float32 xyz, 12
bytes per point.*

## Related format documents

- `[[SKLT]]` — the skeleton this belongs to.
- `[[POL2]]` — polygons referring to these points by 0-based index.
- `[[SEN2]]` — optional sensor points, same float32x3 layout.

## Layout

```
    50 4f 4f 32 00 00 00 78                  POO2...x    # size = 12 * N
    43 e1 00 00                              C...        # x = 490.0f
    00 00 00 00                              ....        # y = 0.0f
    44 3b 80 00                              D;..        # z = 756.0f
    ...
```

- No count prefix; `N = chunk_size / 12`.
- Each value is a *32-bit float in big-endian*, already scaled in the
  engine's units (see `src/sklt.cpp:78` `skeleton_read_pooX`).

### Legacy variant

`POOL` (v1) stored the same data as int16 xyz, 6 bytes per point.
Modern asset files always use `POO2` (12 bytes); the engine still reads
both (`sklt.cpp:78-108`). Keep reading both if you recover old CD data —
but generate only `POO2`.

## Coordinates

The engine keeps these coordinates unscaled until runtime; the parent
`[[STRC]]`'s `scale` (see `[[STRC]]`) transforms them at render/scene
build time — treat them as raw model-space floats.
