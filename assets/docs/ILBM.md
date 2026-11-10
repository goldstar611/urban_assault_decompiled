# ILBM: paletted bitmap (IFF classic)

*The `.ILB`/`.ILBM` files shipped alongside the sets: an IFF form
holding `[[BMHD]]` + `[[CMAP]]` + `[[BODY]]`. The engine's `ilbm.class`
loads **either `ILBM` or `VBMP`** — they share one parser.*

## Related format documents

- `[[BMHD]]`, `[[CMAP]]`, `[[BODY]]` — children.
- `[[VBMP]]` — the sibling format; identical `BODY` semantics, but no
  inline palette.
- `[[CIBO]]` — how these are referenced from meshes.
- `[[EMBD]]` — where they are embedded inside a set.

## Layout

```
FORM ... ILBM
    BMHD <20 bytes>
    CMAP <768 bytes>      # optional; 256-entry palette
    BODY <w * h bytes>
```

## Engine reading

`src/ilbm.cpp:255-340` (`TAG_ILBM` vs `TAG_VBMP` check at the form level
first, then per-chunk). `BMD_ATT_CONVCOLOR` on the rsrc
(`ilbm.cpp:75`) tells the factory to pre-convert to 256-color indexed
with the global palette.

## disk-file extensions

The game data offers both `.ILB` and `.ILBM` files with identical
contents; when the same resource name appears once per extension in a
set (`LEGO4.ilb` vs `LEGO16.ILB`) the *engine* resolves both — our
toolchain needs the same tolerance, see `Mesh.load_ilbm_from_embd` (a
real bug where `.ILB`→`.ILM` was constructed cost us a hang once).

## Sizes and palette coupling

| palette-file | size |
| --- | --- |
| `SETn/PALETTE/STANDARD.PAL` | 896 (24-byte header + 768) |
| `SET46/PALETTE/STANDARD.PAL` | 828 (smaller header) |

`[[CMAP]]`-derived entries are 3 bytes each (RGB, alpha-less); the extra
bytes in the shipped `.PAL` files are *set-specific header*, not entries.
The authoritative per-set palette policy is a documented TODO (see
`[[VBMP]]`).
