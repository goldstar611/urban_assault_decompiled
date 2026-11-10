# CIBO: outline bitmap reference

*A `bitmap.class` reference to a naming-`NAM2` bitmap plus an optional
`[[OTL2]]` outline. Used by `[[AREA]]` texture-plane children and by
UI-space images walked by the game.*

## Related format documents

- `[[NAM2]]`, `[[OTL2]]` — payload chunks.
- `[[VBMP]]`, `[[ILBM]]` — the referenced bitmap formats.
- `[[AREA]]` — the consumer inside a mesh.
- `[[BANI]]` — the animated sibling path.

## Layout

```
FORM ... CIBO
    NAM2 <name\0>          # bitmap resource name, see NAM2
    OTL2 <2 * count>       # optional outline, see OTL2
```

## Engine reading

`src/ilbm.cpp:91` reads `CIBO` children: `TAG_NAM2` (up to 256 bytes) →
resource name; `TAG_OTL2` → outline uv list. When the name resolves, the
`ilbm.class` factory loads either `[[ILBM]]` or `[[VBMP]]` content —
this intersection is why our `Mesh.load_ilbm_from_embd` must handle
`.ILB`/`.ILBM` extension mismatches.

## Caveats

- A `CIBO`'s name needs the enclosing `[[EMBD]]` to resolve; there is no
  fallback path on other class ids.
- `otl2` counts everything per uv as in `[[OLPL]]` (byte/256 semantics);
  128 bytes max observed (64 pairs).
