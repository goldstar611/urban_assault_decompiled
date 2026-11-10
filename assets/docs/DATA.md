# DATA: the VANM byte payload

*Single chunk inside a `FORM/`[[VANM]]`. Its content is identical to the
raw `rsrcpool/<name>.ANM` byte stream — no chunk framing inside.*

Full annotated layout, the example from an `FX2.ILBM` animation
(4 polygons, 8 frames):

```
000b                                # len class_id
69 6c 62 6d 2e 63 6c 61 73 73 00    # = "ilbm.class\0"
000a                                # len names blob
46 58 32 2e 49 4c 42 4d 00 00       # = "FX2.ILBM\0\0" (NUL-separated frames)
0019                                # len poly table
0004 19 42 01 42 01 01 19 01        # poly 0: 4 verts (x,y byte pairs)
0004 1e 12 1e 07 26 07 26 12        # poly 1
0004 18 42 3a 42 3a 01 18 01        # poly 2
0004 60 01 3a 01 3a 42 60 42        # poly 3
0004 5c 42 5c 01 82 01 82 42        # poly 4
0008                                # frame count
00000050 0000 0000                  # t=80  bitmap_idx 0 texcoord_idx 0
00000028 0000 0001                  # t=40  bitmap_idx 0 texcoord_idx 1
00000050 0000 0002                  # t=80  ...
00000028 0000 0001                  # t=40 ...
00000050 0000 0003                  # t=80 ...
00000028 0000 0001                  # t=40 ...
00000050 0000 0004                  # t=80 ...
00000fa0 0000 0001                  # t=4000 (4000 = loop marker)
00                                  # pad
```

## Fields

- `class_id` — the class that builds the bitmaps; `ilbm.class` in every
  shipped asset.
- names blob — NUL-separated frame-bitmap names, resolved against the
  enclosing `[[EMBD]]`; usually one name reused by all frames (the uv
  table moves the textured window across the bitmap).
- poly table — same "u16 count then `x,y` byte pairs" recursion as
  `[[OLPL]]`; `tu = x/256.0`, `tv = y/256.0`.
- frame list — per frame: `s32 time.tick`, `s16 frame_id`, `s16
  texcoords_id` (indexes the poly table consumed by the frame's bitmap).

## Engine reading

`src/bmpAnm.cpp:255` `LoadFromFile` (raw check first: `TAG_FORM`
detection distinguishes raw file vs. embedded form); readers
`ReadClassName`, `ReadBitmapNames`, `ReadTexCoords`,
`ReadFrameData` (`bmpAnm.cpp:128-240`).
