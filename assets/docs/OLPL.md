# OLPL: per-polygon uv lists (texture mapping)

*Sits inside an `[[AMSH]]` next to `[[ATTS]]`: a per-poly list of byte
uv-pairs. This is what puts a static `[[VBMP]]` texture onto a polygon.*

## Related format documents

- `[[AMSH]]` — owner.
- `[[ATTS]]` — per-poly attributes, `poly_id` keys the same geometry.
- `[[VBMP]]` — the fetched bitmap (256×256 indexed palette `[[BODY]]`).
- `[[VANM]]` — replaces OLPL with per-frame uvs when animated.
- `[[POL2]]` — geometry.

## Layout

No global count: the chunk is a list of "s16 count, count×2 bytes" until
the chunk size runs out. The number of lists must equal the `[[AMSH]]`'s
polyCount.

```
    00 04                            # uv count for poly 0 = 4
    eb fd 76 fd 76 82 eb 82          # x0 y0 (235,253) ... (235,130)
    00 04 eb fd 76 fd 76 82 eb 82 ...   # poly 1 same table (quad)
    ...
```

Mapping (from `src/amesh.cpp:110`):

```
uv.tu = x_byte / 256.0    # in the [0,1) texture coordinate space
uv.tv = y_byte / 256.0
```

In the shipped assets the uv coord pair is essentially a *pixel index*
into the 256×256 `[[VBMP]]` bitmap; both views are equivalent.

## Engine reading

`[[AMSH]]` reads it in a single pass (`TAG_OLPL` case); no explicit poly
prefix — you reconstruct a poly-boundary by the leading `u16` count. `TAG`
order between `ATTS`/`OLPL` does not matter for the engine, but our
toolchain currently assumes `ATTS`-then-`OLPL` per `[[AMSH]]` form — keep
that order when writing.
