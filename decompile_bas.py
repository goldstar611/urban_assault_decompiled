import compile
import glob


def main():
    files = glob.glob("set*/**/*.bas", recursive=True)

    for file in files:
        print("file:", file)
        with open(file, "rb") as f:
            form = compile.Form().load_from_file(file)
            with open(file + ".json", "w") as o:
                o.write(form.to_json())

        # Extract EMBD Resources
        bas_file = compile.Mc2().load_from_file(file)
        form = bas_file.get_single_form_by_type("EMBD")
        embd = compile.Embd()
        embd.sub_chunks = form.sub_chunks
        embd.extract_resources("output/dontcare")


if __name__ == '__main__':
    main()
