import compile
import glob
import os


def main():
    files = glob.glob("set*/**/*.bas", recursive=True)
    for file in files:
        print("file:", file)
        with open(file, "rb") as f:
            form = compile.Form().load_from_file(file)
            with open(file + ".json", "w") as o:
                o.write(form.to_json())

    #
    files = glob.glob("set*/**/*.skl", recursive=True)
    for file in files:
        print("file:", file)
        with open(file, "rb") as f:
            form = compile.Form().load_from_file(file)
            with open(file + ".json", "w") as o:
                o.write(form.to_json())

    #
    files = glob.glob("set*/**/*.ANM", recursive=True)
    for file in files:
        print("file:", file)
        with open(file, "rb") as f:
            form = compile.Form().load_from_file(file)
            with open(file + ".json", "w") as o:
                o.write(form.to_json())

    #
    files = glob.glob("set*/*.ILB", recursive=True)
    for file in files:
        print("file:", file)
        vbmp = compile.Vbmp()
        vbmp.load_from_ilbm(file)
        vbmp.save_to_bmp(file + ".bmp")

    #
    for file in glob.glob("sky/*.bas", recursive=True):
        # Extract EMBD Resources
        bas_file = compile.Mc2().load_from_file(file)
        form = bas_file.get_single("EMBD")
        embd = compile.Embd()
        embd.sub_chunks = form.sub_chunks
        embd.extract_resources(os.path.splitext(file)[0])


if __name__ == '__main__':
    main()
