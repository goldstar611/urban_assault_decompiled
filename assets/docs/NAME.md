# NAME / NAM2: name strings

Both are NUL-terminated name strings; they differ by *what they name*.

## Related format documents

- `[[OBJT]]`, `[[BASE]]` — owners of `NAME` (object identity).
- `[[SKLC]]` — owner of `NAME` (global resource name).
- `[[CIBO]]` — owner of `NAM2` (embedded bitmap resource name).

## NAME chunk

Used twice: to name a node (`ROOT/NAME` inside a `[[BASE]]`, e.g.
`VPfFLUG1`), and to link a skeleton resource (`[[SKLC]]`/`NAME`,
e.g. `Skeleton/DUMMY.sklt`).

```
    4e 41 4d 45 00 00 00 08                  NAME....
    56 50 66 42 52 47 52 31                  VPfBRGR1
```

No NUL terminator for node names in the watched file; resource `NAME`
inside `[[SKLC]]` ends with `\0` (13 bytes: `base-NAME "Skeleton/DUMMY.sklt\0"`).

## NAM2 chunk

Owned by `[[CIBO]]`, names a bitmap resource inside the same `[[EMBD]]`
storehouse, always `.ILBM` there:

```
    4e 41 4d 32 00 00 00 0d                  NAM2....
    41 49 52 31 54 58 54 2e                  AIR1TXT.
    49 4c 42 4d 00                           ILM.
```

Engine: `src/ilbm.cpp:42` reads up to 256 bytes from `TAG_NAM2`, then finds
the named resource by name and trims a trailing NUL.

## Which to use where

| doc | owner | notes |
| --- | --- | --- |
| `[[NAME]]` | `ROOT/NAME` in `BASE` trees | object identity, no NUL pad |
| `[[NAME]]` | `SKLC/NAME` | global resource path with `\0` |
| `[[NAM2]]` | `CIBO/NAM2` | bitmap resource path with `\0` |

Note for implementers: strip `\0` before string comparisons; `gui`'s
resource matching has tripped on trailing whitespace/NULs before.
