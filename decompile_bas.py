import reorg
import glob
import os


def main():
    files = glob.glob("set*/**/*.bas", recursive=True)

    for file in []:
        print("file:", file)
        with open(file, "rb") as f:
            form = reorg.Form().load_from_file(file)
            with open(file + ".json", "w") as o:
                o.write(form.to_json())

    for file in glob.glob("sky/*.bas", recursive=True):
        # Extract EMBD Resources
        bas_file = reorg.Mc2().load_from_file(file)
        form = bas_file.get_single_form_by_type("EMBD")
        embd = reorg.Embd()
        embd.sub_chunks = form.sub_chunks
        embd.extract_resources(os.path.splitext(file)[0])


if __name__ == '__main__':
    main()
