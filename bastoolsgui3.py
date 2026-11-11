#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 20:24:06 2014

@author: GoldStar611, Ormu
"""
import os
import struct
import sys
from typing import List, Optional, Union

import numpy
from PyQt6 import QtGui, QtCore, uic, QtWidgets, QtOpenGLWidgets
from OpenGL.GL import glClearColor
from PyQt6.QtOpenGL import QOpenGLTexture

import compile
import myjson

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
        self.association: Optional[Union[compile.Form, compile.Chunk]] = None
        self.icons = {}
        
    def child(self, p_int: int) -> Optional["MyQTreeWidgetItem"]:
        return super(MyQTreeWidgetItem, self).child(p_int)

    def parent(self) -> Optional["MyQTreeWidgetItem"]:
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

    def get_form(self) -> Optional[compile.Form]:
        if self.is_form():
            return self.association

    def form_type(self) -> Optional[str]:
        if self.is_form():
            return self.association.form_type

    def is_chunk(self):
        return isinstance(self.association, compile.Chunk)

    def get_chunk(self) -> Optional[compile.Chunk]:
        if self.is_chunk():
            return self.association

    def chunk_id(self) -> Optional[str]:
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

    def can_render_animation(self):
        if self.is_form():
            if self.association.form_type == "VANM":
                return True
            # A VANM is a modifier: BANI-carrying AREA/FARE objects reference
            # it by name (BANI lives below an OBJT child of the AREA).
            if self.association.form_type in ("AREA", "FARE"):
                return self._animation_reference() is not None
            # Animation units are OBJT-type forms with a CLID child (like the
            # textured wireframe path) that contain animated areas.
            if (self.association.form_type == "OBJT"
                    and isinstance(self.association, compile.Form)
                    and self.association.get_single("CLID") is not None):
                return len(self.animated_areas()) > 0
        return False

    def _clid_class(self):
        if self.form_type() != "OBJT":
            return None
        clid = self.get_form().get_direct_single("CLID")
        if isinstance(clid, compile.Clid):
            return clid.class_id
        return None

    def is_renderable_unit(self):
        """A renderable object unit is an OBJT with CLID base.class whose BASE
        holds a direct ADES part list (a whole vehicle/building/ground entry).
        Skeleton-only links (SKLC, no ADES) draw nothing and are skipped."""
        if self._clid_class() != "base.class":
            return False
        base = self.get_form().get_direct_single("BASE")
        if not isinstance(base, compile.Form):
            return False
        ades = base.get_direct_single("ADES")
        return (isinstance(ades, compile.Form)
                and bool(getattr(ades, "sub_chunks", None)))

    def animation_object_units(self):
        """Self and descendant renderable object units (OBJT+CLID base.class
        with a direct ADES payload). A qualifying OBJT is one unit; its own
        subtree (area/amesh parts, nested links) is not searched further."""
        units = []
        if not self.is_form():
            return units
        if self.is_renderable_unit():
            units.append(self)
            return units
        for i in range(self.childCount()):
            child = self.child(i)
            if child.is_form():
                units.extend(child.animation_object_units())
        return units

    # FLATTRACY polFlag bit: the polygon draws as a translucent "tracy"
    # effect with a global vertex alpha (area.cpp:293-294).
    POLFLAG_FLATTRACY = 0x80

    # gfx.alpha, the engine's global LUMTRACY vertex alpha (inivals.cpp:12).
    LUMTRACY_ALPHA = 192 / 255.0

    def animated_areas(self):
        """Return [(anim_name, poly_index, luminance)] for BANI-driven
        AREA/FARE forms below this item; luminance marks FLATTRACY polys."""
        ret = []
        if not isinstance(self.association, compile.Form):
            return ret
        for area in self.association.get_all("AREA"):
            if not isinstance(area, compile.Form):
                continue
            anim_name, poly_index, luminance = self._bani_reference_for_area(area)
            if anim_name:
                ret.append((anim_name, poly_index, luminance))
        for area in self.association.get_all("FARE"):
            if not isinstance(area, compile.Form):
                continue
            anim_name, poly_index, luminance = self._bani_reference_for_area(area)
            if anim_name:
                ret.append((anim_name, poly_index, luminance))
        return ret

    def _bani_reference_for_area(self, area):
        """Return (anim_name, poly_index, luminance) for the BANI animation
        driving *area*; luminance reflects the FLATTRACY polFlag of the
        area's STRC_AREA flavor (the surface header, area.cpp:89-122)."""
        bani = area.get_single("BANI")
        if isinstance(bani, compile.Bani) and bani.animation and bani.animation.anim_name:
            anim_name = bani.animation.anim_name
            poly_index = None
            luminance = False
            for strc in area.get_all("STRC"):
                if getattr(strc, "strc_type", None) == "STRC_AREA":
                    luminance = bool(
                        getattr(strc, "polFlags", 0) & self.POLFLAG_FLATTRACY)
                if poly_index is None and getattr(strc, "poly", None) is not None:
                    poly_index = strc.poly
            return anim_name, poly_index, luminance
        return None, None, False

    def _animation_reference(self):
        """The BANI STRC ``anim_name`` below an AREA/FARE form, if any."""
        if self.association.form_type not in ("AREA", "FARE"):
            return None
        bani = self.association.get_single("BANI")
        if isinstance(bani, compile.Bani) and bani.animation:
            return bani.animation.anim_name
        return None

    def _animation_poly_index(self):
        """The STRC poly index of the BANI-carrying AREA (which mesh polygon)."""
        if self.association.form_type not in ("AREA", "FARE"):
            return None
        for strc in self.association.get_all("STRC"):
            if getattr(strc, "poly", None) is not None:
                return strc.poly
        return None

    def _area_alpha(self):
        """Vertex alpha for an AREA/FARE poly: the LUMTRACY factor for
        FLATTRACY polys, else 1.0 (area.cpp:293-302)."""
        if self.association.form_type not in ("AREA", "FARE"):
            return 1.0
        for strc in self.association.get_all("STRC"):
            if getattr(strc, "strc_type", None) != "STRC_AREA":
                continue
            polflags = getattr(strc, "polFlags", 0)
            if polflags & self.POLFLAG_FLATTRACY:
                return self.LUMTRACY_ALPHA
        return 1.0

    def can_render_3d(self):
        if self.is_form():
            if self.association.form_type in ["SKLT", "AMSH"]:
                return True
        return False

    def is_editable(self):
        if self.is_chunk():
            return True
        return False

    def get_data(self) -> bytes:
        return self.association.get_data()

    def full_data(self) -> bytes:
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
QtUserRole = QtCore.Qt.ItemDataRole.UserRole

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
        cache_key = ilbm_name.upper()
        if cache_key in Animation.ilbm_image_cache:
            image = Animation.ilbm_image_cache[cache_key]
            self.image = image
            return image
        if hasattr(embd_form, "emrs_resources"):
            candidates = [ilbm_name]
            base, dot, ext = ilbm_name.rpartition(".")
            if ext.upper() == "ILB":
                candidates.append(base + ".ILBM")
            for candidate in candidates:
                for key, res in embd_form.emrs_resources.items():
                    if key.upper() == candidate.upper():
                        data = res.full_data()[34:]
                        image = QtGui.QImage(QtCore.QByteArray(data), width, height,
                                              QtGui.QImage.Format.Format_Indexed8)
                        image = image.mirrored(mirror_horizontal, mirror_vertical)
                        image.setColorTable(compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE))
                        image = Animation.map_yellow_to_alpha(image)
                        Animation.ilbm_image_cache[ilbm_name.upper()] = image
                        self.image = image
                        return image
        for i, chunk in enumerate(embd_form.sub_chunks):
            if bytes(ilbm_name, "ascii") in chunk.get_data():
                data = embd_form.sub_chunks[i + 1].full_data()[34:]

                image = QtGui.QImage(data, width, height, QtGui.QImage.Format.Format_Indexed8)
                image = image.mirrored(mirror_horizontal, mirror_vertical)
                image.setColorTable(compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE))
                self.image = image
                return image

    def load_ilbm_by_name(self, ilbm_name: str, width: int = 256, height: int = 256,
                          mirror_horizontal: bool = False, mirror_vertical: bool = True) -> QtGui.QImage:
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

        image = QtGui.QImage(data, width, height, QtGui.QImage.Format.Format_Indexed8)
        image = image.mirrored(mirror_horizontal, mirror_vertical)
        image.setColorTable(compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE))
        self.image = image

        return image

    def load_sklt_from_embd(self, embd_form, sklt_name):
        for i, chunk in enumerate(embd_form.sub_chunks):
            if bytes(sklt_name, "ascii") in chunk.get_data():
                print("Found ", sklt_name, "in embd")
                sklt = embd_form.sub_chunks[i + 1]
                sklt_poo2_data = sklt.get_single("POO2").get_data()
                poo2 = compile.Poo2()
                poo2.set_binary_data(sklt_poo2_data)
                vertices = poo2.points_as_list()
                self.vertices = vertices

                sklt_pol2_data = sklt.get_single("POL2").get_data()
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

        sklt_poo2_data = sklt.get_single("POO2").get_data()
        poo2 = compile.Poo2()
        poo2.set_binary_data(sklt_poo2_data)
        vertices = poo2.points_as_list()
        self.vertices = vertices

        sklt_pol2_data = sklt.get_single("POL2").get_data()
        pol2 = compile.Pol2()
        pol2.set_binary_data(sklt_pol2_data)
        edges = pol2.edges
        self.edges = edges

        return vertices, edges


