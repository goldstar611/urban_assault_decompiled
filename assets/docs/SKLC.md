# SKLC: skeleton class link

*A `FORM/SKLC` whose only child is a `[[NAME]]` chunk naming a skeleton
resource — the mechanism by which a `[[BASE]]` tree derives its mesh.*

## Related format documents

- `[[OBJT]]` — a `sklt.class` node.
- `[[NAME]]` — the resource path it points at.
- `[[SKLT]]` — the target skeleton form.
- `[[EMBD]]` — where the named resource resolves.
- `[[MC2]]` — the set-level application.

## Layout

```
FORM ... SKLC
    NAME <resource-path\0>    # e.g. "Skeleton/DUMMY.sklt\0"
```

## Engine reading

`src/sklt.cpp:36` `NC_STACK_sklt::rsrc_func64` and the
`saving` counterpart at `sklt.cpp:66` push `FORM/SKLC [NAME]`; readers
resolve by resource name against the class-registry resources.

## Tooling notes

Our `gui` viewer treats a `sklt.class` OBJT as the *renderable skeleton*
entry gate; it merges several skin nodes that share one `SKLC` name into
one render group — see `RENDERABLE_CLID_CLASSES` in `bastoolsgui3.py`.
