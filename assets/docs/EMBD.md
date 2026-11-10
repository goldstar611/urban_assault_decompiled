# EMBD / EMRS: resource storehouse

*`embed.class` payload: a bag of named resources paired with a class name
each. It is the only place where `[[SKLT]]`, `[[VBMP]]`, `[[VANM]]` blobs
live in a set.*

## Related format documents

- `[[OBJT]]` — the embed node whose CLID is `embed.class`.
- `[[SKLT]]`, `[[VBMP]]`, `[[VANM]]` — the embedded resource forms.
- `[[ROOT]]` (`NAME`-less) — the first child, no meaning, always present.
- `[[MC2]]` — the embedding node in a set-level tree.

## Layout

`EMBD` children are: `ROOT`, then **(EMRS, resource)** pairs:

```
FORM ... EMBD
    ROOT                      # empty
    EMRS <class\0name\0\0>    # class+resource pair (the *next* chunk's owner)
    FORM resource ...         # e.g. FORM/SKLT, FORM/VBMP, FORM/VANM
    EMRS ...
    FORM resource ...
    ...
```

The `EMRS` payload is a NUL-separated pair `class\0name\0` plus a final
`0x00` pad byte written by the engine (`src/embed.cpp:114-116`):

```
    45 4d 52 53 00 00 00 1f                  EMRS....
    73 6b 6c 74 2e 63 6c 61 73 73 00         sklt.class.
    53 6b 65 6c 65 74 6f 6e 2f 53 30 30      Skeleton/S00
    48 2e 73 6b 6c 74 00                     H.sklt.
    00                                       .   <- the engine's extra U8(0)
```

Sizes seen in the wild: `class` is `"sklt.class"` (10) or `"ilbm.class"`
or `"bmpanim.class"`; `name` has folders (`Skeleton/`, `rsrcpool/`).
Resolve the resource by opening the *next chunk* (`PIFFFILE`,
`embed.cpp:84-92`).

## Engine reading

`src/embed.cpp:61-92`: `TAG_EMRS` payload is read as
`class\0name\0...`; the code:

- splits at the first `\0` into `classname` and `resname`;
- strips further `\0`s from each (off-by-one tolerance);
- instantiates `classname` with `name=resname` and `TRYSHARED`,
  passing the live IFF file so the resource form that *follows* gets
  picked up by the class's own reader.

Writers must emit the extra `0x00` byte after the name — otherwise the
decompiled parser's byte count mismatches on odd payloads.

## Compile-side notes

Only `sklt.class`, `ilbm.class` and `bmpanim.class` resources are resolved
by our tooling; other class ids stay as raw `EMRS` records. Resource order
is preserved (see `resource_order.json` manifests written by
`decompile_set_bas.py`) — ordering is load-bearing for byte-exact sets.
