# BODY: indexed pixel bytes

*One byte per pixel, palette indices — no palette inside.*

## Related format documents

- `[[HEAD]]` — width/height, `lunghezza = w * h`.
- `[[CMAP]]` — where the palette lives in `[[ILBM]]`; in `[[VBMP]]`,
  the palette is supplied externally (`standard.pal`).
- `[[VBMP]]`, `[[ILBM]]` — owners.

## Layout

`width * height` bytes. Index `i` renders as palette entry `i`
(`[[CMAP]]`/`standard.pal`), including the palette's transparent entry
where the consumer cares about transparency (the viewer keying looks for
the bright-yellow family, see `Animation.map_yellow_to_alpha`).

No compression; odd `BODY` sizes receive one zero pad byte per `[[FORM]]`
framing.

## Byte reference

A 256×256 `BODY` is exactly `00 01 00 00` (`0x00010000 = 65536`) bytes
long. Any `BODY` whose size doesn't match its `[[HEAD]]` should fail
round-trip asserts in our parser.
