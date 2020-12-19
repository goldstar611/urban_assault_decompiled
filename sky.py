import compile
import glob
import os


def decompile_sky():
    for sky in glob.glob("assets/sky/*.bas"):
        sky_dir = os.path.splitext(sky)[0]
        form = compile.Form().load_from_file(sky)

        form.get_single("EMBD").to_class().extract_resources(sky_dir)  # Extract images + skeletons
        form.get_single("EMBD").sub_chunks = [compile.Form("ROOT")]  # Drop resources since we already extracted them

        with open(os.path.join(sky_dir, "sky.json"), "w") as f:
            f.write(form.to_json())


def compile_sky():
    for sky in glob.glob("assets/sky/*/sky.json"):
        sky_dir = os.path.dirname(sky)
        print(sky_dir)

        sky_form = compile.Form().from_json_file(sky)
        embd = sky_form.get_single("EMBD").to_class()

        json_files = glob.glob(os.path.join(sky_dir, "*.sklt.json"))
        bmp_files = glob.glob(os.path.join(sky_dir, "*.*"))

        for bmp_file in bmp_files:
            print(bmp_file)
            vbmp = compile.Vbmp().load_image(bmp_file)
            embd.add_vbmp(vbmp.file_name, vbmp)
        for json_file in json_files:
            print(json_file)
            sklt = compile.Form().from_json_file(json_file)

            resource_name = "Skeleton/" + os.path.splitext(os.path.basename(json_file))[0]
            embd.add_sklt(resource_name, sklt)

        sky_name = os.path.basename(sky_dir) + ".bas"

        sky_form.save_to_file(os.path.join("output", sky_name))


if __name__ == '__main__':
    decompile_sky()
    compile_sky()
