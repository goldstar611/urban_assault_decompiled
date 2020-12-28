#!/usr/bin/python3

import glob

from PyQt5 import QtGui

for file in glob.glob("*.bmp"):
    image = QtGui.QImage(file)
    mirror_horizontal = False
    mirror_vertical = False
    image = image.mirrored(mirror_horizontal, mirror_vertical)
    image.save(file.replace(".ILB", "").replace(".bmp", ".png"))

