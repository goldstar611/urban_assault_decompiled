import compile
import os
from PyQt5 import QtGui, QtCore


file_name = os.path.join("assets","sky", "haamitt1",  "sky.json")
sky_file = compile.Mc2().from_json_file(file_name)
image_dir = os.path.dirname(file_name)

cibo_forms = sky_file.get_all("CIBO")

for i, cibo_form in enumerate(cibo_forms):
    image_filename = cibo_form.get_single("NAM2").to_class().name
    otl2_points = cibo_form.get_single("OTL2").to_class().points
    print(image_filename, otl2_points)

    image = QtGui.QImage(os.path.join(image_dir, image_filename + ".bmp"))
    if image.format() == QtGui.QImage.Format_Invalid:
        raise ValueError("image format was invalid!")
    image = image.convertToFormat(QtGui.QImage.Format_RGB32)
    painter = QtGui.QPainter(image)
    pen = QtGui.QPen()
    pen.setWidth(1)
    pen.setColor(QtGui.QColor(255, 0, 0))
    painter.setPen(pen)
    painter.drawPolygon(*[QtCore.QPoint(x[0], x[1]) for x in otl2_points])
    painter.end()

    image.save(os.path.join("output", image_filename + "{}.bmp".format(i)))
