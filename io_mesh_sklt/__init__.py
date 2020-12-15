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


#SKLT import/export plugin for Blender - main script
#Very experimental - use at your own risk!
##Changelog at the end of this file

#plugin info
bl_info = {
    "name": "SKLT skeleton files",
    "location": "File > Import-Export",
    "description": "Import and export EA85/IFF SKLT skeleton files used in Urban Assault",
    "warning": "Very experimental!",
    "category": "Import-Export"}


if "bpy" in locals():
    import imp
    if "import_sklt" in locals():
        imp.reload(import_sklt)
        imp.reload(bcompile)
    if "export_sklt" in locals():
        imp.reload(export_sklt)
else:
    import bpy

from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper


#Operator for importing
class SKLTImport(bpy.types.Operator, ImportHelper):

    bl_idname = "fileimport.sklt"
    bl_label = "Import SKLT"
    bl_options = {"UNDO"}


    filepath = StringProperty(subtype='FILE_PATH')
    filter_glob = StringProperty(name="Filename filter", default="*.sklt;*.skl;*.bas;*.json")
    sen2_import = BoolProperty(name="Import SEN2", description="Import data from SEN2 section if it exists", default=True)

    def execute(self, context):
        from . import import_sklt, bcompile
        import_sklt.readSklt(self.filepath, self.sen2_import)
        return {"FINISHED"}


#Operator for exporting
class SKLTExport(bpy.types.Operator, ExportHelper):

    bl_idname = "fileexport.sklt"
    bl_label = "Export SKLT"

    filename_ext = EnumProperty(name="File extension", items = ((".sklt", ".sklt", "SKLT, use for unit models"), (".skl", ".skl", "SKL, use for HUD")), default=".sklt")
    filter_glob = StringProperty(name="Filename filter", default="*.sklt;*.skl")
    export_mode = EnumProperty(name="Primitive mode", items = ( ("p", "Polygon mode", "Use polygons (for 3D models, recommended"), ("e", "Edge mode", "Use edges, only for HUD, only when there are lines that do not belong to any polygon.") ), default="p", description = "How to handle 3D primitives" )
    sen2_mode = EnumProperty(name="SEN2 mode", items = (("i", "Ignore", "Do not save SEN2 section"), ("s", "Save", "Save existing SEN2 data"), ("a", "Auto-generate", "Auto-generate SEN2 data and save it")), default = "i", description="How to handle SEN2 section")

    def execute(self, context):
        from . import export_sklt
        export_sklt.writeSklt(self.filepath, self.export_mode, self.sen2_mode)
        return {"FINISHED"}





def menu_import(self, context):
    self.layout.operator(SKLTImport.bl_idname, text="Skeleton (.sklt)")

def menu_export(self, context):
    self.layout.operator(SKLTExport.bl_idname, text="Skeleton (.sklt)")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_import)
    bpy.types.INFO_MT_file_export.append(menu_export)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_import)
    bpy.types.INFO_MT_file_export.remove(menu_export)


if __name__ == "__main__":
    register()


#30.8.2013: Added SEN2 import/export options
