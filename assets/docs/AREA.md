# AREA: textured plane (part of a mesh)

*`area.class` node: a `[[ADE]]` with surface settings plus its texture
source. This is the format that gives a `[[SKLT]]` polygon UVs and a
bitmap.*

## Related format documents

- `[[ADE]]` — superclass.
- `[[STRC]]` — the second 10-byte flavor (`version 256` when read as ADE).
- `[[CIBO]]` — texture-plane bitmap reference (`NAM2`/`[[OTL2]]`).
- `[[SKLC]]` — skeleton link.
- `[[AMSH]]` — the other texture-plane source (animated mesh).
- `[[POO2]]`/`[[POL2]]` — geometry behind `point`/`poly`.

## Layout

```
FORM ... AREA
    ADE [ROOT/NAME, STRC <STRC_ADE bytes>]   # geometry anchor
    STRC <10 bytes STRC_AREA>                # surface settings
    OBJT ...                                 # bits: [[CIBO]]/[[SKLC]] bitmap refs
```

### STRC_AREA payload — `src/area.cpp:93`

```
 0  int16  version (=1)
 2  uint16 flags       (bit 1 dpthfade, bit 2 backcheck — same bits as ADE)
 4  uint16 polflags (bit meaning:)
        0x0001   scanline orientation: 0 = vertical, 1 = horizontal
        0x0002+0x0004 mapping: 00 none, 01 linear, 11 depth
        0x0008   textured when set
        0x0010+0x0020 shading: 00 none, 01 flat, 10 line, 11 gradient
        0x0040+0x0080 tracy: 00 none, 01 clear, 10 flat, 11 mapped
        0x0100   light
 6  byte   clrVal   # palette-ish color when not mapped
 7  byte   trcVal   # transparency
 8  byte   shdVal
```

Real bytes (`color=138, tracy=0, shade=128`):

```
    01 00 00 00 00 8a 00 00 80 00
```

### OBJT children

`area_func5__sub1` (`area.cpp:126`) loads exactly one `bitmap.class`
object per `OBJT` (`[[CIBO]]` or inline) and routes it:

- `polflags=0x8` (textured, non-tracy) → texture image,
- `polflags=0xC0` (only tracy-mapped) → transparency image,

because the texture bitmap used by this `AREA` is loaded through
`LoadObjectFromIFF` from the following form.

## Viewer notes

The uv source for `AREA` static textures is `amsh.olpl_points` semantics —
see `[[OLPL]]` for the byte-for-byte mapping. For `[[AMSH]]`-driven
animation, each frame's `vbmp_coords` defines its own uvs (`[[VANM]]`).
