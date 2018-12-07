import compile
import glob
import os
from PyQt5 import QtGui


def decompile_sky():
    for sky in glob.glob("sky/*.bas"):
        sky_dir = os.path.splitext(sky)[0]
        form = compile.Form().load_from_file(sky)

        embd = compile.Embd()
        embd.sub_chunks = form.get_single_form_by_type("EMBD").sub_chunks  # HACK

        embd.extract_resources(sky_dir)

        ades = form.get_single_form_by_type("ADES")
        if ades:
            with open(os.path.join(sky_dir, "ades.json"), "w") as f:
                f.write(ades.to_json())


def compile_sky():
    with open(os.path.join("sky", "sky_generic.json"), "rt") as f:
        generic_sky_json = f.read()

    for sky in glob.glob("sky/*"):
        print(sky)

        generic_sky = compile.Form().from_json(generic_sky_json)
        embd = generic_sky.get_single_form_by_type("EMBD").to_class()  # to_class() makes this a new object. Not part of generic_sky object anymore
        name = generic_sky.get_single_chunk_by_id("NAME").to_class()  # to_class() makes this a new object. Not part of generic_sky object anymore
        sky_dir = os.path.basename(sky)

        json_files = glob.glob(os.path.join(sky, "[!ades]*.json"))
        bmp_files = glob.glob(os.path.join(sky, "*.bmp"))
        ades_file = os.path.join(sky, "ades.json")

        for bmp_file in bmp_files:
            print(bmp_file)
            vbmp = compile.Vbmp().load_from_bmp(bmp_file)
            embd.add_vbmp(bmp_file, vbmp)
        for json_file in json_files:
            print(json_file)
            with open(json_file, "rt") as f:
                sklt = compile.Form().from_json(f.read())
            embd.add_sklt(json_file, sklt)
        if os.path.isfile(ades_file):
            print(ades_file)


if __name__ == '__main__':
    decompile_sky()
    compile_sky()
