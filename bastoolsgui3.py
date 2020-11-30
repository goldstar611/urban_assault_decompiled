#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 20:24:06 2014

@author: GoldStar611, Ormu
"""
import compile
import myjson
import numpy
import os
import struct
import sys

from PyQt5 import QtGui, QtCore, uic, QtWidgets, QtOpenGL
from typing import Union

try:
    from OpenGL import GL
except ImportError:
    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    QtWidgets.QMessageBox.critical(None, "OpenGL Example", "PyOpenGL must be installed to run this example.")
    sys.exit(1)


########################################################################################################################
# MyQTreeWidgetItem.py


class MyQTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, *args, **kwargs):
        super(MyQTreeWidgetItem, self).__init__(*args, **kwargs)
        self.association = None  # type: Union[None,compile.Form,compile.Chunk]
        self.icons = {}
        
    def child(self, p_int):
        """

        :rtype: MyQTreeWidgetItem
        """
        return super(MyQTreeWidgetItem, self).child(p_int)

    def parent(self):
        """

        :rtype: MyQTreeWidgetItem
        """
        return super(MyQTreeWidgetItem, self).parent()

    def associate(self, form_or_chunk):
        self.association = form_or_chunk
        self.update_icon()

    def update_icon(self):
        if self.is_form():
            if self.form_type() == "SKLT":
                self.setIcon(0, self.icons.get("SKLT"))
            else:
                self.setIcon(0, self.icons.get("FORM"))
            #self.setIcon(0, self.icons.get("FILE"))

    def is_form(self):
        return isinstance(self.association, compile.Form)

    def get_form(self):
        """

        :rtype: Form
        """
        if self.is_form():
            return self.association

    def form_type(self):
        """

        :rtype: str
        """
        if self.is_form():
            return self.association.form_type

    def is_chunk(self):
        return isinstance(self.association, compile.Chunk)

    def get_chunk(self):
        """

        :rtype: Chunk
        """
        if self.is_chunk():
            return self.association

    def chunk_id(self):
        """

        :rtype: str
        """
        if self.is_chunk():
            return self.association.chunk_id

    def save_to_file(self, file_name: str):
        self.association.save_to_file(file_name)

    def save_data_to_file(self, file_name: str):
        if self.is_chunk():
            self.association.save_data_to_file(file_name)

    def load_from_file(self, file_name: str):
        pass  # TODO Need to know parent object

    def load_data_from_file(self, file_name: str):
        if self.is_chunk():
            self.association.load_data_from_file(file_name)

    def can_render_bitmap(self):
        if self.is_form():
            if self.association.form_type in ["VBMP"]:
                return True
        return False

    def can_render_3d(self):
        if self.is_form():
            if self.association.form_type in ["SKLT", "AMSH"]:
                return True
        return False

    def is_editable(self):
        if self.is_chunk():
            return True
        return False

    def get_data(self):
        """

        :rtype: bytes
        """
        return self.association.get_data()

    def full_data(self):
        """

        :rtype: bytes
        """
        return self.association.full_data()

    def to_json(self):
        if self.is_chunk() and self.is_editable():
            return self.get_chunk().to_json()

    def from_json(self, json_string):
        if self.is_chunk() and self.is_editable():
            a = self.get_chunk().from_json(json_string)
            b = a
            self.setText(0, str(self.get_chunk().chunk_id))

########################################################################################################################
# GlobalConstants.py


unsigned_int_be = "<I"
size_of_unsigned_int = 4
unsigned_short_be = "<H"
size_of_unsigned_short = 2
QtUserRole = QtCore.Qt.UserRole

########################################################################################################################
# MyQGLWidget.py


class Mesh(object):
    def __init__(self):
        self.image = QtGui.QImage("preview.bmp")
        self.texture = (
            (0, ((1, 119), (131, 119), (131, 196), (1, 196))),
            (2, ((1, 254), (1, 210), (131, 210), (131, 254))),
            (3, ((1, 120), (60, 120), (60, 196), (1, 196))),
            (4, ((60, 120), (131, 120), (131, 196), (60, 196))),
            (5, ((2, 117), (2, 62), (90, 62), (90, 117))),
            (6, ((2, 63), (2, 21), (90, 21), (90, 63))),
            (7, ((1, 254), (1, 210), (131, 210), (131, 254))),
            (8, ((20, 127), (39, 134), (39, 182))),
            (9, ((39, 182), (20, 187), (20, 127))),
            (10, ((111, 187), (92, 182), (111, 127))),
            (11, ((92, 182), (92, 134), (111, 127)))
        )
        self.edges = (
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (4, 8, 9, 5),
            (5, 9, 10, 6),
            (9, 2, 1, 10),
            (7, 11, 8, 4),
            (11, 0, 3, 8),
            (6, 10, 11, 7),
            (8, 3, 2),
            (2, 9, 8),
            (10, 1, 11),
            (1, 0, 11)
        )
        self.vertices = (
            (7.0, -10.0, 14.0),
            (10.0, -2.0, -15.0),
            (-10.0, -2.0, -15.0),
            (-7.0, -10.0, 14.0),
            (-9.0, 10.0, 13.0),
            (-9.0, 10.0, -15.0),
            (9.0, 10.0, -15.0),
            (9.0, 10.0, 13.0),
            (-12.0, -3.0, 18.0),
            (-12.0, 1.0, -18.0),
            (12.0, 1.0, -18.0),
            (12.0, -3.0, 18.0)
        )

    def load_ilbm_from_embd(self, embd_form, ilbm_name, width=256, height=256, mirror_horizontal=False, mirror_vertical=True):
        for i, chunk in enumerate(embd_form.sub_chunks):
            if bytes(ilbm_name, "ascii") in chunk.get_data():
                print("Found ", ilbm_name, "in embd")
                data = embd_form.sub_chunks[i + 1].full_data()[34:]

                image = QtGui.QImage(data, width, height, QtGui.QImage.Format_Indexed8)
                image = image.mirrored(mirror_horizontal, mirror_vertical)
                # color_table = [QtGui.qRgb(i, i, i) for i in range(256)]
                image.setColorTable(compile.color_table)
                self.image = image
                return image

    def load_ilbm_by_name(self, ilbm_name, width=256, height=256, mirror_horizontal=False, mirror_vertical=True):
        """

        :rtype: QtGui.QImage
        """
        # file_begin = 0
        file_current = 1
        # file_end = 2
        file_path = os.path.join("set", ilbm_name)

        if not os.path.isfile(file_path):
            print("Couldn't find %s" % file_path)

        f = open(file_path, "rb")
        f.seek(34, file_current)
        data = f.read()
        f.close()

        image = QtGui.QImage(data, width, height, QtGui.QImage.Format_Indexed8)
        image = image.mirrored(mirror_horizontal, mirror_vertical)
        # color_table = [QtGui.qRgb(i, i, i) for i in range(256)]
        image.setColorTable(compile.color_table)
        self.image = image

        return image

    def load_sklt_from_embd(self, embd_form, sklt_name):
        for i, chunk in enumerate(embd_form.sub_chunks):
            if bytes(sklt_name, "ascii") in chunk.get_data():
                print("Found ", sklt_name, "in embd")
                sklt = embd_form.sub_chunks[i + 1]
                sklt_poo2_data = sklt.get_single_chunk_by_id("POO2").get_data()
                poo2 = compile.Poo2()
                poo2.set_binary_data(sklt_poo2_data)
                vertices = poo2.points_as_list()
                self.vertices = vertices

                sklt_pol2_data = sklt.get_single_chunk_by_id("POL2").get_data()
                pol2 = compile.Pol2()
                pol2.set_binary_data(sklt_pol2_data)
                edges = pol2.edges
                self.edges = edges

                return vertices, edges

    def load_sklt_by_name(self, sklt_name):
        file_path = os.path.join("set", sklt_name)

        if not os.path.isfile(file_path):
            print("Couldn't find %s" % file_path)

        sklt = compile.Form().load_from_file(file_path)

        sklt_poo2_data = sklt.get_single_chunk_by_id("POO2").get_data()
        poo2 = compile.Poo2()
        poo2.set_binary_data(sklt_poo2_data)
        vertices = poo2.points_as_list()
        self.vertices = vertices

        sklt_pol2_data = sklt.get_single_chunk_by_id("POL2").get_data()
        pol2 = compile.Pol2()
        pol2.set_binary_data(sklt_pol2_data)
        edges = pol2.edges
        self.edges = edges

        return vertices, edges


class GLWidget(QtOpenGL.QGLWidget):
    x_rotation_changed = QtCore.pyqtSignal(int)
    y_rotation_changed = QtCore.pyqtSignal(int)
    z_rotation_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.x_rotation = 0
        self.y_rotation = 0
        self.z_rotation = 0

        self.camera_position = {"x": 0.0,
                                "y": 0.2,
                                "z": -10.0}

        self.last_position = QtCore.QPoint()

        self.meshes = [Mesh()]

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def set_x_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.x_rotation:
            self.x_rotation = angle
            self.x_rotation_changed.emit(angle)
            self.updateGL()

    def set_y_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.y_rotation:
            self.y_rotation = angle
            self.y_rotation_changed.emit(angle)
            self.updateGL()

    def set_z_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.z_rotation:
            self.z_rotation = angle
            self.z_rotation_changed.emit(angle)
            self.updateGL()

    def clear(self):
        self.meshes = []

    def draw_simpl(self, draw_texture=True):
        for mesh in self.meshes:
            GL.glPushMatrix()

            if draw_texture and mesh.texture and mesh.image:
                texture = QtGui.QOpenGLTexture(mesh.image.mirrored())
                texture.setMinificationFilter(QtGui.QOpenGLTexture.LinearMipMapLinear)
                texture.setMagnificationFilter(QtGui.QOpenGLTexture.Linear)
                texture.bind()

                GL.glEnable(GL.GL_TEXTURE_2D)
                gl_mode = GL.GL_POLYGON

                # Using GL_REPLACE will prevent any other vertex colors from interfering with texture colors
                GL.glTexEnvi(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_REPLACE)
            elif mesh.edges:
                GL.glColor3f(1.0, 0.0, 1.0)
                GL.glLineWidth(1.5)
                gl_mode = GL.GL_LINE_LOOP
            else:
                GL.glColor3f(1.0, 0.0, 1.0)
                GL.glPointSize(10)
                gl_mode = GL.GL_POINTS

            # Apply scaling factor so it fits inside GLWidget
            scale_factor = numpy.amax([numpy.linalg.norm(x) for x in mesh.vertices]) * 2
            GL.glScalef(1.0 / scale_factor, 1.0 / scale_factor, 1.0 / scale_factor)

            if not draw_texture or not mesh.texture:
                for edge in mesh.edges:
                    GL.glBegin(gl_mode)
                    for vertex in edge:
                        GL.glVertex3fv(mesh.vertices[vertex])
                    GL.glEnd()

            else:
                for i, tex in mesh.texture:
                    GL.glBegin(gl_mode)

                    for j, (x, y) in enumerate(tex):
                        GL.glTexCoord2f(x / 255.0, y / 255.0)
                        GL.glVertex3fv(mesh.vertices[mesh.edges[i][j]])

                    GL.glEnd()

            if draw_texture and mesh.texture:
                GL.glDisable(GL.GL_TEXTURE_2D)
            GL.glPopMatrix()

    def initializeGL(self):
        # noinspection PyCallByClass, PyTypeChecker
        self.qglClearColor(QtGui.QColor.fromRgb(0, 0, 0))
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(self.camera_position["x"], self.camera_position["y"], self.camera_position["z"])
        GL.glRotated(self.x_rotation / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.y_rotation / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.z_rotation / 16.0, 0.0, 0.0, 1.0)
        # GL.glCallList(self.object))
        self.draw_simpl()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        GL.glViewport(int((width - side) / 2), int((height - side) / 2), int(side), int(side))
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-0.5, +0.5, +0.5, -0.5, 1.0, 20.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.last_position = event.pos()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.camera_position["x"] -= 0.01
        if event.key() == QtCore.Qt.Key_D:
            self.camera_position["x"] += 0.01
        if event.key() == QtCore.Qt.Key_W:
            self.camera_position["y"] -= 0.01
        if event.key() == QtCore.Qt.Key_S:
            self.camera_position["y"] += 0.01
        if event.key() == QtCore.Qt.Key_Space:
            self.camera_position["x"] = 0.0
            self.camera_position["y"] = 0.0
            self.x_rotation = 0
            self.y_rotation = 0
            self.z_rotation = 0
        if event.key() == QtCore.Qt.Key_Q:
            self.grabFrameBuffer().save("opengl.bmp")
        self.glDraw()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.last_position.x()
        dy = event.y() - self.last_position.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.set_x_rotation(self.x_rotation + 8 * -dy)
            self.set_y_rotation(self.y_rotation + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.set_x_rotation(self.x_rotation + 8 * -dy)
            self.set_z_rotation(self.z_rotation + 8 * dx)

        self.last_position = event.pos()

    @staticmethod
    def normalize_angle(angle):
        """

        :rtype: float
        """
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle


########################################################################################################################
# bastoolsgui3.py


class Example(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        uic.loadUi(self.resource_path('QMainWin.ui'), self)
        self.init_ui()

        self.file_changed = False
        self.top_level_form = compile.Form()
        self.search_term = ""
        self.default_windows_title = self.windowTitle()
        self.setWindowTitle(self.default_windows_title)

        self.icons = {"default": QtGui.QIcon(),
                      "FORM": QtGui.QIcon(self.resource_path("1452464202_folder_empty.png")),
                      "FILE": QtGui.QIcon(self.resource_path("1452462960_file.png")),
                      "SKLT": QtGui.QIcon(self.resource_path("1452464741_shoppingcart.png")),
                      }

        self.GLWidget = GLWidget()
        self.GLWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.splitter2.addWidget(self.GLWidget)

        # self.GLWidget.load_ilbm_by_name("BAGGER.ILB")
        # self.GLWidget.load_sklt_by_name("Skeleton/VPWSIMPL.skl")

    def dragEnterEvent(self, event):
        # Accept drag events
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if len(urls) == 1:
            file_name = str(urls[0].toLocalFile())
            self.top_level_form.load_from_file(file_name)
            self.refresh_tree_widget()
            self.file_changed = False
            self.setWindowTitle(self.default_windows_title + " " + file_name)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, "gui", relative_path)

    def closeEvent(self, event):
        if not self.file_changed:
            event.accept()
            return
        # noinspection PyArgumentList, PyCallByClass
        result = QtWidgets.QMessageBox.question(self,
                                                "Unsaved Changes!",
                                                "Exit without saving changes?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def init_ui(self):
        self.show()

        print("connecting signals to slots")
        self.treeWidget.itemSelectionChanged.connect(self.selection_changed)
        self.pushButton_2.clicked.connect(self.update_modifications)
        self.actionUpdate_Modifications.triggered.connect(self.update_modifications)
        self.actionOpen_BAS.triggered.connect(self.open_bas)
        self.actionSave_to_BAS.triggered.connect(self.save_to_bas)
        self.actionQuit.triggered.connect(self.close)
        self.actionDelete_Chunk.triggered.connect(self.delete_selected)
        self.actionInsert_Chunk_Below.triggered.connect(self.insert_chunk_below)
        self.actionRefresh_Tree_Widget.triggered.connect(self.refresh_tree_widget)
        self.actionConvert_to_FORM.triggered.connect(self.convert_to_form)
        self.actionExport_Data_to_File.triggered.connect(self.export_data_to_file)
        self.actionImport_Data_from_File.triggered.connect(self.import_data_from_file)
        self.actionRename.triggered.connect(self.rename_selected)
        self.actionExport_FORM_Chunk.triggered.connect(self.export_form_chunk)
        self.actionSearch.triggered.connect(self.search)
        self.actionSearch_Next.triggered.connect(self.search_next)
        self.actionConvert_to_Chunk.triggered.connect(self.convert_to_chunk)
        self.actionReplace_FORM.triggered.connect(self.replace_form)
        self.actionGoto.triggered.connect(self.goto)
        self.actionExtract_All_EMRS.triggered.connect(self.extract_all_emrs)
        self.actionExtract_Buildings.triggered.connect(self.extract_all_vehicles)
        self.actionExtract_Vehicles.triggered.connect(self.extract_all_buildings)
        self.actionExtract_Ground.triggered.connect(self.extract_all_ground)
        self.actionReplace_VBMPData.triggered.connect(self.replace_vbmp_data)

        # TODO actions:
        self.actionInsert_Chunk_Above.triggered.connect(self.not_implemented)
        self.actionEdit_Chunk_Properties.triggered.connect(self.not_implemented)
        self.actionMove_Up.triggered.connect(self.not_implemented)
        self.actionMove_Down.triggered.connect(self.not_implemented)
        self.actionCopy.triggered.connect(self.not_implemented)
        self.actionPaste.triggered.connect(self.not_implemented)

        print("all signals connected")
        self.update_status("Use [Ctrl]+[O] to open .BAS file.")

    def not_implemented(self):
        self.update_status("Sorry, this function not implemented :\\")

    ##############################################################################
    #   Experimental
    ##############################################################################

    @staticmethod
    def get_ready_for_extraction():

        check_dirs = ["/set",
                      "/set/rsrcpool",
                      "/set/Skeleton",
                      "/set/objects/vehicles",
                      "/set/objects/buildings",
                      "/set/objects/ground"]
        for dirs in check_dirs:
            if not os.path.exists(os.getcwd() + dirs):
                os.makedirs(os.getcwd() + dirs)

    ########################
    #   Extract all EMRS   #
    ########################

    def extract_all_emrs(self):
        self.get_ready_for_extraction()
        self.goto("MC2 /OBJT 0/BASE/OBJT 1/EMBD")

        level = 0
        current_item = self.current_item()
        for i in range(level, current_item.childCount()):
            if current_item.child(i).chunk_id() == "EMRS":
                emrs_class, filename, _, __ = bytes(current_item.child(i).get_data()).decode("ascii").split("\0")

                if "bmpanim.class" in emrs_class.lower():
                    filename = "rsrcpool/" + filename

                if "sklt.class" in emrs_class.lower():
                    filename = "Skeleton/" + filename.split("/")[1]

                if "." in filename:
                    filename = filename.split(".")[0] + "." + filename.split(".")[1][:3]

                print("found EMRS: " + filename)

                i = i + 1

                current_item.child(i).save_to_file(os.getcwd() + "/set/" + filename)

        self.update_status("Extracted all EMRS to  directory")

    ############################
    #   Extract all vehicles   #
    ############################

    def extract_all_vehicles(self):
        self.get_ready_for_extraction()
        self.goto("MC2 /OBJT 0/BASE/KIDS/OBJT 0/BASE/KIDS")

        level = 0
        current_item = self.current_item()
        for i in range(level, current_item.childCount()):
            filename = bytes(current_item.child(i).child(1).child(0).child(0).get_data()).decode()
            print("found vehicle: " + filename)

            selected_bas_chunk = current_item.child(i).get_form()

            new_mc2_form = compile.Form("MC2 ", sub_chunks=[selected_bas_chunk])
            new_mc2_form.save_to_file(os.getcwd() + "/set/objects/vehicles/" + filename + ".bas")

        self.update_status("Extracted all vehicles to  directory")

    ############################
    #   Extract all buildings  #
    ############################

    def extract_all_buildings(self):
        self.get_ready_for_extraction()
        self.goto("MC2 /OBJT 0/BASE/KIDS/OBJT 1/BASE/KIDS")

        level = 0
        current_item = self.current_item()
        for i in range(level, current_item.childCount()):
            filename = bytes(current_item.child(i).child(1).child(0).child(0).get_data()).decode()
            print("found building: " + filename)

            selected_bas_chunk = current_item.child(i).get_form()

            new_mc2_form = compile.Form("MC2 ", sub_chunks=[selected_bas_chunk])
            new_mc2_form.save_to_file(os.getcwd() + "/set/objects/buildings/" + filename + ".bas")

        self.update_status("Extracted all buildings to  directory")

    ############################
    #     Extract all ground   #
    ############################

    def extract_all_ground(self):
        self.get_ready_for_extraction()
        self.goto("MC2 /OBJT 0/BASE/KIDS/OBJT 2/BASE/KIDS")

        level = 0
        current_item = self.current_item()
        for i in range(level, current_item.childCount()):
            filename = bytes(current_item.child(i).child(1).child(0).child(0).get_data()).decode()
            print("found ground: " + filename)

            selected_bas_chunk = current_item.child(i).get_form()

            new_mc2_form = compile.Form("MC2 ", sub_chunks=[selected_bas_chunk])
            new_mc2_form.save_to_file(os.getcwd() + "/set/objects/ground/" + filename + ".bas")

        self.update_status("Extracted all ground to  directory")

    ##############################################################################
    # END Experimental
    ##############################################################################

    def current_item(self):
        """

        :rtype: MyQTreeWidgetItem
        """
        return self.treeWidget.currentItem()

    def current_item_parent(self):
        """

        :rtype: MyQTreeWidgetItem
        """
        if self.current_item():
            return self.current_item().parent()

    @staticmethod
    def object_from_tree_widget_item(tree_widget_item):
        """

        :rtype: Union[Form,Chunk]
        """
        return tree_widget_item.association

    def current_item_index(self):
        if self.current_item_parent():
            return self.current_item_parent().indexOfChild(self.current_item())

    def goto(self, destination=None):
        # TODO Requires MyQTreeWidgetItem to have .goto() method

        if not destination:
            # noinspection PyArgumentList,PyCallByClass
            destination, ok = QtWidgets.QInputDialog.getText(self,
                                                             "Enter a new search term",
                                                             "Where do you want to go??")
        if not destination:
            return
        destination = destination.split("/")[1:]
        current_item = self.treeWidget.topLevelItem(0)

        for dest in destination:
            for i in range(0, current_item.childCount()):
                child = current_item.child(i)

                if child.chunk_id() == dest or child.form_type() == dest or child.text(0) == dest:
                    self.treeWidget.setCurrentItem(child)
                    current_item = child
                    break

    def search_next(self):
        if self.search_term == "":
            self.search()
        else:
            if not self.current_item_parent():
                current_item = self.treeWidget.topLevelItem(0)
                search_selected = True
                search_parents = False
            else:
                current_item = self.current_item()
                search_selected = False
                search_parents = True

            if current_item:
                temp = self.search_tree_widget_item(current_item, self.search_term, 0, search_selected, search_parents)
                if temp:
                    self.treeWidget.setCurrentItem(temp)
            else:
                self.update_status(self.search_term + " was not found")

            return

    def search(self):
        # TODO Requires MyQTreeWidgetItem to have .search() method
        # noinspection PyArgumentList,PyCallByClass
        self.search_term, ok = QtWidgets.QInputDialog.getText(self,
                                                              "Enter a new search term",
                                                              "What form_type of ChunkID do you want to search for?")
        if self.search_term == "":
            return
        self.search_next()

    def search_tree_widget_item(self,
                                tree_widget_item: MyQTreeWidgetItem,
                                search_term: str,
                                level=0,
                                search_selected=False,
                                search_parents=False):
        """

        :rtype: QTreeWidgetItem
        """
        # noinspection PyArgumentList
        QtCore.QCoreApplication.processEvents()
        if tree_widget_item.is_form():
            print("form_type: ", tree_widget_item.form_type())
        else:
            print("id: ", tree_widget_item.chunk_id())

        if search_selected:
            if tree_widget_item.is_chunk() and search_term in tree_widget_item.chunk_id():
                return tree_widget_item
            if tree_widget_item.is_form() and search_term in tree_widget_item.form_type():
                return tree_widget_item
            if search_term in tree_widget_item.text(0):
                return tree_widget_item

        if tree_widget_item.is_form():
            for i in range(level, tree_widget_item.childCount()):
                temp_tree_widget_item = self.search_tree_widget_item(tree_widget_item.child(i), search_term, 0, True,
                                                                     False)
                if temp_tree_widget_item:
                    return temp_tree_widget_item

        if search_parents:
            if tree_widget_item.parent():
                print("searching parent of ", tree_widget_item.text(0))
                my_index = tree_widget_item.parent().indexOfChild(tree_widget_item)
                parent_num_children = tree_widget_item.parent().childCount()
                print("myIndex", my_index)
                print("parentNumChildren", parent_num_children)
                if my_index < parent_num_children - 1:
                    next_level = my_index + 1
                else:  # search parent, but not children
                    next_level = parent_num_children
                temp_tree_widget_item = self.search_tree_widget_item(tree_widget_item.parent(), search_term, next_level,
                                                                     False, True)
                if temp_tree_widget_item:
                    return temp_tree_widget_item

        return False

    def rename_selected(self):
        # TODO Requires MyQTreeWidgetItem to have .rename() method
        # TODO Requires Chunk() to have .rename() method
        # TODO Requires Form() to have .rename method
        current_item_index = self.current_item_index()

        new_name = self.current_item().text(0)
        # noinspection PyArgumentList,PyCallByClass
        new_name, _ = QtWidgets.QInputDialog.getText(self, "Enter new chunk name",
                                                     "Please enter a new name for the selected chunk",
                                                     QtWidgets.QLineEdit.Normal, new_name)
        if new_name == "":
            return
        new_name = new_name[0:4]

        if isinstance(self.current_item_parent().get_form().sub_chunks[current_item_index], compile.Form):
            self.current_item_parent().get_form().sub_chunks[current_item_index].form_type = str(new_name)
        else:
            self.current_item_parent().get_form().sub_chunks[current_item_index].chunk_id = str(new_name)

        self.current_item().setText(0, str(new_name))
        self.update_status("Selected chunk renamed")
        self.file_changed = True

    def export_form_chunk(self):
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export Form to File")
        if filename:
            self.current_item().save_to_file(filename)
            self.update_status("Saved selected FORM chunk")

    def export_data_to_file(self):
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export Chunk to File")
        if filename:
            self.current_item().save_to_file(filename)
            self.update_status("Saved selected Chunk chunk")

    def replace_vbmp_data(self):
        # TODO Requires VBMP to have .replace_bitmap() method
        if self.current_item().chunk_id() != "BODY":
            self.update_status("You must select the BODY chunk of a VBMP first!")
            return None
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select a 256*256 8bit BMP File")
        if filename:
            with open(filename, "rb") as f:
                f.seek(10)
                data_offset = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

                f.seek(18)
                width = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]
                height = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

                f.seek(28)
                bpp = struct.unpack(unsigned_short_be, f.read(size_of_unsigned_short))[0]

                if bpp != 8 or width != 256 or height != 256:
                    self.update_status("Selected bitmap was not in the correct format.")
                    print("Bitmap must be 256x256 and using an indexed 8bit color map!\n"
                          "Image was: %s*%sx%s" % (str(width), str(height), str(bpp)))
                    return None

                f.seek(data_offset)
                bitmap_data = f.read(65536)
                self.current_item().get_chunk().chunk_data = bitmap_data
                self.update_status("Updated VBMP BODY successfully")
                self.file_changed = True
                # print(jsonpickle.dumps({"data": bitmap_data}))

    def import_data_from_file(self):
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import Form Chunk File")
        if filename:
            new_chunk = compile.Chunk().load_from_file(filename)
            self.plainTextEdit.setPlainText(new_chunk.to_json())

    def clear_status(self):
        self.update_status("")

    def update_status(self, status):
        self.statusbar.showMessage(status)

    def convert_to_form(self):
        # Todo Requires Chunk to have .convert() method
        self.update_status("Error: Not implemented")

    def convert_to_chunk(self):
        # Todo Requires Form to have .convert() method
        self.update_status("Error: Not implemented")

    def replace_form(self):
        # TODO Requires MyQTreeWidgetItem to implement .replace_form()
        current_item_index = self.current_item_index()
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import Form Chunk File")
        if filename:
            # noinspection PyArgumentList
            local_bas_struct = compile.Form().load_from_file(filename)

            self.current_item_parent().get_form().sub_chunks[current_item_index] = local_bas_struct
            self.refresh_tree_widget()

    def delete_selected(self):
        current_item = self.current_item()
        current_item_index = self.current_item_index()

        self.current_item_parent().get_form().sub_chunks.pop(current_item_index)

        self.current_item_parent().removeChild(current_item)
        self.update_status("Selected chunk deleted")
        self.file_changed = True

    def insert_chunk_below(self):
        current_item_index = self.current_item_index()
        new_chunk = compile.Chunk("NEW1")
        print("added new chunk")

        if self.current_item().is_form():
            self.current_item().get_form().sub_chunks.insert(0, new_chunk)
            self.current_item().insertChild(0, self.iterate_and_add(new_chunk))
        else:
            self.current_item_parent().get_form().sub_chunks.insert(current_item_index + 1, new_chunk)
            self.current_item_parent().insertChild(current_item_index + 1, self.iterate_and_add(new_chunk))

        self.file_changed = True

    def iterate_and_add(self, sub_chunk, parent=None, idx=None):
        new_twi = MyQTreeWidgetItem(parent)
        new_twi.icons = self.icons
        new_twi.associate(sub_chunk)

        if isinstance(sub_chunk, compile.Form):
            if sub_chunk.form_type == "OBJT":
                new_twi.setText(0, str(sub_chunk.form_type) + " " + str(idx))
            else:
                new_twi.setText(0, str(sub_chunk.form_type))

            for idx, child in enumerate(sub_chunk.sub_chunks):
                self.iterate_and_add(child, new_twi, idx)
        else:
            if sub_chunk.chunk_id == "EMRS":
                dat = sub_chunk.get_data().replace(b"\0", b"")
                new_twi.setText(0, str(
                    sub_chunk.chunk_id + " " + str((idx - 1) / 2) + "(" + bytes(dat).decode() + ")"))
            elif sub_chunk.chunk_id == "NAME" or sub_chunk.chunk_id == "NAM2" or sub_chunk.chunk_id == "CLID":
                dat = sub_chunk.get_data().replace(b"\0", b"")
                new_twi.setText(0, str(sub_chunk.chunk_id + "(" + bytes(dat).decode() + ")"))
            else:
                new_twi.setText(0, str(sub_chunk.chunk_id))

        return new_twi

    def open_bas(self):
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open a .BAS File")

        if filename:
            file_extension = str(filename).lower()[-4:]
            if file_extension in [".bas", ".anm", ".ilb", ".skl"]:
                print("adding BAS top_level_item to tree_widget")
                self.top_level_form.load_from_file(filename)
            else:
                self.update_status("You must select a file that ends with with .bas")
                return

            self.refresh_tree_widget()
            self.file_changed = False
            self.setWindowTitle(self.default_windows_title + " " + filename)

    def refresh_tree_widget(self):
        self.treeWidget.clear()
        self.treeWidget.insertTopLevelItem(0, self.iterate_and_add(self.top_level_form))
        if self.treeWidget.topLevelItem(0):
            self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
        self.update_status("QWidgetTree refreshed from memory.")

    def selection_changed(self):
        current_item = self.current_item()
        self.plainTextEdit.setPlainText("")
        self.VBMP_display.hide()
        self.GLWidget.clear()
        self.GLWidget.hide()
        self.plainTextEdit.hide()
        self.pushButton_2.hide()

        if self.current_item_parent():
            print("current_item_index: ", self.current_item_parent().indexOfChild(current_item))

        if current_item and current_item.is_editable():
            self.plainTextEdit.show()
            self.pushButton_2.show()

            self.plainTextEdit.setPlainText(current_item.to_json())
            self.update_status("Loaded json for %s" % current_item.chunk_id())

        if current_item and current_item.can_render_bitmap():
            self.VBMP_display.show()
            # noinspection PyArgumentList
            data = QtCore.QByteArray(current_item.child(1).get_data())
            image = QtGui.QImage(data, 256, 256, QtGui.QImage.Format_Indexed8)
            image = image.mirrored(False, True)  # Flip image so the BMP is saved correctly
            # fakeColorTable = [QtGui.qRgb(i, i, i) for i in range(256)]
            image.setColorTable(compile.color_table)
            image.save("preview.bmp")
            # noinspection PyArgumentList
            new_pix = QtGui.QPixmap().fromImage(image)
            self.VBMP_display.setPixmap(new_pix)

        if current_item and current_item.form_type() == "SKLT":
            self.GLWidget.show()
            vertices = current_item.get_form().get_single_chunk_by_id("POO2")
            edges = current_item.get_form().get_single_chunk_by_id("POL2")

            poo2_list = []
            pol2_list = []

            if vertices:
                vertices_data = vertices.get_data()
                print(vertices, edges)

                poo2 = compile.Poo2()
                poo2.set_binary_data(vertices_data)
                poo2_list = [(point["x"], point["y"], point["z"]) for point in poo2.points]

            if edges:
                edges_data = edges.get_data()
                pol2 = compile.Pol2()
                pol2.set_binary_data(edges_data)
                pol2_list = pol2.edges

            new_mesh = Mesh()
            new_mesh.edges = pol2_list
            new_mesh.vertices = poo2_list
            new_mesh.texture = None
            self.GLWidget.meshes.append(new_mesh)

            print(poo2_list, pol2_list)

        if current_item and current_item.form_type() == "OBJT" and not current_item.get_form().get_single_form_by_type("KIDS"):

            amshes = current_item.get_form().get_all_form_by_type("AMSH")
            sklc = current_item.get_form().get_single_form_by_type("SKLC")
            if amshes and sklc:
                for amsh in amshes:
                    sklc_name = sklc.get_single_chunk_by_id("NAME")
                    atts = amsh.get_single_chunk_by_id("ATTS")
                    olpl = amsh.get_single_chunk_by_id("OLPL")
                    nam2 = amsh.get_single_chunk_by_id("NAM2")

                    if sklc_name and nam2 and atts and olpl:
                        self.GLWidget.show()
                        new_mesh = Mesh()
                        sklc_name_data = sklc_name.get_data()
                        atts_data = atts.get_data()
                        olpl_data = olpl.get_data()
                        nam2_data = nam2.get_data()

                        top_level = self.treeWidget.topLevelItem(0)  # type: MyQTreeWidgetItem
                        embd = top_level.get_form().get_single_form_by_type("EMBD")

                        temp_name = compile.Name()
                        temp_name.set_binary_data(sklc_name_data)
                        sklt_name = temp_name.name
                        new_mesh.load_sklt_from_embd(embd, sklt_name[:-1])
                        #new_mesh.load_sklt_by_name(sklt_name[:-1])

                        nam2 = compile.Nam2()
                        nam2.set_binary_data(nam2_data)
                        new_mesh.load_ilbm_from_embd(embd, nam2.name[:-1])
                        #new_mesh.load_ilbm_by_name(nam2.name[:-1])

                        atts = compile.Atts()
                        atts.set_binary_data(atts_data)
                        atts_pols = [x["poly_id"] for x in atts.atts_entries]

                        olpl = compile.Olpl()
                        olpl.set_binary_data(olpl_data)
                        olpl_coordinates = olpl.points

                        new_mesh.texture = list(zip(atts_pols, olpl_coordinates))
                        self.GLWidget.meshes.append(new_mesh)

                        print(atts_pols)
                        print(olpl_coordinates)

        if current_item:
            path = current_item.text(0)
            while current_item.parent():
                path = current_item.parent().text(0) + "/" + path
                current_item = current_item.parent()
            self.plainTextEdit_path.setPlainText(path)

    def update_modifications(self):
        if self.current_item().is_chunk():
            # TODO Requires Chunk to have .from_json() method
            self.current_item().from_json(myjson.loads(self.plainTextEdit.toPlainText()))
            #self.plainTextEdit.toPlainText()
            #
            self.update_status("Saved changed into memory.")
            self.file_changed = True

    def save_to_bas(self):
        # noinspection PyArgumentList,PyCallByClass
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save to BAS File")
        if filename:
            self.top_level_form.save_to_file(filename)
            self.file_changed = False
            self.setWindowTitle(self.default_windows_title + " " + filename)
            self.update_status("Saved " + filename)


def generate_color_table():
    """

    :rtype: list[QtGui.qRgb]
    """
    # This function is here to regenerate a new color_table if necessary
    file = open("colorMap.bin", "rb")
    data = file.read()
    file.close()

    my_color_table = []
    for i in range(0, len(data), 4):
        b, g, r, a = struct.unpack("4B", data[i:i + 4])
        my_color_table.append(QtGui.qRgb(r, g, b))

    return my_color_table


if __name__ == "__main__":
    print("\n\ncurrently in debug mode")
    print(sys.version)
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
