# BMHD: ILBM bitmap header

*The `[[ILBM]]` analog of `[[HEAD]]`: 20 bytes with richer metadata
(plane count, masking, aspect, page size). Only ever inside `ILBM` forms.*

## Related format documents

- `[[ILBM]]`, `[[CMAP]]`, `[[BODY]]` — siblings that consume this meta.
- `[[HEAD]]` — the VBMP-style 6-byte header.

## Layout (20 bytes, all big-endian)

```
 0 u16 width
 2 u16 height
 4 u16 x
 6 u16 y
 8 s8  nPlanes
 9 s8  masking
10 s8  compression
11 s8  flags
12 u16 transparentColor
14 s8  xAspect
15 s8  yAspect
16 u16 pageWidth
18 u16 pageHeight
```

Engine reader: `src/ilbm.cpp:287-311` (`TAG_BMHD` branch of the
`ilbm.class` parser).

## Writers

`src/ilbm.cpp:515` writes `flags = 0x80` for new ILBMs; preserved values
must round-trip.