class Animation(object):
    """Bitmap animation built from a VANM form.

    A VANM does not render by itself; it is a *modifier* referenced from
    another object (BANI/AREA in a building or vehicle). Each frame names a
    VBMP plus polygon coords (bitmap pixel space) that act as the *texture
    coordinates* for the animated object's polygon; per frame the whole
    bitmap is bound and the polygon vertices are mapped onto those coords."""

    def __init__(self):
        self.frames = []
        self.frame_index = 0
        self.elapsed_ms = 0
        self.playing = True
        self.loop = True

    def load_vanm(self, vanm_form, embd_form):
        """Resolve a VANM's frames from its EMBD through the sibling VBMPs."""
        for frame in vanm_form.frames:
            image = self.qimage_from_vbmp(embd_form, frame["vbmp_name"])
            if image is not None:
                self.frames.append((frame["frame_time"],
                                    image,
                                    frame["vbmp_coords"]))
        self.elapsed_ms = 0
        self.frame_index = 0 if self.frames else -1
        return self

    @staticmethod
    def find_resource(embd_form, name):
        """EMBD lookup by exact name first, case-insensitive as fallback."""
        resource = embd_form.emrs_resources.get(name)
        if resource is None:
            for emrs_name, candidate in embd_form.emrs_resources.items():
                if emrs_name.upper() == name.upper():
                    resource = candidate
                    break
        return resource

    sklt_cache = {}
    mesh_cache = {}
    vanm_cache = {}
    ilbm_image_cache = {}
    static_texture_cache = {}

    @staticmethod
    def load_vanm_by_name(embd_form, anim_name):
        """Build the animation for a BANI STRC ``anim_name`` (e.g. 'SMILEY1.ANM')."""
        if not anim_name:
            return None
        if anim_name in Animation.vanm_cache:
            return Animation.vanm_cache[anim_name]
        vanm = Animation.find_resource(embd_form, anim_name)
        if vanm is None or vanm.form_type != "VANM":
            return None
        animation = Animation().load_vanm(vanm, embd_form)
        Animation.vanm_cache[anim_name] = animation
        return animation

    @staticmethod
    def load_sklt_by_name(embd_form, sklt_name):
        """Resolve a skeleton (POO2 points + POL2 edges) from the EMBD."""
        if not sklt_name:
            return None
        if sklt_name in Animation.sklt_cache:
            return Animation.sklt_cache[sklt_name]
        sklt = Animation.find_resource(embd_form, sklt_name)
        if sklt is None or sklt.form_type != "SKLT":
            return None
        poo2 = sklt.get_single("POO2")
        pol2 = sklt.get_single("POL2")
        if poo2 is None or pol2 is None:
            return None
        Animation.sklt_cache[sklt_name] = sklt
        return sklt

    @staticmethod
    def crop_polygon(image, polygon):
        """Crop *image* to the bounding box of *polygon* (xy uv coords)."""
        if not polygon:
            return image
        xs = [p[0] for p in polygon]
        ys = [p[1] for p in polygon]
        left = max(0, min(xs) - 1)
        top = max(0, min(ys) - 1)
        right = min(image.width(), max(xs) + 1)
        bottom = min(image.height(), max(ys) + 1)
        if left >= right or top >= bottom:
            return image
        return image.copy(left, top, right - left, bottom - top)

    @property
    def current_image(self):
        if 0 <= self.frame_index < len(self.frames):
            return self.frames[self.frame_index][1]
        return None

    @property
    def current_uvs(self):
        if 0 <= self.frame_index < len(self.frames):
            return self.frames[self.frame_index][2]
        return None

    def duration_ms(self):
        return sum(frame[0] for frame in self.frames)

    def advance(self, delta_ms):
        """Advance playback by *delta_ms*; returns True when a new frame begins."""
        if not self.frames or not self.playing:
            return False
        if self.frame_index < 0:
            self.frame_index = 0
            self.elapsed_ms = 0
            return True
        self.elapsed_ms += delta_ms
        started_frame = False
        while self.elapsed_ms >= self.frames[self.frame_index][0]:
            self.elapsed_ms -= self.frames[self.frame_index][0]
            self.frame_index += 1
            started_frame = True
            if self.frame_index >= len(self.frames):
                if not self.loop:
                    self.frame_index = len(self.frames) - 1
                    self.playing = False
                    self.elapsed_ms = 0
                    break
                self.frame_index = 0
        return started_frame

    @staticmethod
    def qimage_from_vbmp(embd_form, vbmp_name):
        """Look up *vbmp_name* in the EMBD and decode it into a QImage."""
        for emrs_name, resource in embd_form.emrs_resources.items():
            if emrs_name == vbmp_name and resource.form_type == "VBMP":
                data = resource.full_data()[34:]
                # QImage does not copy the buffer we hand it, so take a deep
                # copy right away; and convert indexed8 -> RGB32 so the
                # palette survives texture upload.
                image = QtGui.QImage(QtCore.QByteArray(data), 256, 256,
                                     256, QtGui.QImage.Format.Format_Indexed8)
                image = image.mirrored(False, True)
                image.setColorTable(compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE))
                image = image.convertToFormat(QtGui.QImage.Format.Format_RGB32)
                return Animation.map_yellow_to_alpha(image)
        return None

    @staticmethod
    def map_yellow_to_alpha(image):
        """Return *image* with exactly palette-yellow (255, 255, 0) keyed
        transparent, matching the engine's ConvAlphaPalette
        (system/gfx.cpp:2202-2208). Every other color stays opaque; the
        translucent look of exhaust polys comes from the FLATTRACY render
        mode, not the key."""
        image = image.convertToFormat(QtGui.QImage.Format.Format_ARGB32)
        height = image.height()
        stride = image.bytesPerLine() // 4
        if not image.bytesPerLine() % 4:
            import ctypes
            pointer = ctypes.cast(int(image.constBits()),
                                  ctypes.POINTER(ctypes.c_uint32))
            array = numpy.ctypeslib.as_array(pointer, shape=(stride * height,))
            array = array.reshape(height, stride)
            # little endian ARGB: 0xAARRGGBB; pure yellow rgb = 0x00FFFF00
            yellow = numpy.uint32(0x00FFFF00)
            array &= numpy.uint32(0x00FFFFFF)
            array |= numpy.where(array == yellow,
                                 numpy.uint32(0), numpy.uint32(0xFF000000)).astype(numpy.uint32)
        return image


