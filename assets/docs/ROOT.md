# ROOT: object-tree node marker

*A form whose body is empty or carries a `[[NAME]]` chunk. Marks the top of
a `[[BASE]]` or `[[ADE]]` payload.*
## Related format documents

- `[[BASE]]`, `[[ADE]]` — owners.
- `[[NAME]]` — the optional child.
- `[[EMBD]]`, `[[MC2]]` — always-present children (unnamed).

## Layout

```
    52 4f 4f 54 00 00 00 00                  ROOT....     # unnamed
    52 4f 4f 54 ... 4e 41 4d 45 ...          ROOT....NAME. # named variant
```

The engine loads `ROOT` as the identity step
(`NC_STACK_nucleus::LoadingFromIFF`); naming is traditional but a
missing name is fine (see `[[MC2]]`: the set root has none).

## Reader note

`ROOT`'s content is ignored beyond the name; writers must reproduce it
verbatim because its *presence* (or absence) shifts chunk alignment in
the parent form.
