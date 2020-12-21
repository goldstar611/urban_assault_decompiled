# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# SKLT import plugin for Blender - very experimental!
##Changelog at the end of this file

import bpy
from . import bcompile


def readSklt(filepath, sen2_mode):
    # convert the filename to an object name
    obj_name = bpy.path.display_name_from_filepath(filepath)

    sen2_vertices = []

    if filepath.endswith("json"):
        first_sklt = bcompile.Form().from_json_file(filepath)
    else:
        first_sklt = bcompile.Form().load_from_file(filepath)

    if first_sklt.form_type != "SKLT":
        first_sklt = first_sklt.get_single("SKLT")

    sklt_primitives = first_sklt.get_single("POL2").to_class().edges

    poo2 = first_sklt.get_single("POO2").to_class()
    poo2.scale_down(150)
    poo2.change_coordinate_system()
    sklt_vertices = poo2.points_as_list()

    if first_sklt.get_single("SEN2"):
        sen2 = first_sklt.get_single("SEN2").to_class()
        sen2.scale_down(150)
        sen2.change_coordinate_system()
        sen2_vertices = sen2.points_as_list()
        print(sen2_vertices)

    # create new mesh
    new_mesh = bpy.data.meshes.new(obj_name)
    # Try to create polygons, edges are created anyway, even if there are only lines, not polygons
    new_mesh.from_pydata(sklt_vertices, [], sklt_primitives)

    # add mesh into scene
    current_scene = bpy.context.scene
    new_mesh.update()
    new_mesh.validate()

    # create new object, add mesh to it
    new_obj = bpy.data.objects.new(obj_name, new_mesh)
    current_scene.objects.link(new_obj)

    # Create SEN2 frame with hard-coded name
    if sen2_mode is True and sen2_vertices:
        sen2_mesh = bpy.data.meshes.new("{}_SEN2".format(obj_name))
        sen2_mesh.from_pydata(sen2_vertices, [], [])
        sen2_mesh.update()
        sen2_mesh.validate()
        # Create SEN2 main object
        sen2_obj = bpy.data.objects.new("{}_SEN2".format(obj_name), sen2_mesh)
        current_scene.objects.link(sen2_obj)

    new_obj.select = True
    current_scene.objects.active = new_obj

# 30.8.2013: added SEN2 importing
