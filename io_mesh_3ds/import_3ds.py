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

# <pep8 compliant>

# Script copyright (C) Bob Holcomb
# Contributors: Bob Holcomb, Richard L?rk?ng, Damien McGinnes,
# Campbell Barton, Mario Lapin, Dominique Lorre, Andreas Atteneder

import os
import time
import struct


class FakeMaterial:
    def __init__(self, name):
        self.name = name
        self.texture_slots = self

    def add(self):
        return self


class FakeTexture:
    def __init__(self, name, tex_type):
        self.name = name
        self.texture_type = tex_type


class FakeImage:
    def __init__(self, texture_name, dir_name):
        self.texture_name = texture_name
        self.dir_name = dir_name


class FakeBlenderMesh:
    def __init__(self, ob_name, vertices=None, faces=None, uv_map=None, materials=None):
        self.ob_name = ob_name
        self.tessface_uv_textures = uv_map or []
        self.materials = materials or []
        self.tessfaces = faces or []
        self.vertices = vertices or []
        self.face_to_material_idx = {}

    def validate(self):
        pass

    def update(self):
        pass


######################################################
# Data Structures
######################################################

# Some of the chunks that we will see
# ----- Primary Chunk, at the beginning of each file
PRIMARY = 0x4D4D

# ------ Main Chunks
OBJECTINFO = 0x3D3D  # This gives the version of the mesh and is found right before the material and object information
VERSION = 0x0002  # This gives the version of the .3ds file
EDITKEYFRAME = 0xB000  # This is the header for all of the key frame info

# ------ Data Chunks, used for various attributes
PERCENTAGE_SHORT = 0x30
PERCENTAGE_FLOAT = 0x31

# ------ sub defines of OBJECTINFO
MATERIAL = 0xAFFF  # This stored the texture info
OBJECT = 0x4000  # This stores the faces, vertices, etc...

# >------ sub defines of MATERIAL
# ------ sub defines of MATERIAL_BLOCK
MAT_NAME = 0xA000  # This holds the material name
MAT_AMBIENT = 0xA010  # Ambient color of the object/material
MAT_DIFFUSE = 0xA020  # This holds the color of the object/material
MAT_SPECULAR = 0xA030  # SPecular color of the object/material
MAT_SHINESS = 0xA040  # ??
MAT_TRANSPARENCY = 0xA050  # Transparency value of material
MAT_SELF_ILLUM = 0xA080  # Self Illumination value of material
MAT_WIRE = 0xA085  # Only render's wireframe

MAT_TEXTURE_MAP = 0xA200  # This is a header for a new texture map
MAT_SPECULAR_MAP = 0xA204  # This is a header for a new specular map
MAT_OPACITY_MAP = 0xA210  # This is a header for a new opacity map
MAT_REFLECTION_MAP = 0xA220  # This is a header for a new reflection map
MAT_BUMP_MAP = 0xA230  # This is a header for a new bump map
MAT_MAP_FILEPATH = 0xA300  # This holds the file name of the texture

MAT_MAP_TILING = 0xa351  # 2nd bit (from LSB) is mirror UV flag
MAT_MAP_USCALE = 0xA354  # U axis scaling
MAT_MAP_VSCALE = 0xA356  # V axis scaling
MAT_MAP_UOFFSET = 0xA358  # U axis offset
MAT_MAP_VOFFSET = 0xA35A  # V axis offset
MAT_MAP_ANG = 0xA35C  # UV rotation around the z-axis in rad

MAT_FLOAT_COLOR = 0x0010  # color defined as 3 floats
MAT_24BIT_COLOR = 0x0011  # color defined as 3 bytes

