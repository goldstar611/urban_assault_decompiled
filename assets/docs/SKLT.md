# SKLT: skeleton resource

*Point cloud + polygon list that an area can stretch itself onto; a form
whose children are `[[POO2]]` / `[[POL2]]` (+ optional `[[SEN2]]`).*
Stored as `[[EMRS]]` pairs (class `sklt.class`) inside `[[EMBD]]` —
resource names often look like `Skeleton/DUMMY.sklt`.

## Related format documents

- `[[POO2]]`, `[[POL2]]`, `[[SEN2]]` — the payload chunks.
- `[[SKLC]]` — how an `OBJT` links to a stored skeleton by name.
- `[[AREA]]`/`[[ADE]]` — consumers of points/polys (point id / poly id).
- `[[EMBD]]` — where they live.

## Layout

```
FORM ... SKLT
    POO2 <12 * num_points>    # points, see POO2.md; first chunk
    SEN2 <12 * num_sens>      # optional; see SEN2.md
    POL2 <4 + sum>            # polygons, see POL2.md; last chunk
```

An example dump from `SET1/OBJECTS/SET.BAS` on-disk
(`Skeleton/S00H.sklt`, 5 points / 5 polys):

```
    53 4b 4c 54                              SKLT
    50 4f 4f 32 00 00 00 78                  POO2...x      # 0x78 = 12 * 10
    43 e1 00 00 00 00 00 00 44 3b 80 00      C.....D;..
    43 16 00 00 00 00 00 00 44 3b 80 00      C.....D;..
    ...
    50 4f 4c 32 00 00 00 32                  POL2...2      # 0x32 = 50
    00 00 00 05                              ....          # poly count
    00 03 00 04 00 00 00 08                  ..            # poly 0: 3 verts
    00 04 00 01 00 00 00 04                  ..            # poly 1: 4 verts
    00 05 00 04 00 02 00 01                  ..
    00 05 00 06 00 04 00 03                  ..
    00 02 00 06 00 07 00 03                  ..
    00 03 00 07 00 09                        ...
```

## Engine reading

`src/sklt.cpp:305` onwards (`NC_STACK_sklt::rsrc_func64`): `TAG_NAME`,
`TAG_POO2`/`TAG_POOL` and `TAG_SEN2`/`TAG_SENS` and `TAG_POL2`/`TAG_POLY`. A
missing or empty `POL2` is legal — `BEEBOX.BAS` in SET46 has a skeleton
with `POO2` only ("points, no polygons").

After loading, each polygon's plane equation is recomputed
(`sklt_func64__sub0__sub0`, `sklt.cpp:214`) from the first three vertices —
this is why point order within a poly matters.

## Legacy notes

`POLY`/`POLY` (without the `2`) are the v1 forms; modern assets only carry
`POO2`/`POL2`/`SEN2`.
