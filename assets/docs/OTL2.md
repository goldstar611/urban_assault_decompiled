# OTL2: outline coordinates

*Optional `[[CIBO]]` child: a fixed-capacity uv list. Same byte/256
mapping as `[[OLPL]]`.*

## Related format documents

- `[[CIBO]]` — the owner.
- `[[OLPL]]` — the shaped sibling with the per-poly `u16` count.

## Layout

No count prefix; the size/capacity is decided by the owner
(`ilbm.cpp:119` writes `opl2.size() * 2`). Reading:

```
 0  byte   x / 256.0
 1  byte   y / 256.0
 2  ...                       # pairs until the chunk ends
```

Read bounded — the engine reads at most 128 bytes (`src/ilbm.cpp:52`,
`uint8_t dst[128]`): 64 uv pairs hard limit.
