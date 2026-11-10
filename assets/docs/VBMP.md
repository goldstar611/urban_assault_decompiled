# VBMP: indexed bitmap asset

`VBMP` is Urban Assault's embedded indexed-bitmap form. It stores palette
*indices*, not RGB pixels: the palette is supplied separately when the bitmap
is imported or displayed.

## Related format documents

- `[[FORM]]` — the IFF-style container that wraps `VBMP`.
- `[[HEAD]]` — bitmap dimensions and flags (6 bytes).
- `[[BODY]]` — indexed pixel bytes.
- `[[CMAP]]` — an ILBM palette; set 1 normally uses
  `assets/sets/set1/palette/standard.pal`. (No `CMAP` inside a VBMP.)
- `[[ILBM]]` — the engine's *alternative* format loaded through the same
  `ilbm.class` parser (`src/ilbm.cpp:262`).
- `[[BMHD]]` — the ILBM-side header, 20 bytes.
- `[[EMBD]]` — names and embeds a VBMP resource in a larger asset.
- `[[VANM]]` — bitmap animation data that refers to named VBMP frames.
- `[[CIBO]]` — the mesh-side reference path (`NAM2`/`[[OTL2]]`).

## On-disk layout

A VBMP is an IFF-style form:

```
FORM <big-endian u32 form-size> VBMP
    HEAD <big-endian u32 chunk-size> <6-byte payload>
    BODY <big-endian u32 chunk-size> <indexed pixel data>
```

`FORM`'s size includes the four-byte `VBMP` form type and all enclosed chunk
headers and payloads. Each chunk begins with its four-character identifier and
big-endian payload size. Odd-length chunk payloads receive a zero pad byte;
the stored size does not include that byte.

### HEAD

The `[[HEAD]]` payload is exactly six bytes:

| Offset | Type | Meaning |
| --- | --- | --- |
| 0 | big-endian `u16` | Width in pixels |
| 2 | big-endian `u16` | Height in pixels |
| 4 | big-endian `u16` | Flags |

The current import/export path creates 256 × 256 VBMPs and leaves `flags` at
zero. The engine *reads* flags (`src/ilbm.cpp:315`) but no known reader
consumes their value — treat as opaque and preserve verbatim.

### BODY

`[[BODY]]` contains one byte per pixel. Each byte is an index into the active
palette, ordinarily 256 entries. For a 256 × 256 bitmap this is 65,536 bytes.
The bytes are not RGB, alpha, or palette data.

## Palette relationship

The compiler derives its default palette from the `[[CMAP]]` chunk in
`assets/sets/set1/palette/standard.pal`. A `CMAP` payload is a sequence of RGB
triplets. The code turns each triplet into an opaque ARGB value for Qt and into
RGB bytes for Pillow.

Because VBMP stores only indices, changing the palette changes the rendered
colors without changing `[[BODY]]`. A bitmap exported by `Vbmp.save_to_bmp()`
is a paletted image with this palette attached.

**Open TODO (per-set palettes):** the palette is hardcoded to set 1's
`standard.pal`; other sets require an explicit palette-selection policy
(e.g. SET46's 828-byte `STANDARD.PAL` has a smaller header than the
896-byte set-1 file). See `[[CMAP]]`.

## Reading and writing with the current code

### Parse or serialize a VBMP form

`Vbmp().load_from_file(path)` parses the `FORM` file into its registered
children, including `Head` and `Body`. Calling `full_data()` on the resulting
form emits its IFF representation; `save_to_file(path)` writes those bytes to
disk. `Form().parse_stream()` is the lower-level parsing API that returns the
concrete registered `Vbmp` object directly.

To preserve an existing VBMP structurally, parse it and serialize it without
rebuilding `HEAD` or `BODY`.

### Import an image

`Vbmp().load_image(path)` accepts an image through Pillow. It:

1. preserves indices when the source is a 256 × 256 paletted image with the
   exact project palette;
2. otherwise converts the image to RGB, resizes it to 256 × 256 if necessary,
   and quantizes it to the default palette;
3. creates a `HEAD` and `BODY` pair for the result.

The first path matters for byte-exact rebuilds: converting an already-matching
paletted image through RGB can select different indices for visually identical
palette colors.

### Export an image

`Vbmp.save_to_bmp(path)` reads the indexed `BODY`, constructs a 256 × 256
Pillow `P` image, attaches the default palette, and saves it. It assumes the
stored body has the matching 256 × 256 length.

## Embedding and animation references

`[[EMBD]]` pairs a resource-name entry (`[[EMRS]]`) with the resource form.
`Embd.add_vbmp()` adds a VBMP using the `ilbm.class` resource class. The
higher-level `Mc2.add_image_from_file()` imports an image, appends `M` to the
image basename for the resource name, and embeds the resulting VBMP
(the `FOO.ILBM` → `FOOM`-style abbreviations are historical engine
behavior, kept for byte-parity).

`[[VANM]]` stores animation frame metadata. Its frame bitmap names resolve to
VBMP resource names in an enclosing `EMBD`; it does not duplicate pixel data.

## Validation and assumptions

- A normal VBMP has direct `HEAD` and `BODY` chunks.
- The current image conversion and BMP export paths assume 256 × 256 indexed
  images; non-square strip bitmaps (1×N seen in font pages) need the
  explicit `[[HEAD]]` dims honored by the parse path.
- Palette lookup currently defaults to set 1's `standard.pal`; other sets may
  require an explicit palette-selection policy in the future (see `[[CMAP]]`).
