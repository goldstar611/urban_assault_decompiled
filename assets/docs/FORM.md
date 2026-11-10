# FORM: container chunk

*Urban Assault asset files are chains of `FORM` containers, each wrapping a
run of child chunks.*

## Related format documents

- `[[MC2]]`, `[[OBJT]]`, `[[BASE]]`, `[[EMBD]]`, `[[SKLT]]`, `[[VBMP]]`,
  `[[VANM]]`, `[[AMSH]]`, `[[ADE]]`, `[[AREA]]`, `[[BANI]]`, `[[CIBO]]`,
  `[[SKLC]]`, `[[ADES]]` — container `FORM`s with the extension deciding which
  of these interpretation applies.
- `[[CLID]]`, `[[NAME]]`, `[[STRC]]`, `[[EMRS]]`, `[[KIDS]]`, `[[POO2]]`,
  `[[POL2]]`, `[[SEN2]]`, `[[ATTS]]`, `[[OLPL]]`, `[[OTL2]]`, `[[HEAD]]`,
  `[[BODY]]`, `[[CMAP]]`, `[[BMHD]]`, `[[DATA]]` — leaf chunks usually found
  directly inside a `FORM`.

## On-disk layout

```
FORM <big-endian u32 payload-size> <4-byte format-extension>
    ... child chunks ...
```

- The size field covers the 4-byte extension plus everything after it,
  *excluding* the 8-byte `FORM <size>` header itself.
- Children may be leaf chunks or nested `FORM`s.
- IFF-style padding: a leaf chunk payload that is odd-length is followed by
  one pad zero-byte, which is *not* counted in the chunk's size field
  (the padding sits inside the enclosing form's size, though).

## Reading via the decompiled engine

`src/IFFile.cpp/.h` implements the parse loop; `mfile->parse()` returns the
next chunk (or `IFF_ERR_EOC` at form end). Readers walk the children and
`skipChunk()` anything they don't recognize — so unknown chunk identifiers must
be tolerated by writers that want engine compatibility.

## Engine note

`src/utils.h` defines every known identifier as `TAG_x` through `MKTAG`.
Those tags are the authoritative set of format names used in the other
documents.
