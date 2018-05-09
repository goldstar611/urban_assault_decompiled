import compile
import os
from PyQt5 import QtGui, QtCore


sky_file = compile.Mc2().load_from_file(os.path.join("sky", "haamitt1.bas"))
print(sky_file.to_json())
image_dir = os.path.join("sky", "haamitt1")

cibo_forms = sky_file.get_all_form_by_type("CIBO")

for cibo_form in cibo_forms:
    image_filename = cibo_form.get_single_chunk_by_id("NAM2").conversion_class.name
    otl2_points = cibo_form.get_single_chunk_by_id("OTL2").conversion_class.points
    print(image_filename, otl2_points)

    image = QtGui.QImage(os.path.join(image_dir, image_filename + ".bmp"))
    image = image.convertToFormat(QtGui.QImage.Format_RGB32)
    painter = QtGui.QPainter(image)
    pen = QtGui.QPen()
    pen.setWidth(1)
    pen.setColor(QtGui.QColor(255, 0, 0))
    painter.setPen(pen)
    painter.drawPolygon(*[QtCore.QPoint(x[0], x[1]) for x in otl2_points])
    painter.end()

    image.save(os.path.join(image_dir, image_filename + ".bmp"))