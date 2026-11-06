# Roadmap

## Form validation

- Add `validate()` methods to `Ade`, `Cibo`, `Vanm`, and `Area`.
- Report precise structural errors for missing or invalid direct children, such as:
  - `AREA`: missing direct `ADE ` form.
  - `AREA/ADE `: missing direct `STRC` chunk.
  - Textured `AREA`: missing `OBJT/CIBO/NAM2` bitmap reference.

## Remove conversion shims

- Replace remaining `.to_class()` calls in `3ds.py`, `sky.py`, and the Blender import/export modules with the concrete objects returned by parsing.
- Deprecate, then remove, `Chunk.to_class()` and `Form.to_class()` once all call sites have migrated.

## Test coverage

- Add binary round-trip tests using real asset fixtures for each specialized form, in addition to the current minimal constructed-form tests.
