# ADE / ADES: detail node and detail list

*`ade.class` (detail, e.g. points/polys of a `[[SKLT]]`) and its list
container. `[[AREA]]` is the textured-plane subclass that also derives from
this hierarchy.*

## Related format documents

- `[[STRC]]` — the 10-byte `STRC_ADE` flavor.
- `[[AREA]]` — subclass with the second 10-byte flavor and texture planes.
- `[[ADES]]` — list-of-`ADE` form (also the generic holder for the
  vehicle's mesh parts).
- `[[SKLT]]`/`[[POO2]]`/`[[POL2]]` — what `point`/`poly` indices hit.
- `[[NAME]]` — identity `ROOT/NAME` chunk in this form.

## ADE layout

```
FORM ... ADE
    ROOT                        # ROOT/NAME identity chunk
    STRC <10 bytes STRC_ADE>    # see STRC.md - point/poly indices
```

Engine: `src/ade.cpp:75` (`NC_STACK_ade::LoadingFromIFF`) parses the
`STRC`; bit 1 of `flags` = depth-fade, bit 2 = back-face check. There is
no `KIDS` here — an ADE is a leaf.

**Note**: even for `area.class` payloads, the surface settings
(`polFlags`, `clrVal`, `trcVal`, `shdVal`) are *not* in this form — the
plain `ADE` subform only carries the `STRC_ADE` point/poly bytes. The
AREA's own `STRC` chunk (sibling of the `ADE` subform inside the `AREA`
form) holds them; see `[[AREA]]`.

## ADES layout

```
FORM ... ADES
    OBJT [CLID ade.class|area.class, ...]   # one per detail part
    OBJT ...
```

`[[ADES]]` is just a list wrapper: no `STRC` of its own, no `CLID`. The
engine's `NC_STACK_base::ReadIFFTagADES` (`base.cpp:121`) iterates it and
loads each contained `OBJT` through the normal loader. In the vehicle
assets the `ADES` holds the (often ~8) area/ade parts that make up the
model's textured planes, wheels, and hull.

## Engine-defaults caveat

The engine does **not** store `fadeStart`/`fadeLength` for ADEs — do not
"clean up" a missing `STRC` in an existing `ADE`: a stripped `STRC` loses
`point`/`poly` indexing, not just transforms.
