# OBJT: object node

*Worker form of the game's object tree: an object instance with a class and
a payload.*

## Related format documents

- `[[FORM]]` — container that wraps it, extension always literally `OBJT`.
- `[[CLID]]` — first child, names the class.
- `[[BASE]]` — payload for `base.class` nodes.
- `[[EMBD]]` — payload for `embed.class` nodes.
- `[[ADE]]`, `[[AREA]]`, `[[AMSH]]`, `[[BANI]]`, `[[SKLC]]` — payload refs
  attached under `[[ADES]]` containers in `base.class` nodes.
- `[[ROOT]]`/`[[NAME]]` — identity.

## Layout

```
FORM ... OBJT
    CLID <class_id>          # e.g. "base.class", "embed.class", "sklt.class"
    ... payload children (exact list depends on the class) ...
```

Known shapes in the set `.bas` assets:

```text
base.class    FORM/OBJT [CLID, FORM/BASE [ROOT, OBJT..., STRC, KIDS ...]]
embed.class   FORM/OBJT [CLID, FORM/EMBD [ROOT, EMRS, resource, EMRS, ...]]
sklt.class    FORM/OBJT [CLID, FORM/SKLC [NAME]]    # skeleton class link
```

An example from `VPfFLUG1.bas.json` — a base-class node whose `ROOT` is
named `VPfFLUG1`:

```
    46 4f 52 4d .. .. .. .. 4f 42 4a 54       FORM....OBJT
    43 4c 49 44 00 00 00 0b 62 61 73 65       CLID....base
    2e 63 6c 61 73 73 00                      .class.
```

## Engine reading

The engine picks the class from the `CLID` and then calls the matching
`LoadingFromIFF` (`src/base.cpp`, `embed.cpp`, `sklt.cpp`, `area.cpp` …).
Anything unknown is skipped — chunk *order* is mostly irrelevant except for
`base.class` loaders that switch between the `STRC` and sub-`OBJT` paths (see
`src/base.cpp:225`). Keep the order the originals use: `CLID` first, then
`BASE`/`EMBD` payload.
