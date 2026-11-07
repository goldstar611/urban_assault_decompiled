import compile
import json
import os


SET_BAS_PATH = os.path.join("/Users/af/Downloads/OpenUA Standalone Package", "DATA")


def decompile_set_bas(game_root: str = SET_BAS_PATH,
                      set_number: str = "1",
                      assets_dir: str = "assets/sets/set{}") -> None:
    """Decompile the original game ``SET.BAS`` for one set.

    Extracts the EMBD resources (VBMP bitmaps, SKLT skeletons, VANM
    animations) into the asset folders and writes a per-set manifest
    ``resource_order.json`` that records the *exact original resource order
    and EMRS names*, which ``compile.build_set()`` replays to stay
    byte-identical with the original game file. The original files mix upper
    and lower case versions of the same resource prefix (e.g. ``Skeleton/`` and
    ``skeleton/``), so the manifest must store exact names - sorting or
    normalizing them breaks the byte layout.
    """
    set_bas = os.path.join(game_root, "SET" + set_number, "OBJECTS", "SET.BAS")
    with open(set_bas, "rb") as f:
        mc2 = compile.Form().parse_stream(f)[0]
    embd = mc2.get_single("EMBD")
    if embd is None:
        raise ValueError("No EMBD form found in %s" % set_bas)
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

    base_dir = assets_dir.format(set_number)
    manifest_resources = []
    for emrs, resource in resources:
        if resource.form_type == "VBMP":
            files_rel = emrs + ".bmp"
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
    with open(manifest_path, "w") as f:
        json.dump(manifest_resources, f, indent=2)
    print("manifest written:", manifest_path, len(manifest_resources), "entries")


def main() -> None:
    decompile_set_bas()


if __name__ == '__main__':
    main()
