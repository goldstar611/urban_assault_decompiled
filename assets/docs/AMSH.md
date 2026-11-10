# AMSH: animated mesh

*`amesh.class` node: attaches texture and attribute data per polygon of
the owning `[[SKLT]]`. `[[ATTS]]` holds per-poly attributes; `[[OLPL]]`
holds per-poly UV tables.*

## Related format documents

- `[[ATTS]]`, `[[OLPL]]` — payload chunks.
- `[[AREA]]` — the static-texture path (`[[CIBO]]`), a sibling mechanism.
- `[[POL2]]` — `ATTS.poly_id` indexes into the same polygons.
- `[[VBMP]]` — the texture that OLPL maps onto.
- `[[VANM]]`/`[[BANI]]` — the *animated* frames that replace static
  texture at runtime.
- `[[SKLT]]` — geometry it lays onto.

## Layout

```
FORM ... AMSH
    AREA ...               # optional; area rendering mode nodes
    ATTS <6 * polyCount>   # per polygon: s16 poly_id, u8 color, u8 shade,
                           #              u8 tracy, u8 pad
    OLPL <varies>          # per poly uv list
```

`src/amesh.cpp:87-131`: `TAG_ATTS` is `chunk_size / 6` entries; `TAG_OLPL`
is a list of `s16 count` pairs. `particle.class` (its cousin class) has
its **own, different** layout for `ATTS` — see `[[ATTS]]`.

## Real bytes (`VPfBRGR1.bas`, poly attrs; 10 entries × 6 bytes = 60)

```
    00 00 00 0b 80 00    poly_id 0,   color 11, shade 128, tracy 0
    00 01 00 00 80 00    poly_id 1,   color  0, shade 128, tracy 0
    ...
    00 09 00 00 80 00    poly_id 9,   color  0, shade 128, tracy 0
```

## Engine reading

`src/amesh.cpp`: `TAG_ATTS` → `ATTS` array of
`{polyID, colorVal, shadeVal, tracyVal, pad}`; `TAG_OLPL` → per-poly
`vector<tUtV>` where each uv pair is a *byte*:

```
uv.tu = byte / 256.0
uv.tv = byte / 256.0
```

Save sees the write side (`uv.tu * 256.0`). So the mapping of the map
plane to the `[[VBMP]]` source bitmap is `pixel = byte value` — no
bilinear filtering, no wrap, no clamp: the browser can index up to 255.

## Viewer caveat

Our tooling keeps an `ATTS`-order `[[OLPL]]` mapping for the static
texture path; see `bastoolsgui3.py` `find_static_textures`.