# >------ sub defines of OBJECT
OBJECT_MESH = 0x4100  # This lets us know that we are reading a new object
OBJECT_LAMP = 0x4600  # This lets un know we are reading a light object
OBJECT_LAMP_SPOT = 0x4610  # The light is a spotloght.
OBJECT_LAMP_OFF = 0x4620  # The light off.
OBJECT_LAMP_ATTENUATE = 0x4625
OBJECT_LAMP_RAYSHADE = 0x4627
OBJECT_LAMP_SHADOWED = 0x4630
OBJECT_LAMP_LOCAL_SHADOW = 0x4640
OBJECT_LAMP_LOCAL_SHADOW2 = 0x4641
OBJECT_LAMP_SEE_CONE = 0x4650
OBJECT_LAMP_SPOT_RECTANGULAR = 0x4651
OBJECT_LAMP_SPOT_OVERSHOOT = 0x4652
OBJECT_LAMP_SPOT_PROJECTOR = 0x4653
OBJECT_LAMP_EXCLUDE = 0x4654
OBJECT_LAMP_RANGE = 0x4655
OBJECT_LAMP_ROLL = 0x4656
OBJECT_LAMP_SPOT_ASPECT = 0x4657
OBJECT_LAMP_RAY_BIAS = 0x4658
OBJECT_LAMP_INNER_RANGE = 0x4659
OBJECT_LAMP_OUTER_RANGE = 0x465A
OBJECT_LAMP_MULTIPLIER = 0x465B
OBJECT_LAMP_AMBIENT_LIGHT = 0x4680

OBJECT_CAMERA = 0x4700  # This lets un know we are reading a camera object

# >------ sub defines of CAMERA
OBJECT_CAM_RANGES = 0x4720  # The camera range values

# >------ sub defines of OBJECT_MESH
OBJECT_VERTICES = 0x4110  # The objects vertices
OBJECT_FACES = 0x4120  # The objects faces
OBJECT_MATERIAL = 0x4130  # This is found if the object has a material, either texture map or color
OBJECT_UV = 0x4140  # The UV texture coordinates
OBJECT_TRANS_MATRIX = 0x4160  # The Object Matrix

# >------ sub defines of EDITKEYFRAME
ED_KEY_AMBIENT_NODE = 0xB001
ED_KEY_OBJECT_NODE = 0xB002
ED_KEY_CAMERA_NODE = 0xB003
ED_KEY_TARGET_NODE = 0xB004
ED_KEY_LIGHT_NODE = 0xB005
ED_KEY_L_TARGET_NODE = 0xB006
ED_KEY_SPOTLIGHT_NODE = 0xB007
# >------ sub defines of ED_KEY_OBJECT_NODE
# EK_OB_KEYFRAME_SEG = 0xB008
# EK_OB_KEYFRAME_CURTIME = 0xB009
# EK_OB_KEYFRAME_HEADER = 0xB00A
EK_OB_NODE_HEADER = 0xB010
EK_OB_INSTANCE_NAME = 0xB011
# EK_OB_PRESCALE = 0xB012
EK_OB_PIVOT = 0xB013
# EK_OB_BOUNDBOX =   0xB014
# EK_OB_MORPH_SMOOTH = 0xB015
EK_OB_POSITION_TRACK = 0xB020
EK_OB_ROTATION_TRACK = 0xB021
EK_OB_SCALE_TRACK = 0xB022
# EK_OB_CAMERA_FOV_TRACK = 0xB023
# EK_OB_CAMERA_ROLL_TRACK = 0xB024
# EK_OB_COLOR_TRACK = 0xB025
# EK_OB_MORPH_TRACK = 0xB026
# EK_OB_HOTSPOT_TRACK = 0xB027
# EK_OB_FALLOF_TRACK = 0xB028
# EK_OB_HIDE_TRACK = 0xB029
# EK_OB_NODE_ID = 0xB030

ROOT_OBJECT = 0xFFFF


class Chunk:
    __slots__ = (
        "ID",
        "length",
        "bytes_read",
    )
    # we don't read in the bytes_read, we compute that
    binary_format = "<HI"

    def __init__(self):
        self.ID = 0
        self.length = 0
        self.bytes_read = 0

    def dump(self):
        print('ID: ', self.ID)
        print('ID in hex: ', hex(self.ID))
        print('length: ', self.length)
        print('bytes_read: ', self.bytes_read)


