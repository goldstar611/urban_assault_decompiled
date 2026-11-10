# EMRS: resource name pair

*One `EMRS` chunk + its resource form = one entry in an `[[EMBD]]`. The
payload names (class id, resource name); the resource form *follows it*
as the next chunk.*

## Related format documents

- `[[EMBD]]` — the pairing container.
- `[[SKLT]]`, `[[VBMP]]`, `[[VANM]]` — resource forms this refers to.
- `[[CLID]]` — the same class-id vocabulary, different context.

## Layout

Payload: `class\0name\0` plus a final `0x00` that the engine's writer
emits (`src/embed.cpp:114-116`):

```
    45 4d 52 53 00 00 00 1f                  EMRS....   # 31-byte payload
    73 6b 6c 74 2e 63 6c 61 73 73 00          sklt.class.
    53 6b 65 6c 65 74 6f 6e 2f 53 30 30 48    Skeleton/S00H
    2e 73 6b 6c 74 00                        .sklt.
    00                                       .          # extra pad byte
```

Sizes: 31 here; the class string is either `sklt.class` (10 bytes),
`ilbm.class`, or `bmpanim.class` in all shipped sets.

## Resolution rules (`src/embed.cpp:61-92`)

1. payload is a NUL-separated list — split on the first `\0` into
   `classname`, `resname`;
2. trim **additional** trailing `\0`s (only a warning; our parser does
   the same);
3. instantiate the class named by `classname` with `name=resname` and
   `TRYSHARED`, handing it the live IFF stream so the resource form that
   immediately follows is consumed by the class reader.

Common resource names and their folder prefixes:

| prefix | resource |
| --- | --- |
| `Skeleton/…` | `[[SKLT]]` |
| `rsrcpool/…` | `[[VANM]]` (the `.ANM` form) |
| `(none)` | `[[VBMP]]`/`[[ILBM]]` name (e.g. `FOOM`) |

## Writer pitfalls

- The `0x00` pad byte after the name is mandatory for engine-parity.
- Case *matters*: a set can hold both `Skeleton/` and `skeleton/`
  prefixes for different resources — the byte-exact set builders replay
  the original order from `resource_order.json` manifests written by
  `decompile_set_bas.py`.
