# CLID: class identifier

*One-line chunk: a NUL-terminated class name that tells the engine which
built-in object class to instantiate for the enclosing `[[OBJT]]`.*

## Related format documents

- `[[OBJT]]` — the object this identifies.
- `[[FORMATS]]` — the class list lives here.

## Layout

Exactly 11 bytes in practice (`0000000B` length prefix covers 10 chars +
NUL):

```
    43 4c 49 44 00 00 00 0b 62 61 73 65      CLID....base
    2e 63 6c 61 73 73 00                     .class.
```

The engine parser (`src/base.cpp` etc.) treats `CLID` as `TAG_CLID` inside
an `OBJT` and then dispatches by matching class id against
`__ClassName` constants in each subsystem header (`base.h:207`,
`embed.h:23`, `sklt.h:22`, `area.h:118`, `ade.h:85`, `amesh.h:57`,
`particle.h:119`, `bmpAnm.h:107`, `bitmap.h:58`, `ilbm.h:60`).

## Class ids that appear in set assets and what they mean

| class id | doc | used on |
| --- | --- | --- |
| `base.class` | `[[BASE]]`, `[[OBJT]]` | container node |
| `embed.class` | `[[EMBD]]` | resource store node |
| `sklt.class` | `[[SKLT]]`, `[[SKLC]]` | skeleton link or skeleton resource |
| `ade.class` | `[[ADE]]` | detail node |
| `area.class` | `[[AREA]]` | textured plane node |
| `amesh.class` | `[[AMSH]]` | animated mesh node |
| `particle.class` | `[[AMSH]]` note | particle emitter (own `ATTS` layout!) |
| `bmpanim.class` | `[[VANM]]` | animation player |
| `bitmap.class` | `[[VBMP]]`, `[[ILBM]]` | raw image resource |
| `ilbm.class` | `[[ILBM]]`, `[[VBMP]]` | ilbm-or-vbmp image class |

## Caveat

`CLID` strings end in `.class`; the engine's own identifiers are that
`__ClassName` token. `gui`'s `RENDERABLE_CLID_CLASSES` allow-list is a
viewer-side convenience, not part of the format.
