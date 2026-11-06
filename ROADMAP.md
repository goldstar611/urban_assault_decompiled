# Roadmap

## Form validation

## Remove conversion shims

- Replace remaining `.to_class()` calls in `3ds.py`, `sky.py`, and the Blender import/export modules with the concrete objects returned by parsing.
- Deprecate, then remove, `Chunk.to_class()` and `Form.to_class()` once all call sites have migrated.

## Test coverage

- Add binary round-trip tests using real asset fixtures for each specialized form, in addition to the current minimal constructed-form tests.
