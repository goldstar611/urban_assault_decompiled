# VANM: bitmap animation resource (`rsrcpool/*.ANM`)

*Named animation resource: a class name, one or more bitmap names, a
shared uv-table, and a frame list. Live as raw `rsrcpool/<name>.ANM`
byte-stream files (not IFF!) or embedded in an `[[EMBD]]` as a `VANM`
form whose single `DATA` chunk is the same byte layout.*

## Related format documents

- `[[BANI]]` — the container-side link that names this resource.
- `[[VBMP]]` — the bitmap each frame refers to by name.
- `[[AMSH]]`/`[[OLPL]]` — uv space is defined in the same way
  (byte / 256).
- `[[EMBD]]` — where an embedded `VANM` lives its storehouse life.

## Raw `.ANM` byte layout (the DATA chunk payload):

```
0002                                  # len class name
"ilbm.class\0"                        # class for the bitmap factory
0002                                  # len names blob                                   ↓
"<name1>\0<name2>\0...\0"             # NUL-separated bitmap names; trailing \0
0002                                  # total polygon table length (u16, bytes)
...
0002                                  # per-poly table: count of vertices (u16)
0002 ... x y pairs everyone           # byte x, byte y (tu = x / 256.0)
0002                                  # frame count (u16)
<frame time> s32, <frame id> s16, <texcoords id> s16
...
```

Concretely, a `[[VANM]]`'s `DATA` chunk from `FX2.ILBM` (4 frames):

```
    00 0b                                     # 11 = len class name
    69 6c 62 6d 2e 63 6c 61 73 73 00           ilbm.class>
    00 0a                                     # 10 = len names blob
    46 58 32 2e 49 4c 42 4d 00 00              FX2.ILBM>
    00 19                                     # 25 = len poly table
    00 04 19 42 01 42 01 01 19 01              #    # poly 0: 4 verts
    00 04 1e 12 1e 07 26 07 26 12              # poly 1
    00 04 18 42 3a 42 3a 01 18 01              # poly 2
    00 04 60 01 3a 01 3a 42 60 42              # poly 3
    00 04 5c 42 5c 01 82 01 82 42              # poly 4
    00 08                                     # 8 = frame count
    00 00 00 50 00 00 00 00                    # t= 80, bitmap 0, tc 0
    00 00 00 28 00 00 00 01                    # t= 40, bitmap 0, tc 1
    ...
    00                                        # pad
```

## Timing

`FrameTime` is a *raw timer tick* value (s32). The shipped animations
pattern is two values alternating per frame (t=0x50/0x28 in the example);
the engine multiplexes time-based frame advance.

## Texcoords

The `TexCoords` table is *shared* and indexed by the frame:
one entry per polygon — each vertex is 2 bytes, divided by 256 at load
time (`src/bmpAnm.cpp:200`; matches `[[OLPL]]`).

## Embedding

When an `[[EMBD]]` carries one, the resource is stored as
`FORM/VANM [DATA]` where `DATA` is exactly the byte series above. Bitmap
names resolve inside the same `[[EMBD]]` (see `[[VBMP]]`).

## Engine reading

`src/bmpAnm.cpp:240` `LoadFromFile`: opens `rsrc:rsrcpool/<name>`,
checks for a `FORM` tag (embedded case), then reads 4 sections in order.
`bmpanim.class` and `ilbm.class` are the only known values of the
`class_id`; `BANM_ATT_ANIMTYPE` set on the `[[BANI]]` `STRC` is the
consumer's playback-ish mode.