class GLWidget(QtOpenGLWidgets.QOpenGLWidget):
    x_rotation_changed = QtCore.pyqtSignal(float)
    y_rotation_changed = QtCore.pyqtSignal(float)
    z_rotation_changed = QtCore.pyqtSignal(float)

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

        self.zoom = 1.0

        self.meshes = [Mesh()]
        self.animation = None
        # Mesh-driven playback groups: [(mesh, poly_animations)] where each
        # mesh resolves from the skeleton nearest its animated areas.
        self.animation_groups = []
        self.animation_timer = QtCore.QTimer(self)
        self.animation_timer.setInterval(33)
        self.animation_timer.timeout.connect(self.animation_tick)

    def animation_tick(self):
        animations = [animation
                      for _, poly_animations, _ in self.animation_groups
                      for _, animation, _ in poly_animations]
        if self.animation is not None:
            animations.append(self.animation)
        if not animations:
            self.animation_timer.stop()
            return
        changed = any(animation.advance(self.animation_timer.interval())
                      for animation in animations)
        if changed:
            self.update()

    def play_animations(self, groups):
        """Play animation groups: [(mesh, poly_animations)] per skeleton."""
        self.animation = None
        self.animation_groups = groups
        self.animation_timer.start()
        self.update()

    def play_animation(self, animation: Animation):
        self.animation = animation
        self.animation_groups = []
        self.animation_timer.start()
        self.update()

    def stop_animation(self):
        self.animation_timer.stop()
        self.animation = None
        self.animation_groups = []
        self.update()

    def _bind_frame_texture(self, image):
        """Bind a VBMP frame as texture; matches the sklt mesh uv convention."""
        texture = QOpenGLTexture(image.mirrored())
        texture.setMagnificationFilter(QOpenGLTexture.Filter.Nearest)
        texture.setMinificationFilter(QOpenGLTexture.Filter.Nearest)
        texture.bind()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glDisable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        # MODULATE multiplies the fragment by glColor, so per-pixel keyed
        # alpha survives while a global tracy factor scales the whole poly.
        GL.glTexEnvi(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_MODULATE)
        return texture

    def _draw_textured_polygon(self, image, uvs, vertices, alpha=1.0):
        """Map *uvs* (bitmap pixel coords) onto polygon *vertices*."""
        texture = self._bind_frame_texture(image)
        if alpha < 1.0:
            # FLATTRACY polys glow additively (engine destblend path,
            # gfx.cpp:1047-1048): dark pixels add nothing, so the effect
            # melts into the background instead of shading it.
            GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE)
        else:
            GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glColor4f(1.0, 1.0, 1.0, alpha)
        GL.glBegin(GL.GL_POLYGON)
        for (uv_x, uv_y), vertex in zip(uvs, vertices):
            GL.glTexCoord2f(uv_x / 255.0, uv_y / 255.0)
            GL.glVertex3fv(vertex)
        GL.glEnd()
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glEnable(GL.GL_CULL_FACE)
        texture.release()

    @staticmethod
    def _static_texture_for_poly(static_textures, poly_index):
        """Return (atts_poly_ids, olpl_uvs, image) covering *poly_index*, if any."""
        for atts_pols, olpl_points, image in static_textures or []:
            if poly_index in atts_pols:
                return atts_pols, olpl_points, image
        return None

    def draw_animation(self):
        if self.animation_groups:
            for mesh, poly_animations, static_textures in self.animation_groups:
                vertices, edges = mesh
                if not vertices or not edges or not poly_animations:
                    continue
                scale_factor = numpy.amax([numpy.linalg.norm(x) for x in vertices]) * 2
                GL.glPushMatrix()
                GL.glScalef(1.0 / scale_factor, 1.0 / scale_factor, 1.0 / scale_factor)
                # Static polygons: textured where the AMSH defines a texture,
                # otherwise plain wireframe context
                animated_indices = set(poly_index for poly_index, _, _ in poly_animations)
                GL.glColor3f(1.0, 0.0, 1.0)
                GL.glLineWidth(1.0)
                GL.glBegin(GL.GL_LINES)
                for poly_index, edge in enumerate(edges):
                    if poly_index in animated_indices:
                        continue
                    if not self._static_texture_for_poly(static_textures, poly_index):
                        for j, vertex_index in enumerate(edge):
                            next_index = edge[(j + 1) % len(edge)]
                            GL.glVertex3fv(vertices[vertex_index])
                            GL.glVertex3fv(vertices[next_index])
                GL.glEnd()
                for poly_index in range(len(edges)):
                    if poly_index in animated_indices:
                        continue
                    textured = self._static_texture_for_poly(static_textures, poly_index)
                    if textured is not None:
                        atts_pols, olpl_points, image = textured
                        try:
                            slot = atts_pols.index(poly_index)
                            uvs = olpl_points[slot]
                        except ValueError:
                            continue
                        poly_vertices = [vertices[vi] for vi in edges[poly_index]]
                        if len(uvs) != len(poly_vertices):
                            uvs = (list(uvs) * len(poly_vertices))[:len(poly_vertices)]
                        self._draw_textured_polygon(image, uvs, poly_vertices)
                # Animated polygons textured with the current frame
                for poly_index, animation, poly_alpha in poly_animations:
                    image = animation.current_image
                    uvs = animation.current_uvs
                    if image is None or uvs is None or poly_index >= len(edges):
                        continue
                    poly_vertices = [vertices[vi] for vi in edges[poly_index]]
                    if len(uvs) != len(poly_vertices):
                        # Coords do not align with the polygon; pad/clamp to vertex count
                        uvs = (list(uvs) * len(poly_vertices))[:len(poly_vertices)]
                    self._draw_textured_polygon(image, uvs, poly_vertices, poly_alpha)
                GL.glPopMatrix()
        elif self.animation is not None:
            image = self.animation.current_image
            if image is None:
                return
            # Standalone preview: sprite cropped to the frame polygon
            uvs = self.animation.current_uvs
            if uvs:
                image = Animation.crop_polygon(image, uvs)
            texture = QOpenGLTexture(image.mirrored(vertical=True))
            texture.setMagnificationFilter(QOpenGLTexture.Filter.Nearest)
            texture.setMinificationFilter(QOpenGLTexture.Filter.Nearest)
            texture.bind()
            GL.glEnable(GL.GL_TEXTURE_2D)
            GL.glDisable(GL.GL_CULL_FACE)
            GL.glEnable(GL.GL_BLEND)
            GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
            GL.glTexEnvi(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_REPLACE)
            side = 1.6  # sprite size in ortho view (-0.5..0.5 usable)
            GL.glBegin(GL.GL_QUADS)
            GL.glTexCoord2f(0.0, 1.0)
            GL.glVertex3f(-side / 2, -side / 2, 0.0)
            GL.glTexCoord2f(1.0, 1.0)
            GL.glVertex3f(side / 2, -side / 2, 0.0)
            GL.glTexCoord2f(1.0, 0.0)
            GL.glVertex3f(side / 2, side / 2, 0.0)
            GL.glTexCoord2f(0.0, 0.0)
            GL.glVertex3f(-side / 2, side / 2, 0.0)
            GL.glEnd()
            GL.glDisable(GL.GL_TEXTURE_2D)
            GL.glEnable(GL.GL_CULL_FACE)
            texture.release()

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def set_x_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.x_rotation:
            self.x_rotation = angle
            self.x_rotation_changed.emit(angle)
            self.update()

    def set_y_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.y_rotation:
            self.y_rotation = angle
            self.y_rotation_changed.emit(angle)
            self.update()

    def set_z_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.z_rotation:
            self.z_rotation = angle
            self.z_rotation_changed.emit(angle)
            self.update()

    def clear(self):
        self.meshes = []

    def draw_simpl(self, draw_texture=True):
        for mesh in self.meshes:
            GL.glPushMatrix()

            if draw_texture and mesh.texture and mesh.image:
                texture = QOpenGLTexture(mesh.image.mirrored())
                texture.setMinificationFilter(QOpenGLTexture.Filter.LinearMipMapLinear)
                texture.setMagnificationFilter(QOpenGLTexture.Filter.Linear)
                texture.bind()

                GL.glEnable(GL.GL_TEXTURE_2D)
                GL.glEnable(GL.GL_BLEND)
                GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
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
        # Black for pictures
        glClearColor(0.0, 0.0, 0.0, 1.0)
        # Grey for detecting missing texture
        glClearColor(0.33, 0.33, 0.33, 1.0)
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def showEvent(self, event):
        super().showEvent(event)
        self.update()

    def paintGL(self):
        try:
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            GL.glLoadIdentity()
            GL.glTranslated(self.camera_position["x"], self.camera_position["y"], self.camera_position["z"])
            GL.glScaled(self.zoom, self.zoom, self.zoom)
            GL.glRotated(self.x_rotation / 16.0, 1.0, 0.0, 0.0)
            GL.glRotated(self.y_rotation / 16.0, 0.0, 1.0, 0.0)
            GL.glRotated(self.z_rotation / 16.0, 0.0, 0.0, 1.0)
            # GL.glCallList(self.object))
            if self.animation is not None or self.animation_groups:
                self.draw_animation()
            else:
                self.draw_simpl()
        except Exception:
            import traceback
            traceback.print_exc()

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
        self.last_position = event.position()

    def wheelEvent(self, event):
        # Ortho projection: zoom scales about the view center
        angle = event.angleDelta().y()
        if angle == 0:
            return
        factor = 1.1 if angle > 0 else 1.0 / 1.1
        self.zoom = max(0.05, min(50.0, self.zoom * factor))
        self.update()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_A:
            self.camera_position["x"] -= 0.01
        if event.key() == QtCore.Qt.Key.Key_D:
            self.camera_position["x"] += 0.01
        if event.key() == QtCore.Qt.Key.Key_W:
            self.camera_position["y"] -= 0.01
        if event.key() == QtCore.Qt.Key.Key_S:
            self.camera_position["y"] += 0.01
        if event.key() == QtCore.Qt.Key.Key_Space:
            if self.animation is not None:
                self.animation.playing = not self.animation.playing
            else:
                self.camera_position["x"] = 0.0
                self.camera_position["y"] = 0.0
                self.zoom = 1.0
                self.x_rotation = 0.0
                self.y_rotation = 0.0
                self.z_rotation = 0.0
        if event.key() == QtCore.Qt.Key.Key_Escape and self.animation is not None:
            self.stop_animation()
        if event.key() == QtCore.Qt.Key.Key_Q:
            self.grabFrameBuffer().save("opengl.bmp")
        self.update()

    def mouseMoveEvent(self, event):
        dx = event.position().x() - self.last_position.x()
        dy = event.position().y() - self.last_position.y()

        if event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.set_x_rotation(self.x_rotation + 8.0 * -dy)
            self.set_y_rotation(self.y_rotation + 8.0 * dx)
        elif event.buttons() & QtCore.Qt.MouseButton.RightButton:
            self.set_x_rotation(self.x_rotation + 8.0 * -dy)
            self.set_z_rotation(self.z_rotation + 8.0 * dx)

        self.last_position = event.position()

    @staticmethod
    def normalize_angle(angle: float) -> float:
        while angle < 0.0:
            angle += 360.0 * 16.0
        while angle > 360.0 * 16.0:
            angle -= 360.0 * 16.0
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
        self.GLWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
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

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if hasattr(sys, "_MEIPASS"):
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        else:
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
                                                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
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
        self.actionRefresh_Tree_Widget.triggered.connect(self.refresh_tree_widget)
        self.actionSearch.triggered.connect(self.search)
        self.actionSearch_Next.triggered.connect(self.search_next)
        self.actionGoto.triggered.connect(self.goto)

        # TODO: replace_vbmp_data ??

        print("all signals connected")
        self.update_status("Use [Ctrl]+[O] to open .BAS file.")

    def current_item(self) -> Optional[MyQTreeWidgetItem]:
        return self.treeWidget.currentItem()

    def current_item_parent(self) -> Optional[MyQTreeWidgetItem]:
        if self.current_item():
            return self.current_item().parent()

    @staticmethod
    def object_from_tree_widget_item(tree_widget_item: MyQTreeWidgetItem) -> Optional[Union[compile.Form, compile.Chunk]]:
        return tree_widget_item.association

    def current_item_index(self):
        if self.current_item_parent():
            return self.current_item_parent().indexOfChild(self.current_item())

    def find_skeleton_for_item(self, tree_widget_item, embd):
        """Resolve the (vertices, edges) mesh of the skeleton owning *item*.

        Top-level objects (buildings, vehicles, ground) carry a SKLC naming
        their skeleton; kids hang under them per the MC2/OBJT/BASE/KIDS/OBJT
        tree."""
        item = tree_widget_item
        while item is not None:
            association = item.association
            if association is not None and not isinstance(association, compile.Chunk):
                name_chunks = association.get_all("SKLC")
            else:
                name_chunks = []
            for chunk in name_chunks:
                names = chunk.get_all("NAME")
                for name_chunk in names:
                    sklt_name = name_chunk.name
                    sklt = Animation.load_sklt_by_name(embd, sklt_name)
                    if sklt is not None:
                        if sklt_name not in Animation.mesh_cache:
                            poo2 = sklt.get_single("POO2")
                            pol2 = sklt.get_single("POL2")
                            vertices = [(point["x"], point["y"], point["z"]) for point in poo2.points]
                            edges = pol2.edges
                            Animation.mesh_cache[sklt_name] = (vertices, edges)
                        mesh = Animation.mesh_cache[sklt_name]
                        if sklt_name not in Animation.static_texture_cache:
                            Animation.static_texture_cache[sklt_name] = \
                                self.find_static_textures(item, embd)
                        static_textures = Animation.static_texture_cache[sklt_name]
                        return mesh, sklt_name, static_textures
            item = item.parent()
        return None, None, []

    def find_static_textures(self, tree_widget_item, embd):
        """Collect static (non-bmpanim) AMSH textures at/below *item*.

        Returns [(atts_poly_ids, olpl_uvs, image)] where poly ids index into
        the skeleton POL2 polygons and uvs are per-vertex bitmap coords."""
        static_textures = []
        seen_atts = set()
        seen_forms = set()
        stack = []

        if tree_widget_item.is_form() and tree_widget_item.association is not None:
            stack.append(tree_widget_item.association)

        while stack:
            form = stack.pop()
            if not isinstance(form, compile.Form):
                continue
            if id(form) in seen_forms:
                continue
            seen_forms.add(id(form))
            atts = form.get_direct_single("ATTS")
            olpl = form.get_direct_single("OLPL")
            if atts is not None and olpl is not None and id(atts) not in seen_atts:
                seen_atts.add(id(atts))
                nam2 = form.get_single("NAM2")
                if isinstance(nam2, compile.Nam2):
                    atts_data = compile.Atts()
                    atts_data.set_binary_data(atts.get_data())
                    olpl_data = compile.Olpl()
                    olpl_data.set_binary_data(olpl.get_data())
                    image = Mesh().load_ilbm_from_embd(embd, nam2.name[:-1])
                    if image is not None:
                        static_textures.append(
                            ([x["poly_id"] for x in atts_data.atts_entries],
                             olpl_data.points, image))
            stack.extend(
                sub_chunk for sub_chunk in reversed(form.sub_chunks)
                if isinstance(sub_chunk, compile.Form))
        return static_textures

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
                                level: int = 0,
                                search_selected: bool = False,
                                search_parents: bool = False) -> Optional[MyQTreeWidgetItem]:
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

    def clear_status(self):
        self.update_status("")

    def update_status(self, status):
        self.statusbar.showMessage(status)

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
            self.load_bas_file(filename)

    def load_bas_file(self, filename: str) -> bool:
        """Load *filename* and populate the tree; False if rejected."""
        file_extension = str(filename).lower()[-4:]
        if file_extension not in [".bas", ".anm", ".ilb", ".skl"]:
            self.update_status("You must select a file that ends with with .bas")
            return False

        print("adding BAS top_level_item to tree_widget")
        self.top_level_form.load_from_file(filename)

        self.refresh_tree_widget()
        self.file_changed = False
        self.setWindowTitle(self.default_windows_title + " " + filename)
        return True

    def refresh_tree_widget(self):
        self.treeWidget.clear()
        self.treeWidget.insertTopLevelItem(0, self.iterate_and_add(self.top_level_form))
        if self.treeWidget.topLevelItem(0):
            self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
        self.update_status("QWidgetTree refreshed from memory.")

    def selection_changed(self):
        current_item = self.current_item()
        self.plainTextEdit.setPlainText("")
        self.statusbar.clearMessage()
        self.VBMP_display.hide()
        self.GLWidget.stop_animation()
        self.GLWidget.clear()
        self.GLWidget.hide()
        self.plainTextEdit.hide()
        self.pushButton_2.hide()

        if self.current_item_parent():
            print("current_item_index: ", self.current_item_parent().indexOfChild(current_item))

        if current_item and current_item.can_render_animation():
            self.GLWidget.show()
            # The EMBD is not an ancestor of the current item; it is a
            # sibling branch of the top-level MC2 form.
            embd = self.top_level_form.get_single("EMBD")
            if embd is None:
                self.update_status("No EMBD parent found for this animation")
            else:
                if current_item.form_type() == "VANM":
                    animation = Animation().load_vanm(current_item.get_form(), embd)
                    if animation is not None and animation.frames:
                        self.update_status("Playing %d frames (%d ms loop)" % (
                            len(animation.frames), animation.duration_ms()))
                        self.GLWidget.play_animation(animation)
                    else:
                        self.update_status("Could not resolve animation frames")
                elif current_item.form_type() in ("AREA", "FARE"):
                    # AREA/FARE: the BANI descendant names the VANM to play;
                    # its STRC poly index tells which mesh polygon animates.
                    anim_name = current_item._animation_reference()
                    animation = (Animation.load_vanm_by_name(embd, anim_name)
                                 if anim_name else None)
                    poly_index = current_item._animation_poly_index()
                    poly_alpha = current_item._area_alpha()
                    if animation is not None and animation.frames:
                        mesh, sklt_name, static_textures = self.find_skeleton_for_item(current_item, embd)
                        if mesh is not None and poly_index is not None and 0 <= poly_index < len(mesh[1]):
                            self.update_status("Playing %d frames (%d ms loop) on skeleton %s polygon %d" % (
                                len(animation.frames), animation.duration_ms(),
                                sklt_name, poly_index))
                            self.GLWidget.play_animations(
                                [(mesh, [(poly_index, animation, poly_alpha)], static_textures)])
                        else:
                            # Fallback to standalone sprite preview
                            self.GLWidget.play_animation(animation)
                    else:
                        self.update_status("Could not resolve animation frames")
                else:
                    # Top-level selection: every renderable object unit beneath
                    # it (OBJT+CLID base.class with a direct ADES part list)
                    # plays its own animated areas against its own skeleton.
                    units = current_item.animation_object_units()
                    if len(units) > 1 and not current_item.is_renderable_unit():
                        # A container holding many units would render them all
                        # stacked at the origin; leave that to per-unit picks.
                        self.GLWidget.hide()
                        self.update_status(
                            "%d object unit(s) beneath; select one to render it"
                            % len(units))
                    else:
                        groups = []
                        unit_skelts = []
                        for unit in units:
                            mesh, sklt_name, static_textures = self.find_skeleton_for_item(unit, embd)
                            if mesh is None:
                                continue
                            unit_poly_animations = []
                            for anim_name, poly_index, luminance in unit.animated_areas():
                                animation = (Animation.load_vanm_by_name(embd, anim_name)
                                             if anim_name else None)
                                if (animation is not None and animation.frames
                                        and poly_index is not None
                                        and 0 <= poly_index < len(mesh[1])):
                                    poly_alpha = (MyQTreeWidgetItem.LUMTRACY_ALPHA
                                                  if luminance else 1.0)
                                    unit_poly_animations.append(
                                        (poly_index, animation, poly_alpha))
                            if unit_poly_animations:
                                groups.append((mesh, unit_poly_animations, static_textures))
                                unit_skelts.append(sklt_name)
                        if groups:
                            self.update_status("Playing %d frame(s) on %d object unit(s) %r" % (
                                sum(len(a.frames)
                                    for _, unit_polys, _ in groups
                                    for _, a, _ in unit_polys),
                                len(groups), unit_skelts))
                            self.GLWidget.play_animations(groups)
                        else:
                            self.update_status("Could not resolve animation frames under selected object")

        if current_item and current_item.is_editable():
            self.plainTextEdit.show()
            self.pushButton_2.show()

            self.plainTextEdit.setPlainText(current_item.to_json())
            self.update_status("Loaded json for %s" % current_item.chunk_id())

        if current_item and current_item.can_render_bitmap():
            self.VBMP_display.show()
            # noinspection PyArgumentList
            data = QtCore.QByteArray(current_item.child(1).get_data())
            image = QtGui.QImage(data, 256, 256, QtGui.QImage.Format.Format_Indexed8)
            image = image.mirrored(False, True)  # Flip image so the BMP is saved correctly
            image.setColorTable(compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE))
            image.save("preview.bmp")
            # noinspection PyArgumentList
            new_pix = QtGui.QPixmap().fromImage(image)
            self.VBMP_display.setPixmap(new_pix)

        if current_item and current_item.form_type() == "SKLT":
            self.GLWidget.show()
            vertices = current_item.get_form().get_single("POO2")
            edges = current_item.get_form().get_single("POL2")

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

        if current_item and current_item.form_type() == "OBJT" and not current_item.get_form().get_single("KIDS"):

            amshes = current_item.get_form().get_all("AMSH")
            sklc: compile.Sklc = current_item.get_form().get_single("SKLC")
            if amshes and sklc:
                for amsh in amshes:
                    atts = amsh.get_single("ATTS")
                    olpl = amsh.get_single("OLPL")
                    nam2 = amsh.get_single("NAM2")

                    if sklc.skeleton_name and nam2 and atts and olpl:
                        self.GLWidget.show()
                        new_mesh = Mesh()
                        atts_data = atts.get_data()
                        olpl_data = olpl.get_data()
                        nam2_data = nam2.get_data()

                        top_level: MyQTreeWidgetItem = self.treeWidget.topLevelItem(0)
                        embd = top_level.get_form().get_single("EMBD")

                        new_mesh.load_sklt_from_embd(embd, sklc.skeleton_name[:-1])
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


def generate_color_table() -> List[int]:
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
    if len(sys.argv) > 1:
        ex.load_bas_file(sys.argv[1])
    sys.exit(app.exec())
