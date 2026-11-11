# STRC: structure chunk (the messy one)

*The most mis-documented format in the set: `STRC` has **no type field**.
The engine picks the payload shape purely from **who owns the chunk**
(`NC_STACK_base` vs `NC_STACK_ade` vs `NC_STACK_area` vs `NC_STACK_bmpanim`)
— four distinct layouts. There is no in-band "STRC_BASE"/"STRC_AREA" label
anywhere in a real file.*

## Related format documents

- `[[BASE]]` — owns the 62-byte flavor.
- `[[ADE]]` — owns the 10-byte flavor version 1.
- `[[AREA]]` — owns the 10-byte flavor version 256 (`0x0100`).
- `[[BANI]]` — owns the BANI flavor (`version 1, offset 6`).
- `[[SKLT]]`, `[[AMSH]]` — consumers.

## The four layouts

### 1) `[[BASE]]` (STRC_BASE), 62 bytes — `src/base.cpp:77`

```
 0  int16  version (=1)
 2  float  pos.x       6  float pos.y     10  float pos.z
14  float  vec.x (move)18  float vec.y    22  float vec.z
26  float  scale.x     30  float scale.y  34  float scale.z
38  int16  ax          40  int16 ay       42  int16 az      (euler)
44  int16  rx saved    46  int16 ry saved 48  int16 rz saved
50  int16  flags (bit 6 = follow-parent)
52  int16  (unused)
54  int32  vis_limit
58  int32  ambient_light
```

Real bytes (`VPfBRGR1.bas`, the set-1 root vehicle):

```
    00 01 00 00 00 00 00 00 00 00 00 00       version 1, pos 0,0,0
    00 00 00 00 00 00 00 00 3f 80 00 00       vec 0,0, scale.x=1
    3f 80 00 00 3f 80 00 00 00 00 00 00       scale.y=z=1, euler 0
    00 00 00 00 00 00 00 00 00 00 00 48       rotations 0, flags 0x48
    00 00 00 00 10 00 00 00 00 ff             vis_limit=4096, light=255
```

Engine: `ReadIFFTagSTRC` only *applies* fields when `version >= 1`.
`fadeStart`/`fadeLength` are **not in the chunk** — they are engine
defaults (`base.cpp:234`).

### 2) `[[ADE]]` (STRC_ADE), 10 bytes — `src/ade.cpp:75`

```
 0  int16  version (=1)
 2  byte   _nu1 (=0)
 3  byte   flags (bit 1 = depth-fade, bit 2 = back-check)
 4  int16  point   # index into the parent [[SKLT]]'s [[POO2]]
 6  int16  poly    # index into the parent's [[POL2]]
 8  int16  _nu2 (=0)
```

Real bytes (an area-definition ADE, `point=4`, `poly=10`):

```
    00 01 00 04 00 00 00 0a 00 00     version 1, flags 0, point 4, poly 10
```

### 3) `[[AREA]]` (STRC_AREA), 10 bytes — `src/area.cpp:89-122`

```
 0  int16  version (=256, i.e. 0x0100 big-endian)
 2  uint16 flags  (bit 1 = depth-fade, bit 2 = back-check)
 4  uint16 polFlags (see [[AREA]] for the bit meanings and render modes)
 6  byte   _un1 (=0)
 7  byte   clrVal
 8  byte   trcVal
 9  byte   shdVal
```

Real bytes (a LUMTRACY texture plane from `VPfJET1`, set 1):

```
    01 00 00 00 00 8a 00 00 80 00     ver 256 (0x0100), flags 0,
                                      polFlags 0x8a = 138
                                      (LINEARMAPPED|TEXBIT|FLATTRACY),
                                      clrVal 0, trcVal 0, shdVal 128
```

(`version >= 1` is the only test the engine makes on this field
(`area.cpp:105`), so the 256 still passes — the values are applied
regardless.)

**Trap**: if an ADE reader (layout 2) parses an AREA chunk, its `version`
field reads as **256** instead of 1, because the AREA flavor stores
`0x0100` big-endian. Our `compile.Strc` factory exploits this
(`set_binary_data`: length 10 + `version==256` → AREA). It's a heuristic,
not a format feature.

### 4) `[[BANI]]` (STRC_BANI), 6 + name bytes — `src/bmpAnm.cpp:46`

```
 0  int16  version (=1)
 2  int16  offset   (always 6: byte offset of the name within the payload)
 4  int16  animType (=0 in all shipped assets)
 6  ...    name, NUL-terminated, e.g. "BLITZL1.ANM"
```

Real bytes:

```
    00 01 00 06 00 00 42 4c 49 54 5a 4c 31 2e 41 4e    01 06 00 BLITZL1.AN
    4d 00                                             M.
```

Engine reads `buf[offset - 6]` — that is why writers must keep `offset=6`
and put the name exactly there.

## How our toolchain labels them

`compile.Strc` infers the flavor, in order:
1. `len == 62` → `STRC_BASE`
2. `len == 10` and version==1 → `STRC_ADE`; version==256 → `STRC_AREA`
3. payload starting `00 01 00 06 00` → `STRC_BANI`
4. otherwise `STRC_UNKNOWN` (kept verbatim)

These labels are **porting artifacts**, not on-disk data (the engine and
the original files never store a type string). If you meet a 10-byte
`STRC` whose version is neither 1 nor 256, our inference has failed —
fall back to the owner form to decide.

## Who am I? — the human confusion

People (and older docs) report "3 STRC types". From the ground truth
there are **four**; the BANI one is the one that gets missed because it
only appears inside `[[BANI]]` forms attached to `[[AMSH]]`/`[[BASE]]`
detail nodes and is easy to read as layout 2 or 3 since it is also
< 62 bytes.
