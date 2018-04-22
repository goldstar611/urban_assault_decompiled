import os


def parse_set_descriptor(set_number=1):
    set = []
    with open(os.path.join("set%i" % set_number, "scripts", "set.sdf"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b" ")[0].decode("ascii")
            set.append(base)
    print("set:", set)
    return set


def parse_visproto(set_number=1):
    visproto = []
    with open(os.path.join("set%i" % set_number, "scripts", "visproto.lst"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            visproto.append(base)
    print("visproto:", visproto)
    return visproto


def parse_slurps(set_number=1):
    slurps = []
    with open(os.path.join("set%i" % set_number, "scripts", "slurps.lst"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            slurps.append(base)
    print("slurps:", slurps)
    return slurps


if __name__ == "__main__":
    parse_set_descriptor(1)
    parse_visproto(1)
    parse_slurps(1)