def read_chunk(file, chunk):
    temp_data = file.read(struct.calcsize(chunk.binary_format))
    data = struct.unpack(chunk.binary_format, temp_data)
    chunk.ID = data[0]
    chunk.length = data[1]
    # update the bytes read function
    chunk.bytes_read = 6

    # if debugging
    # chunk.dump()


def read_string(file):
    # read in the characters till we get a null character
    s = []
    while True:
        c = file.read(1)
        if c == b'\x00':
            break
        s.append(c)
        # print('string: ', s)

    # Remove the null character from the string
    # print("read string", s)
    return str(b''.join(s), "utf-8", "replace"), len(s) + 1


######################################################
# IMPORT
######################################################


def process_next_object_chunk(file, previous_chunk):
    new_chunk = Chunk()

    while previous_chunk.bytes_read < previous_chunk.length:
        # read the next chunk
        read_chunk(file, new_chunk)


def skip_to_end(file, skip_chunk):
    buffer_size = skip_chunk.length - skip_chunk.bytes_read
    binary_format = "%ic" % buffer_size
    file.read(struct.calcsize(binary_format))
    skip_chunk.bytes_read += buffer_size


def add_texture_to_material(image, texture, scale, offset, extension, material, mapto):
    print('add_texture_to_material %s to %s' % (texture, material))

    if mapto not in {'COLOR', 'SPECULARITY', 'ALPHA', 'NORMAL'}:
        print(
            "\tError: Cannot map to %r\n\tassuming diffuse color. modify material %r later." %
            (mapto, material.name)
        )
        mapto = "COLOR"

    if image:
        texture.image = image

    mtex = material.texture_slots.add()
    mtex.texture = texture
    mtex.texture_coords = 'UV'
    mtex.use_map_color_diffuse = False

    mtex.scale = (scale[0], scale[1], 1.0)
    mtex.offset = (offset[0], offset[1], 0.0)

    texture.extension = 'REPEAT'
    if extension == 'mirror':
        # 3DS mirror flag can be emulated by these settings (at least so it seems)
        texture.repeat_x = texture.repeat_y = 2
        texture.use_mirror_x = texture.use_mirror_y = True
    elif extension == 'decal':
        # 3DS' decal mode maps best to Blenders CLIP
        texture.extension = 'CLIP'

    if mapto == 'COLOR':
        mtex.use_map_color_diffuse = True
    elif mapto == 'SPECULARITY':
        mtex.use_map_specular = True
    elif mapto == 'ALPHA':
        mtex.use_map_alpha = True
    elif mapto == 'NORMAL':
        mtex.use_map_normal = True


def put_context_mesh(vertls, facels, materials, ob_name, mesh_uv, mat_dict, imported_objects):
    bmesh = FakeBlenderMesh(ob_name)

    if facels is None:
        facels = []

    if vertls:
        bmesh.vertices = vertls

        for v1, v2, v3 in facels:
            bmesh.tessfaces.append([v3, v1, v2] if v3 == 0 else [v1, v2, v3])

        for mat_idx, (matName, faces) in enumerate(materials):
            if matName is None:
                bmat = None
            else:
                bmat = mat_dict.get(matName)
                # in rare cases no materials defined.
                if not bmat:
                    # raise ValueError("Material %r not defined!" % matName)
                    bmat = mat_dict[matName] = FakeMaterial(matName)

            bmesh.materials.append(bmat)  # can be None

            for f_idx in faces:
                bmesh.face_to_material_idx[f_idx] = mat_idx

        if mesh_uv:
            for f_idx, pl in enumerate(bmesh.tessfaces):
                face = facels[f_idx]
                v1, v2, v3 = face

                # eekadoodle
                if v3 == 0:
                    v1, v2, v3 = v3, v1, v2

                bmesh.tessface_uv_textures.append([mesh_uv[v1 * 2: (v1 * 2) + 2],
                                                   mesh_uv[v2 * 2: (v2 * 2) + 2],
                                                   mesh_uv[v3 * 2: (v3 * 2) + 2]
                                                   ])
                # always a tri

    bmesh.validate()
    bmesh.update()

    imported_objects.append(bmesh)


