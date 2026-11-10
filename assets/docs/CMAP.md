# CMAP: palette chunk

*RGB triplets (3 bytes per entry, no alpha); the only palette stored with
a bitmap. Sits inside `[[ILBM]]` — `[[VBMP]]` never carries one.*

## Related format documents

- `[[ILBM]]`, `[[BMHD]]`, `[[BODY]]` — siblings.
- `[[VBMP]]` — reads its palette from the external set palette instead.

## Layout

```
 0  R G B        # entry 0
 3  R G B        # entry 1
 ...             # 256 entries = 768 bytes
```

Engine: `src/ilbm.cpp:323` collects the palette into `ResBitmap.palette`.

## Set palettes

The engine loads palettes separately per set — the de-facto project
palette used by our toolchain is `assets/sets/set1/palette/standard.pal`
(palette file formats: `.PAL`/`_.pal` files are `CMAP`-suffixed
containers, sizes 896 = 24-byte header + 768 for `STANDARD.PAL`** and
828 for the SET46 variant).

Sharp corners:

- The same `[[BODY]]` indices render differently under different
  palettes — *palette identity is part of visual identity*.
- Our default palette (`standard.pal` of SET1) is hardcoded for the VBMP
  import path today; shipping per-set palettes (e.g. SET46's 828-byte
  file) is an open TODO documented in the viewer.
