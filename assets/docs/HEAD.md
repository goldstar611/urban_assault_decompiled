# HEAD: VBMP header

*First child of a `[[VBMP]]`: 6 bytes. Width, height, flags.*

## Related format documents

- `[[VBMP]]`, `[[BODY]]` — the format this sizes.
- `[[BMHD]]` — the `[[ILBM]]` header (a different 20-byte layout).

## Layout

```
    48 45 41 44 00 00 00 06                  HEAD....
    <u16 width>  <u16 height>  <u16 flags>
```

Engine reader (`src/ilbm.cpp:313`):

```
vbmp.width  = readU16B()
vbmp.height = readU16B()
vbmp.flags  = readU16B()
```

## Flags

Parsed but never consulted by any known engine reader; writers emit `0`.
Treat the stored value as opaque — preserve it verbatim on lossless
rebuild (`compile.Head.set_binary_data` asserts round-trip with the
parsed bytes).

## Size invariants

- `BODY` byte count must be `width * height` for the common 256×256 case
  (`# 0x00 0x00` and `# 0x01 0x00` pairs elsewhere are the *only*
  non-square sizes seen in the wild: 1×N / M×1 strip headers appear in
  font pages).