def process_next_chunk(file, previous_chunk, imported_objects):
    context_ob_name = None
    context_material = None
    context_mesh_vertls = None  # flat array: (verts * 3)
    context_mesh_facels = None
    context_mesh_materials = []  # (matname, [face_idxs])
    context_mesh_uv = None  # flat array (verts * 2)

    texture_dict = {}
    matdict = {}

    # Localspace variable names, faster.
    struct_size_float = struct.calcsize('f')
    struct_size_2_float = struct.calcsize('2f')
    struct_size_3_float = struct.calcsize('3f')
    struct_size_4_float = struct.calcsize('4f')
    struct_size_unsigned_short = struct.calcsize('H')
    struct_size_4_unsigned_short = struct.calcsize('4H')
    struct_size_4x3_mat = struct.calcsize('ffffffffffff')
    # only init once
    object_list = []  # for hierarchy
    object_parent = []  # index of parent in hierarchy, 0xFFFF = no parent

    # a spare chunk
    new_chunk = Chunk()
    temp_chunk = Chunk()

    create_blender_object = False

    def read_float_color(temp_chunk):
        temp_data = file.read(struct_size_3_float)
        temp_chunk.bytes_read += struct_size_3_float
        return [float(col) for col in struct.unpack('<3f', temp_data)]

    def read_float(temp_chunk):
        temp_data = file.read(struct_size_float)
        temp_chunk.bytes_read += struct_size_float
        return struct.unpack('<f', temp_data)[0]

    def read_short(temp_chunk):
        temp_data = file.read(struct_size_unsigned_short)
        temp_chunk.bytes_read += struct_size_unsigned_short
        return struct.unpack('<H', temp_data)[0]

    def read_byte_color(temp_chunk):
        temp_data = file.read(struct.calcsize('3B'))
        temp_chunk.bytes_read += 3
        return [float(col) / 255 for col in struct.unpack('<3B', temp_data)]  # data [0,1,2] == rgb

    def read_texture(new_chunk, temp_chunk, name, mapto):
        print("read_texture {}".format(name))
        new_texture = FakeTexture(name, tex_type='IMAGE')

        u_scale, v_scale, u_offset, v_offset = 1.0, 1.0, 0.0, 0.0
        extension = 'wrap'
        while new_chunk.bytes_read < new_chunk.length:
            # print 'MAT_TEXTURE_MAP..while', new_chunk.bytes_read, new_chunk.length
            read_chunk(file, temp_chunk)

            if temp_chunk.ID == MAT_MAP_FILEPATH:
                texture_name, read_str_len = read_string(file)

                img = texture_dict[context_material.name] = FakeImage(texture_name, dir_name)
                print("img = TEXTURE_DICT[{}] {}".format(context_material.name, texture_name))
                temp_chunk.bytes_read += read_str_len  # plus one for the null character that gets removed

            elif temp_chunk.ID == MAT_MAP_USCALE:
                u_scale = read_float(temp_chunk)
            elif temp_chunk.ID == MAT_MAP_VSCALE:
                v_scale = read_float(temp_chunk)

            elif temp_chunk.ID == MAT_MAP_UOFFSET:
                u_offset = read_float(temp_chunk)
            elif temp_chunk.ID == MAT_MAP_VOFFSET:
                v_offset = read_float(temp_chunk)

            elif temp_chunk.ID == MAT_MAP_TILING:
                tiling = read_short(temp_chunk)
                if tiling & 0x2:
                    extension = 'mirror'
                elif tiling & 0x10:
                    extension = 'decal'

            elif temp_chunk.ID == MAT_MAP_ANG:
                print("\nwarning: ignoring UV rotation")

            skip_to_end(file, temp_chunk)
            new_chunk.bytes_read += temp_chunk.bytes_read

        # add the map to the material in the right channel
        if img:
            add_texture_to_material(img, new_texture, (u_scale, v_scale),
                                    (u_offset, v_offset), extension, context_material, mapto)

    dir_name = os.path.dirname(file.name)

    # loop through all the data for this chunk (previous chunk) and see what it is
    while previous_chunk.bytes_read < previous_chunk.length:
        # read the next chunk
        read_chunk(file, new_chunk)

        # is it a Version chunk?
        if new_chunk.ID == VERSION:
            print("new_chunk.ID == VERSION")
            # read in the version of the file
            # it's an unsigned short (H)
            temp_data = file.read(struct.calcsize('I'))
            version = struct.unpack('<I', temp_data)[0]
            new_chunk.bytes_read += 4  # read the 4 bytes for the version number
            # this loader works with version 3 and below, but may not with 4 and above
            if version > 3:
                print('\tNon-Fatal Error:  Version greater than 3, may not load correctly: ', version)

        # is it an object info chunk?
        elif new_chunk.ID == OBJECTINFO:
            print("new_chunk.ID == OBJECTINFO")
            process_next_chunk(file, new_chunk, imported_objects)

            # keep track of how much we read in the main chunk
            new_chunk.bytes_read += temp_chunk.bytes_read

        # is it an object chunk?
        elif new_chunk.ID == OBJECT:
            print("new_chunk.ID == OBJECT")

            if create_blender_object:
                print("CreateBlenderObject is True")
                put_context_mesh(context_mesh_vertls, context_mesh_facels, context_mesh_materials, context_ob_name,
                                 context_mesh_uv, matdict, imported_objects)
                context_mesh_vertls = []
                context_mesh_facels = []

                # preparando para receber o proximo objeto
                context_mesh_materials = []
                context_mesh_uv = None

            create_blender_object = True
            context_ob_name, read_str_len = read_string(file)
            print("contextObName: {}".format(context_ob_name))
            new_chunk.bytes_read += read_str_len

        # is it a material chunk?
        elif new_chunk.ID == MATERIAL:
            print("new_chunk.ID == MATERIAL")

            # 			print("read material")

            context_material = FakeMaterial('Material')

        elif new_chunk.ID == MAT_NAME:
            print("new_chunk.ID == MAT_NAME")
            material_name, read_str_len = read_string(file)
            print("New material name: {}".format(material_name))

            # 			print("material name", material_name)

            # plus one for the null character that ended the string
            new_chunk.bytes_read += read_str_len

            context_material.name = material_name.rstrip()  # remove trailing  whitespace
            matdict[material_name] = context_material
            print("MATDICT[{}] = {}".format(material_name, context_material))

        elif new_chunk.ID == MAT_AMBIENT:
            read_chunk(file, temp_chunk)
            if temp_chunk.ID == MAT_FLOAT_COLOR:
                context_material.mirror_color = read_float_color(temp_chunk)
            elif temp_chunk.ID == MAT_24BIT_COLOR:
                context_material.mirror_color = read_byte_color(temp_chunk)
            else:
                skip_to_end(file, temp_chunk)
            new_chunk.bytes_read += temp_chunk.bytes_read

        elif new_chunk.ID == MAT_DIFFUSE:
            read_chunk(file, temp_chunk)
            if temp_chunk.ID == MAT_FLOAT_COLOR:
                context_material.diffuse_color = read_float_color(temp_chunk)
            elif temp_chunk.ID == MAT_24BIT_COLOR:
                context_material.diffuse_color = read_byte_color(temp_chunk)
            else:
                skip_to_end(file, temp_chunk)

            # 			print("read material diffuse color", contextMaterial.diffuse_color)

            new_chunk.bytes_read += temp_chunk.bytes_read

        elif new_chunk.ID == MAT_SPECULAR:
            read_chunk(file, temp_chunk)
            if temp_chunk.ID == MAT_FLOAT_COLOR:
                context_material.specular_color = read_float_color(temp_chunk)
            elif temp_chunk.ID == MAT_24BIT_COLOR:
                context_material.specular_color = read_byte_color(temp_chunk)
            else:
                skip_to_end(file, temp_chunk)
            new_chunk.bytes_read += temp_chunk.bytes_read

        elif new_chunk.ID == MAT_TEXTURE_MAP:
            print("new_chunk.ID == MAT_TEXTURE_MAP")
            read_texture(new_chunk, temp_chunk, "Diffuse", "COLOR")

        elif new_chunk.ID == OBJECT_MESH:
            print("new_chunk.ID == OBJECT_MESH")
            # print 'Found an OBJECT_MESH chunk'
            pass
        elif new_chunk.ID == OBJECT_VERTICES:
            print("new_chunk.ID == OBJECT_VERTICES")
            """
            Worldspace vertex locations
            """
            temp_data = file.read(struct_size_unsigned_short)
            num_verts = struct.unpack('<H', temp_data)[0]
            new_chunk.bytes_read += 2

            context_mesh_vertls = list(struct.unpack('<%df' % (num_verts * 3), file.read(struct_size_3_float * num_verts)))
            new_chunk.bytes_read += struct_size_3_float * num_verts
            # dummyvert is not used atm!

        elif new_chunk.ID == OBJECT_FACES:
            print("new_chunk.ID == OBJECT_FACES")
            # print 'elif new_chunk.ID == OBJECT_FACES:'
            temp_data = file.read(struct_size_unsigned_short)
            num_faces = struct.unpack('<H', temp_data)[0]
            new_chunk.bytes_read += 2

            temp_data = file.read(struct_size_4_unsigned_short * num_faces)
            new_chunk.bytes_read += struct_size_4_unsigned_short * num_faces  # 4 short ints x 2 bytes each
            context_mesh_facels = struct.unpack('<%dH' % (num_faces * 4), temp_data)
            context_mesh_facels = [context_mesh_facels[i - 3:i] for i in range(3, (num_faces * 4) + 3, 4)]

        elif new_chunk.ID == OBJECT_MATERIAL:
            print("new_chunk.ID == OBJECT_MATERIAL")
            material_name, read_str_len = read_string(file)
            new_chunk.bytes_read += read_str_len  # remove 1 null character.

            temp_data = file.read(struct_size_unsigned_short)
            num_faces_using_mat = struct.unpack('<H', temp_data)[0]
            new_chunk.bytes_read += struct_size_unsigned_short

            temp_data = file.read(struct_size_unsigned_short * num_faces_using_mat)
            new_chunk.bytes_read += struct_size_unsigned_short * num_faces_using_mat

            temp_data = struct.unpack("<%dH" % num_faces_using_mat, temp_data)

            context_mesh_materials.append((material_name, temp_data))

            # look up the material in all the materials

        elif new_chunk.ID == OBJECT_UV:
            print("new_chunk.ID == OBJECT_UV")
            temp_data = file.read(struct_size_unsigned_short)
            num_uv = struct.unpack('<H', temp_data)[0]
            new_chunk.bytes_read += 2

            temp_data = file.read(struct_size_2_float * num_uv)
            new_chunk.bytes_read += struct_size_2_float * num_uv
            context_mesh_uv = list(struct.unpack('<%df' % (num_uv * 2), temp_data))

        else:
            print("unknown chunk: "+hex(new_chunk.ID))
            buffer_size = new_chunk.length - new_chunk.bytes_read
            binary_format = "%ic" % buffer_size
            _ = file.read(struct.calcsize(binary_format))
            new_chunk.bytes_read += buffer_size

        # update the previous chunk bytes read
        previous_chunk.bytes_read += new_chunk.bytes_read

    # FINISHED LOOP
    # There will be a number of objects still not added
    if create_blender_object:
        put_context_mesh(context_mesh_vertls, context_mesh_facels, context_mesh_materials, context_ob_name,
                         context_mesh_uv, matdict, imported_objects)


