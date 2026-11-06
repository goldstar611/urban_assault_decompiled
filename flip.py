#!/usr/bin/python3

import glob

from PIL import Image

mirror_horizontal = False
mirror_vertical = False

for file in glob.glob("*.bmp"):
    with Image.open(file) as image:
        if mirror_horizontal:
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if mirror_vertical:
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        image.save(file.replace(".ILB", "").replace(".bmp", ".png"))
