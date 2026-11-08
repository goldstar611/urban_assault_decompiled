import io
import os

import compile
import hashlib
import json


def decompile_set_bas(set_bas_path: str,
                      assets_dir: str) -> None:
    """Decompile one original game ``SET.BAS`` file into *assets_dir*.

    Extracts the EMBD resources (VBMP bitmaps, SKLT skeletons, VANM
    animations) and writes a manifest ``resource_order.json`` that records
    the source file's sha256 (for provenance) and the *exact original
    resource order and EMRS names*; ``compile.build_set()`` replays the
    manifest to stay byte-identical with the original game file. The
    original files mix upper and lower case versions of the same resource
    prefix (e.g. ``Skeleton/`` and ``skeleton/``), so the manifest must
    store exact names - sorting or normalizing them breaks the byte layout.
    """
    with open(set_bas_path, "rb") as f:
        set_bas_bytes = f.read()
        mc2 = compile.Form().parse_stream(io.BytesIO(set_bas_bytes))[0]
        set_bas_sha256 = hashlib.sha256(set_bas_bytes).hexdigest()
    embd = mc2.get_single("EMBD")
    if embd is None:
        raise ValueError("No EMBD form found in %s" % set_bas_path)
    elif not isinstance(embd, compile.Embd):
        # A generic Form was parsed; rebuild the EMRS/resource pairing
        # manually (Root first, then EMRS + resource pairs).
        resources = []
        sub_chunks = embd.sub_chunks[1:]
        for i in range(0, len(sub_chunks), 2):
            emrs = sub_chunks[i]
            resource = sub_chunks[i + 1]
            resources.append((emrs.emrs_name, resource))
    else:
        resources = list(embd.emrs_resources.items())
    if not resources:
        raise ValueError("No EMBD resources found in %s" % set_bas)

    base_dir = assets_dir
    manifest_resources = []
    import glob
    for emrs, resource in resources:
        if resource.form_type == "VBMP":
            # Reuse an already-extracted bitmap file if one exists; asset
            # dirs differ in naming (".ILBM.bmp" vs ".ILB.bmp"), and the
            # assets are what they are.
            existing = glob.glob(os.path.join(base_dir, emrs + "*.bmp"))
            files_rel = os.path.basename(existing[0]) if existing else emrs + ".bmp"
        elif resource.form_type == "SKLT":
            stem = emrs[:-len(".sklt")] + ".skl.json"
            if "/" in emrs:
                files_rel = stem
            else:
                files_rel = "Skeleton/" + stem
        elif resource.form_type == "VANM":
            files_rel = "rsrcpool/" + emrs + ".json"
        else:
            raise ValueError("Unimplemented resource type: %s" % resource.form_type)

        files_dir = os.path.dirname(files_rel)
        if files_dir:
            directory = os.path.join(base_dir, files_dir)
            if not os.path.isdir(directory):
                os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(base_dir, files_rel)
        if resource.form_type == "VBMP":
            resource.save_to_bmp(file_path)
        else:
            with open(file_path, "w") as f:
                f.write(resource.to_json())

        manifest_resources.append([emrs, resource.form_type, files_rel])
        print("extracted:", emrs, "->", files_rel)

    manifest_path = os.path.join(base_dir, "resource_order.json")
    manifest = {
        "source": set_bas_path,
        "source_sha256": set_bas_sha256,
        "resources": manifest_resources,
    }
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print("manifest written:", manifest_path, len(manifest_resources),
          "entries, source sha256:", set_bas_sha256)


def main() -> None:
    import sys
    if len(sys.argv) != 3:
        print("usage: decompile_set_bas.py <SET.BAS path> <assets_dir>")
        raise SystemExit(1)
    decompile_set_bas(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