def load_3ds(filepath):
    imported_objects = []

    print("importing 3DS: %r..." % filepath, end="")

    time1 = time.clock()
    # 	time1 = Blender.sys.time()

    current_chunk = Chunk()

    file = open(filepath, 'rb')

    # here we go!
    # print 'reading the first chunk'
    read_chunk(file, current_chunk)
    if current_chunk.ID != PRIMARY:
        print('\tFatal Error:  Not a valid 3ds file: %r' % filepath)
        file.close()
        return

    process_next_chunk(file, current_chunk, imported_objects)

    print(" done in %.4f sec." % (time.clock() - time1))
    file.close()

    return imported_objects


import glob
#objects = [load_3ds(f) for f in glob.glob("/media/spinnydisk/git/urban_assault_decompiled/output/*.3ds")]

import compile
ST_HYPE = load_3ds("/media/spinnydisk/git/urban_assault_decompiled/output/ST_HYPE.3ds")

# Create top level object
model_name = ST_HYPE[0].ob_name  # TODO Hope that first mesh isn't SEN2
# Set SKLC.NAME.name
o = compile.Objt()
clid = compile.Clid()
sklc = compile.Form(form_type="SKLC")
o.sub_chunks = [clid, sklc]
clid.class_id = "sklt.class"

name = compile.Name()
sklc.sub_chunks = [name]
name.name = "{}.sklt".format(model_name)

