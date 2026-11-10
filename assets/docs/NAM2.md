# NAM2: bitmap resource name

*Standalone NUL-terminated name chunk used by `[[CIBO]]` to point at a
bitmap stored in the same `[[EMBD]]` (`ilbm.class`).*

## Related format documents

- `[[CIBO]]` — owner.
- `[[NAME]]` — the other naming chunk (different owner, different use).
- `[[VBMP]]`, `[[ILBM]]` — target formats.

## Layout

```
    4e 41 4d 32 00 00 00 0d                  NAM2....
    41 49 52 31 54 58 54 2e 49 4c 42 4d 00   AIR1TXT.ILBM.
```

Engine bins it as a `rsrc`-resolvable name (up to 256 bytes,
`src/ilbm.cpp:44`). Names in the shipped set usually carry an explicit
extension (`.ILBM` in `CIBO/NAM2`); the tail byte is 0x00.
