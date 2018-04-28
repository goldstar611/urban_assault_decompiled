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


if __name__ == '__main__':
    main()