# For each Fake Blender Mesh
temp_dict = {}
temp_vertices = []
temp_faces = []
for mesh in ST_HYPE:
    if "sen2" in mesh.ob_name.lower():
        print("Found SEN2 mesh, skipping")  # TODO
        continue
    # For each material in materials
    for material in mesh.materials:
        if material.texture.image.texture_name not in temp_dict:
            temp_dict[material.texture.image.texture_name] = []

    # create vertex list, ensure no duplicates
    for vertex in zip(mesh.vertices[::3], mesh.vertices[1::3], mesh.vertices[2::3]):
        if vertex not in temp_vertices:
            temp_vertices.append(list(vertex))

    for tess_face in mesh.tessfaces:
        temp_face = list(map(lambda j: temp_vertices.index(j), map(lambda i: mesh.vertices[i*3:i*3+3], tess_face)))
        temp_faces.append(temp_face)

    # For each face_to_material_idx
    for poly, material_index in mesh.face_to_material_idx.items():
        uv = [[int(x*255), int(y*255)] for x, y in mesh.tessface_uv_textures[poly]]

        # map mesh.tessfaces[poly] -> index of temp_vertices
        temp_face = list(
            map(lambda j: temp_vertices.index(j), map(lambda i: mesh.vertices[i * 3:i * 3 + 3], mesh.tessfaces[poly]))
        )
        temp_dict[mesh.materials[material_index].texture.image.texture_name].append({"poly": temp_faces.index(temp_face),
                                                                                     "uv": uv})

# Write Skeleton file (POO2/POL2/SEN2)
#  TODO SEN2
poo2 = compile.Poo2()
poo2.set_points_from_list(temp_vertices)
poo2.scale_up(150)
poo2.round_points()
poo2.change_coordinate_system()
pol2 = compile.Pol2()
pol2.edges = temp_faces
sklt = compile.Sklt()
sklt.sub_chunks = [poo2, pol2]
sklt.save_to_json_file(os.path.join(".", "{}.skl.json".format(model_name)))  # TODO USE OUTPUTDIR

# For each poly, uv in temp_dict, append ATTS and OLPL to the correct AMSH form


print("Done")
