# Extracts real golden form fixtures from the original game set files.
#
# Usage: python3 test/make_orig_fixtures.py "/path/to/OpenUA Standalone Package"
#
# Each set ships as a single compiled SET.BAS, so individual forms are carved
# out of the parsed SET1 / SET46 trees.  Any fixture already present on disk is
# left untouched, so re-running the tool never silently changes golden bytes;
# delete a fixture to refresh it (e.g. after a parser fix).
#
# Fixtures stay small by design: the resource-bearing EMBD forms embed ~2 MB of
# bitmaps, so the committed EMBD fixture is the resource-less SET46 copy.

import glob
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import compile  # noqa: E402

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", "orig")

# (fixture name, set folder, form_type)
PLAN = [
    ("ADE.bin", "SET1", "ADE "),
    ("ADES.bin", "SET1", "ADES"),
    ("AMSH.bin", "SET1", "AMSH"),
    ("AREA.bin", "SET1", "AREA"),
    ("AREA-textured.bin", "SET1", "AREA-visible"),
    ("BANI.bin", "SET1", "BANI"),
    ("CIBO.bin", "SET1", "CIBO"),
    ("EMBD.bin", "SET46", "EMBD"),
    ("PTCL.bin", "SET1", "PTCL"),
    ("SKLC.bin", "SET1", "SKLC"),
    ("SKLT.bin", "SET1", "SKLT"),
    ("VANM.bin", "SET1", "VANM"),
    ("VBMP.bin", "SET1", "VBMP"),
    ("MC2.bin", "SET46", "MC2 "),
]


def is_textured_area(form):
    """The first AREA in a set is often animated; prefer one with a bitmap."""
    bitmap_refs = form.get_direct_all("OBJT")
    return any(ref.get_direct_single("CIBO") for ref in bitmap_refs if isinstance(ref, compile.Form))


def carve_form(src, form_type):
    """Depth-first search of a parsed set, returning the first matching form."""
    predicate = is_textured_area if form_type.endswith("-visible") else None
    if predicate:
        form_type = form_type[:-len("-visible")]
    with open(src, "rb") as f:
        raw = f.read()
    root = compile.Form().parse_stream(io.BytesIO(raw))[0]
    stack = [root]
    while stack:
        node = stack.pop()
        if not isinstance(node, compile.Form):
            continue
        if node.form_type == form_type and (predicate is None or predicate(node)):
            return node
        stack.extend(reversed(node.sub_chunks))
    return None


def main(game_root):
    os.makedirs(FIXTURE_DIR, exist_ok=True)
    ok = True
    for name, set_name, form_type in PLAN:
        fixture = os.path.join(FIXTURE_DIR, name)
        if os.path.exists(fixture):
            print("keep  ", name)
            continue
        matches = glob.glob(os.path.join(game_root, "*", set_name, "OBJECTS", "SET.BAS"))
        if not matches:
            print("missing source set:", set_name)
            ok = False
            continue
        form = carve_form(matches[0], form_type)
        if form is None:
            print("no %r form in" % form_type, matches[0])
            ok = False
            continue
        data = form.full_data()
        with open(fixture, "wb") as f:
            f.write(data)
        print("wrote ", name, len(data), "bytes")
    return ok


if __name__ == "__main__":
    if not main(sys.argv[1]):
        sys.exit(1)
