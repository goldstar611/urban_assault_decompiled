import compile
import glob
import os
from PyQt5 import QtGui


def main():
    for sky in glob.glob("sky/*.bas"):
        sky_dir = os.path.splitext(sky)[0]
        form = compile.Form().load_from_file(sky)

        embd = compile.Embd()
        embd.sub_chunks = form.get_single_form_by_type("EMBD").sub_chunks  # HACK

        embd.extract_resources(sky_dir)


if __name__ == '__main__':
    main()
