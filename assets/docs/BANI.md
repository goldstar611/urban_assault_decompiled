# BANI: bitmap animation link

*One per animated polygon of a model; the engine turns it into a
`bmpanim.class` resource that resolves `rsrcpool/<name>.ANM` at load
time. Each BANI carries no bitmap data — only settings plus the ANM file
name.*

## Related format documents

- `[[VANM]]` — the `.ANM` byte layout it points at.
- `[[STRC]]` — the BANI-specific flavor (6 bytes + name).
- `[[AMSH]]` — where these often sit (shelf-by-shelf texture planes).
- `[[VBMP]]` — the frames' bitmap destination.
- `[[BASE]]` — where `BANI` OBJTs live in a tree.

## Layout

```
FORM ... BANI
    STRC <6 + name bytes>   # the BANI flavor; no other children
```

Note: **no `CLID`** — `bmpanim.class` is implied by the engine's
`NC_STACK_bmpanim::LoadingFromIFF` (the form type decides the class).

### STRC payload — `src/bmpAnm.cpp:46`

```
 0  int16  version   (=1)
 2  int16  offset    (=6: absolute offset of the name inside the payload)
 4  int16  animType  (=0 in every shipped asset)
 6  ...    name, NUL-terminated, e.g. "BLITZL1.ANM"
```

Real bytes:

```
    00 01 00 06 00 00 42 4c 49 54 5a 4c 31 2e 41 4e    .  ..  BLITZL1.AN
    4d 00                                             M.
```

The engine computes `anmName = buf[offset - 6]` (`bmpAnm.cpp:79`) —
`offset` is therefore redundant with the constant 6, but *is* saved and
must be 6 or the name reads from the wrong place.

## Resolution

`src/bmpAnm.cpp:255`: the name is opened as `rsrc:rsrcpool/<name>` —
the resource pool mounts the set's `RSRCPOOL` directory. The `.ANM` is
the `[[VANM]]` byte layout; see that doc.

## animType

All shipped BANIs carry `animType = 0`. The engine passes it to
`BANM_ATT_ANIMTYPE`; the only known consumer differences are
engine-internal. Don't invent values — keep 0.
