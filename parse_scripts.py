import os


def parse_set_descriptor(set_number=1):
    with open(os.path.join("set%i" % set_number, "scripts", "set.sdf")) as f:
        pass


def parse_visproto(set_number=1):

    with open(os.path.join("set%i" % set_number, "scripts", "visproto.lst")) as f:
        pass


def parse_slurps(set_number=1):

    with open(os.path.join("set%i" % set_number, "scripts", "slurps.lst")) as f:
        pass


if __name__ == "__main__":
    parse_set_descriptor()
    parse_visproto()
    parse_slurps()
