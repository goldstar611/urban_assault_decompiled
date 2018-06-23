import base64
import io
import logging
import myjson
import os
import struct

from typing import Union, Tuple


color_table = [4294967040, 4294967295, 4292532954, 4288387995, 4285361517, 4282992969, 4278190081, 4288398800,
               4278203647, 4278190335, 4294901760, 4294945564, 4278245713, 4282795590, 4294967176, 4278225322,
               4278190081, 4294967295, 4289063167, 4285382071, 4284531364, 4284532626, 4288399276, 4284660169,
               4284724444, 4284788975, 4291738328, 4292655531, 4294428045, 4294963045, 4294937927, 4294926689,
               4278190081, 4293848814, 4288338158, 4284854442, 4284069273, 4284070280, 4287674784, 4284198075,
               4284262605, 4284327135, 4290817481, 4291669151, 4293310339, 4293844830, 4293821250, 4293810778,
               4278190081, 4292730333, 4287613405, 4284392350, 4283672718, 4283673726, 4287016085, 4283736238,
               4283800766, 4283865295, 4289896891, 4290683028, 4292258426, 4292726615, 4292704829, 4292695124,
               4278190081, 4291611852, 4286888396, 4283930514, 4283210627, 4283211636, 4286357385, 4283339936,
               4283404463, 4283403455, 4288976044, 4289696904, 4291140976, 4291608400, 4291588152, 4291579213,
               4278190081, 4290493371, 4286163643, 4283402886, 4282814072, 4282814827, 4285632894, 4282877843,
               4282942625, 4283007407, 4288120990, 4288776061, 4290089063, 4290490186, 4290471732, 4290463559,
               4278190081, 4289374890, 4285438634, 4282941050, 4282417517, 4282418273, 4284974194, 4282481542,
               4282546322, 4282545567, 4287200400, 4287789938, 4288971614, 4289371971, 4289355311, 4289347648,
               4278190081, 4288256409, 4284713881, 4282478957, 4281955426, 4281956183, 4284315495, 4282019704,
               4282084483, 4282083727, 4286279553, 4286803814, 4287919700, 4288253756, 4288238634, 4288231994,
               4278190081, 4287137928, 4283988872, 4282016865, 4281558871, 4281559629, 4283591259, 4281623147,
               4281622645, 4281687423, 4285358963, 4285882971, 4286802251, 4287135541, 4287122213, 4287116083,
               4278190081, 4286019447, 4283264119, 4281489493, 4281096780, 4281097284, 4282932304, 4281161309,
               4281226342, 4281225839, 4284503652, 4284896847, 4285750081, 4286017327, 4286005537, 4286000429,
               4278190081, 4284900966, 4282539110, 4281027401, 4280700225, 4280700730, 4282273604, 4280765008,
               4280764503, 4280763999, 4283583062, 4283910724, 4284632632, 4284899112, 4284889116, 4284884518,
               4278190081, 4283782485, 4281814357, 4280565565, 4280303670, 4280304176, 4281549369, 4280302915,
               4280368201, 4280367695, 4282662472, 4282989881, 4283580719, 4283780897, 4283772695, 4283768864,
               4278190081, 4282664004, 4281089348, 4280103472, 4279841579, 4279842086, 4280890669, 4279906613,
               4279906362, 4279905855, 4281741625, 4282003757, 4282463269, 4282662682, 4282656018, 4282652953,
               4278190081, 4281545523, 4280364595, 4279575844, 4279445024, 4279445277, 4280231714, 4279444776,
               4279444523, 4279444271, 4280886571, 4281017634, 4281411356, 4281544468, 4281539598, 4281537299,
               4278190081, 4280427042, 4279639586, 4279114008, 4278982933, 4278983187, 4279507478, 4279048218,
               4279048221, 4279047967, 4279965724, 4280096790, 4280293906, 4280426253, 4280422921, 4280421388,
               4278190081, 4279308561, 4278914833, 4278651916, 4278586378, 4278586633, 4278848779, 4278586381,
               4278586382, 4278586127, 4279045134, 4279110667, 4279241993, 4279308038, 4279306500, 4279305734]


class Chunk(object):
    def __init__(self, chunk_id="?!!?"):
        self.chunk_id = chunk_id
        self.data = bytes("", "ascii")

    @staticmethod
    def validate_id(chunk_id):
        if not isinstance(chunk_id, str):
            raise ValueError("chunk_id must be a string. Supplied type was %s" % type(chunk_id))
        if chunk_id and not len(chunk_id) == 4:
            raise ValueError("length of chunk_id must be 4.")
        return chunk_id

    @staticmethod
    def validate_data(chunk_data):
        if not isinstance(chunk_data, bytes):
            raise ValueError("chunk_data must be bytes. Supplied type was %s" % type(chunk_data))
        return chunk_data

    def set_binary_data(self, binary_data):
        self.data = binary_data

    # Returns only chunk data
    def get_data(self):
        """

        :rtype: bytes
        """
        return self.data

    # Returns chunk_id, size, chunk_data and pad byte
    def full_data(self):
        """

        :rtype: bytes
        """
        data = self.get_data()
        data_length = len(data)
        if len(data) % 2:
            data += b"\x00"
        return bytes(self.chunk_id, "ascii") + struct.pack(">I", data_length) + data

    def size(self):
        """

        :rtype: int
        """
        return len(self.data)

    def load_data_from_file(self, file_name):
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as f:
            data = f.read()
            if data[0:4] == bytes("FORM", "ascii"):
                raise ValueError("You shouldn't load a FORM file into a chunk!")
            self.data = data

        return data

    def load_from_file(self, file_name):
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as f:
            data = f.read()
            if data[0:4] == bytes("FORM", "ascii"):
                raise ValueError("You shouldn't load a FORM file into a chunk!")

            chunk_id = bytes(data[0:4]).decode()
            chunk_size = struct.unpack(">I", data[4:8])[0]
            rest_of_file_data = data[8:]
            if chunk_size <= len(rest_of_file_data):
                self.data = rest_of_file_data[:chunk_size]
                self.chunk_id = chunk_id

            return self

    def save_data_to_file(self, file_name):
        with open(file_name, "wb") as f:
            f.write(self.get_data())

    def save_to_file(self, file_name):
        with open(file_name, "wb") as f:
            f.write(self.full_data())

    def to_json(self):
        if self.chunk_id in master_list:
            o = master_list[self.chunk_id]()
            o.set_binary_data(self.data)
            return myjson.dumps(o.to_json())
        # Generic json support for all IFF chunks
        return myjson.dumps({self.chunk_id: {"data": base64.b64encode(self.data).decode("ascii")}})

    def from_json(self, json_dict):
        self.chunk_id, attributes_dict = json_dict.popitem()
        o = master_list[self.chunk_id]()
        o.from_json_generic({self.chunk_id: attributes_dict})
        self.set_binary_data(o.get_data())
        return self

    def from_json_generic(self, json_string):
        # Generic json support for all IFF chunks
        if isinstance(json_string, str):
            json_dict = myjson.loads(json_string)  # type: dict
        else:
            json_dict = json_string

        self.chunk_id, attributes_dict = json_dict.popitem()
        for k, v in attributes_dict.items():
            setattr(self, k, v)
        return self


class Form(object):
    def __init__(self, form_type="!??!", sub_chunks=None):
        self.form_type = form_type
        if sub_chunks is None:
            self.sub_chunks = []
        else:
            self.sub_chunks = sub_chunks

    @staticmethod
    def validate_form_type(form_type):
        if not isinstance(form_type, str):
            raise ValueError("form_type must be a string. Supplied type was %s" % type(form_type))
        if form_type == "FORM":
            raise ValueError("form_type should not be FORM.")
        if form_type and not len(form_type) == 4:
            raise ValueError("length of form_type must be 4.")
        return form_type

    @staticmethod
    def validate_sub_chunks(sub_chunks):
        if sub_chunks is None:
            return []
        if not isinstance(sub_chunks, list):
            raise ValueError("sub_chunks must be a list. Supplied type was %s" % type(sub_chunks))
        return sub_chunks

    def child(self, child_num):
        """

        :rtype: Union[Form,Chunk]
        """
        return self.sub_chunks[child_num]

    # Returns only form_data
    def get_data(self):
        """

        :rtype: bytes
        """
        form_header = bytes(self.form_type, "ascii")
        form_data = bytes()
        for c in self.sub_chunks:
            form_data += c.full_data()
        return form_header + form_data

    # Returns form_type, size, form_data
    def full_data(self):
        """

        :rtype: bytes
        """
        data = self.get_data()
        data_length = len(data)
        return bytes("FORM", "ascii") + struct.pack(">I", data_length) + data

    def to_json(self):
        # Generic json support for all IFF forms
        children = []
        for child in self.sub_chunks:
            children.append(myjson.loads(child.to_json()))
        ret_string = {self.form_type: children}
        return myjson.dumps(ret_string)

    def from_json(self, json_dict):
        # Generic json support for all IFF forms
        if isinstance(json_dict, str):
            json_dict = myjson.loads(json_dict)

        if isinstance(json_dict, list):
            ret_list = []
            for child in json_dict:
                ret_list.append(self.from_json(child))
            return ret_list

        if isinstance(json_dict, dict):
            for k, v in json_dict.items():
                if isinstance(v, list):
                    return Form(form_type=k, sub_chunks=self.from_json(v))
                if isinstance(v, dict):
                    return Chunk(k).from_json({k: v})
                raise ValueError("not dict or list :(", k, v)

        raise ValueError("Fall through error. This shouldnt happen on well formed data")

    def size(self):
        """

        :rtype: int
        """
        return len(self.get_data())

    def get_all_form_by_type(self, form_type, max_count=9999):
        """

        :rtype: list[Form]
        """
        ret_chunks = []
        for child in self.sub_chunks:
            if isinstance(child, Form):
                if child.form_type == form_type:
                    ret_chunks.append(child)
                if len(ret_chunks) >= max_count:
                    break
                ret_chunks.extend(child.get_all_form_by_type(form_type, max_count - len(ret_chunks)))
        return ret_chunks

    def get_all_chunks_by_id(self, chunk_id, max_count=9999):
        """

        :rtype: list[Chunk]
        """
        ret_chunks = []
        for child in self.sub_chunks:
            if isinstance(child, Chunk) and child.chunk_id == chunk_id:
                ret_chunks.append(child)
                if len(ret_chunks) >= max_count:
                    break
            if isinstance(child, Form):
                ret_chunks.extend(child.get_all_chunks_by_id(chunk_id, max_count - len(ret_chunks)))
        return ret_chunks

    def get_single_form_by_type(self, form_type):
        """

        :rtype: Form
        """
        ret_form = self.get_all_form_by_type(form_type, max_count=1)
        if ret_form:
            return ret_form[0]
        return None

    def get_single_chunk_by_id(self, chunk_id):
        """

        :rtype: Chunk
        """
        ret_chunk = self.get_all_chunks_by_id(chunk_id, max_count=1)
        if ret_chunk:
            return ret_chunk[0]
        return None

    def load_from_file(self, file_name):
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as bas_file:
            parsed_bas = Form().parse_stream(bas_file)[0]
            self.sub_chunks = parsed_bas.sub_chunks
            self.form_type = parsed_bas.form_type

        return self

    def save_to_file(self, file_name):
        with open(file_name, "wb") as f:
            f.write(self.full_data())

    def parse_stream(self, bas_data):
        """

        :rtype: list
        """
        ret_chunks = []
        while True:
            chunk_id = bytes(bas_data.read(4)).decode()
            if not chunk_id:
                break

            if chunk_id == "FORM":
                form_size = struct.unpack(">I", bas_data.read(4))[0] - 4
                form_type = bytes(bas_data.read(4)).decode()
                form_data_stream = io.BytesIO(bas_data.read(form_size))
                #print("Found Form", form_type, form_size)
                ret_chunks.append(Form(form_type=form_type, sub_chunks=self.parse_stream(form_data_stream)))
                continue

            if chunk_id != "FORM":
                chunk_size = struct.unpack(">I", bas_data.read(4))[0]
                chunk_data = bas_data.read(chunk_size)
                if chunk_size % 2:
                    bas_data.read(1)  # Discard pad byte
                #print("Found Chunk", chunk_id, chunk_size)
                c = Chunk(chunk_id)
                c.set_binary_data(chunk_data)
                ret_chunks.append(c)

        return ret_chunks

    def add_chunk(self, chunk):
        self.sub_chunks.append(chunk)


class Name(Chunk):
    def __init__(self, chunk_id="NAME"):
        super(Name, self).__init__(chunk_id)
        self.zero_terminated = False
        self.name = ""

    def set_binary_data(self, binary_data):
        # binary_data = b"Skeleton/DUMMY.sklt\x00"
        # binary_data = b"VPfFLAK2"
        # binary_data = b"joh_mei_2.ade"
        self.zero_terminated = binary_data[-1:] == b"\x00"
        self.name = bytes(binary_data.split(b"\x00")[0]).decode()
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes(self.name, "ascii")
        if self.zero_terminated:
            return ret + b"\x00"
        else:
            return ret

    def to_json(self):
        return {self.chunk_id: {"zero_terminated": self.zero_terminated,
                                "name": self.name
                                }
                }


class Clid(Chunk):
    def __init__(self, chunk_id="CLID"):
        super(Clid, self).__init__(chunk_id)
        self.class_id = ""

    def set_binary_data(self, binary_data):
        # binary_data = b"base.class\x00"
        self.class_id = bytes(binary_data[:-1]).decode()
        assert binary_data == self.get_data()

    def get_data(self):
        return bytes(self.class_id, "ascii") + b"\x00"

    def to_json(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                }
                }


class Emrs(Chunk):
    def __init__(self, chunk_id="EMRS"):
        super(Emrs, self).__init__(chunk_id)
        self.class_id = ""
        self.emrs_name = ""

    def set_binary_data(self, binary_data):
        # binary_data = b"sklt.class\x00Skeleton/S00H.sklt\x00\x00"
        if binary_data:
            temp = binary_data.split(b"\x00")
            self.class_id = bytes(temp[0]).decode()
            self.emrs_name = bytes(temp[1]).decode()
            assert binary_data == self.get_data()

    def get_data(self):
        return bytes(self.class_id, "ascii") + b"\x00" + bytes(self.emrs_name, "ascii") + b"\x00\x00"

    def to_json(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                "emrs_name": self.emrs_name,
                                }
                }


class Nam2(Name):
    def __init__(self, chunk_id="NAM2"):
        super(Nam2, self).__init__(chunk_id)


class Data(Chunk):
    """
    000B                             # class_id_len
    69 6C 62 6D 2E 63 6C 61 73 73 00 # class_id
    000A                             # vbmp_name_len
    46 58 32 2E 49 4C 42 4D 00 00    # vbmp[0] = vbmp_name
    0019                             # len(poly[...])
    0004 19 42 01 42 01 01 19 01     # poly[0] = num_verts + x,y coords
    0004 1E 12 1E 07 26 07 26 12
    0004 18 42 3A 42 3A 01 18 01
    0004 60 01 3A 01 3A 42 60 42
    0004 5C 42 5C 01 82 01 82 42

    0008                             # num frames

    00000050 0000 0000               # frame time + index of vbmp_name + index of poly
    00000028 0000 0001
    00000050 0000 0002
    00000028 0000 0001
    00000050 0000 0003
    00000028 0000 0001
    00000050 0000 0004
    00000FA0 0000 0001

    00
    """

    def __init__(self, chunk_id="DATA"):
        super(Data, self).__init__(chunk_id)
        self.class_id = ""
        self.frames = []

    def set_binary_data(self, binary_data):
        vanm_data = binary_data
        vanm_data_len = len(vanm_data)

        idx = 0
        # Handle the source class ID, it's safer than just stepping +13
        source_class_id_len = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
        idx += 2
        self.class_id = bytes(vanm_data[idx:idx + source_class_id_len].strip(b"\x00")).decode()
        idx += source_class_id_len

        # Get length of VBMP file names (ALL names)
        vbmp_fnames_len = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
        idx += 2

        # Split the names
        vbmp_fnames = bytes(vanm_data[idx:idx + vbmp_fnames_len].strip(b"\x00")).decode().split("\x00")
        idx += vbmp_fnames_len

        num_shorts_for_polygons = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
        idx += 2
        polygons_len = 2 * num_shorts_for_polygons

        # Read all polygons
        vanm_polygons = []
        polygons_start = idx
        while idx < polygons_start + polygons_len:

            # Get number of vertices in this polygon
            temp_num_vertices = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
            idx += 2
            # Read that many vertices
            p = 0
            temp_polygon = []
            while p < temp_num_vertices:
                v = struct.unpack(">BB", vanm_data[
                                         idx:idx + 2])  # Unpack (x,y) pair of unsigned bytes (NOTE: tuple format is fine!)
                temp_polygon.append(list(v))  # Add the pair to the polygon
                p += 1
                idx += 2

            vanm_polygons.append(temp_polygon)  # Now we have a list of ((x1,y1), (x2,y2), (x2,y2)...) sets

        # Read the number of frames
        vanm_num_frames = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
        idx += 2

        # Read and construct all frames
        f = 0
        while f < vanm_num_frames:
            temp_frame_time = struct.unpack(">I", vanm_data[idx:idx + 4])[0]
            temp_frame_file_idx = struct.unpack(">H", vanm_data[idx + 4:idx + 6])[0]
            temp_frame_polygon_idx = struct.unpack(">H", vanm_data[idx + 6:idx + 8])[0]
            idx += 8
            f += 1

            # Build a new frame object - pick VBMP name, coordinates and set duration
            temp_vframe = {"frame_time": temp_frame_time,
                           "vbmp_name": vbmp_fnames[temp_frame_file_idx],
                           "vbmp_coords": vanm_polygons[temp_frame_polygon_idx],
                           }

            self.frames.append(temp_vframe)

        return None

    def get_data(self):
        class_id = self.class_id + "\x00"
        vbmp_names = []
        poly = []
        frame_times = []
        for frame in self.frames:
            poly.append(frame["vbmp_coords"])
            vbmp_names.append(frame["vbmp_name"])
            vbmp_names = list(set(vbmp_names))  # HACK
            frame_times.append([frame["frame_time"],
                                vbmp_names.index(frame["vbmp_name"]),
                                poly.index(frame["vbmp_coords"])])

        vbmp_names_bytes = bytes("\x00".join(vbmp_names), "ascii") + b"\x00\x00"

        poly_bytes = b""
        for pol in poly:
            poly_bytes += struct.pack(">H", len(pol))
            for po in pol:
                for p in po:
                    poly_bytes += struct.pack(">B", p)

        frame_times_bytes = b"".join([struct.pack(">I", x[0]) + struct.pack(">H", x[1]) + struct.pack(">H", x[2]) for x in frame_times])
        a = struct.pack(">H", len(class_id)) + bytes(class_id, "ascii") + struct.pack(">H", len(vbmp_names_bytes)) + vbmp_names_bytes + struct.pack(">H", int(len(poly_bytes) / 2)) + poly_bytes + struct.pack(">H", len(frame_times)) + frame_times_bytes
        return a

    def to_json(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                "frames": self.frames,
                                }
                }


class Head(Chunk):
    def __init__(self, chunk_id="HEAD"):
        super(Head, self).__init__(chunk_id)
        self.width = 0
        self.height = 0
        self.flags = 0

    def set_binary_data(self, binary_data):
        if binary_data:
            width, height, flags = struct.unpack(">HHH", binary_data)
            self.width = width
            self.height = height
            self.flags = flags
            assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">HHH",
                           self.width, self.height, self.flags)

    def to_json(self):
        return {self.chunk_id: {"width": self.width,
                                "height": self.height,
                                "flags": self.flags,
                                }
                }


class Body(Chunk):
    def __init__(self, chunk_id="BODY"):
        super(Body, self).__init__(chunk_id)
        self.file_name = "not_used.vbmp"  # TODO USE THIS
        self.data = bytes()

    def set_binary_data(self, binary_data):
        self.data = binary_data
        assert binary_data == self.get_data()

    def get_data(self):
        return self.data


# https://github.com/Marisa-Chan/UA_source/blob/master/src/amesh.cpp#L262
# Particle.class has its own binary format https://github.com/Marisa-Chan/UA_source/blob/master/src/particle.cpp#L681
class Atts(Chunk):
    def __init__(self, chunk_id="ATTS"):
        super(Atts, self).__init__(chunk_id)
        self.is_ptcl_atts = False
        self.atts_entries = []

    @staticmethod
    def atts_entry(poly_id=0, color_val=0, shade_val=0, tracy_val=0, pad=0):
        return {"poly_id": poly_id,
                "color_val": color_val,
                "shade_val": shade_val,
                "tracy_val": tracy_val,
                "pad": pad,
                }

    def _set_binary_data_particle(self, binary_data):
        self.is_ptcl_atts = True
        (version,
         accel_start_x, accel_start_y, accel_start_z,
         accel_end_x, accel_end_y, accel_end_z,
         magnify_start_x, magnify_start_y, magnify_start_z,
         magnify_end_x, magnify_end_y, magnify_end_z,
         collide, start_speed,
         context_number, context_life_time,
         context_start_gen, context_stop_gen,
         gen_rate, lifetime,
         start_size, end_size, noise) = struct.unpack(">hfffffffffffflllllllllll", binary_data)

        self.version = version
        self.accel_start_x = accel_start_x
        self.accel_start_y = accel_start_y
        self.accel_start_z = accel_start_z
        self.accel_end_x = accel_end_x
        self.accel_end_y = accel_end_y
        self.accel_end_z = accel_end_z
        self.magnify_start_x = magnify_start_x
        self.magnify_start_y = magnify_start_y
        self.magnify_start_z = magnify_start_z
        self.magnify_end_x = magnify_end_x
        self.magnify_end_y = magnify_end_y
        self.magnify_end_z = magnify_end_z
        self.collide = collide
        self.start_speed = start_speed
        self.context_number = context_number
        self.context_life_time = context_life_time
        self.context_start_gen = context_start_gen
        self.context_stop_gen = context_stop_gen
        self.gen_rate = gen_rate
        self.lifetime = lifetime
        self.start_size = start_size
        self.end_size = end_size
        self.noise = noise

    def set_binary_data(self, binary_data):
        if len(binary_data) == 94:
            self._set_binary_data_particle(binary_data)
            assert binary_data[0:len(self.get_data())] == self.get_data()
            return

        if len(binary_data) % 6 != 0:
            logging.error("Atts.convert_binary_data(): Length of binary data was not a multiple of 6! Size: %i" % len(binary_data))

        self.is_ptcl_atts = False
        poly_cnt = int(len(binary_data) / 6)
        atts_entries = []

        for i in range(poly_cnt):
            offset = int(i * 6)

            poly_id, color_val, shade_val, tracy_val, pad = struct.unpack(">hBBBB", binary_data[offset:offset + 6])

            new_atts_entry = self.atts_entry(poly_id, color_val, shade_val, tracy_val, pad)
            atts_entries.append(new_atts_entry)

        self.atts_entries = atts_entries
        assert binary_data[0:len(self.get_data())] == self.get_data()

    def _get_data_particle(self):
        return struct.pack(">hfffffffffffflllllllllll",
                           self.version,
                           self.accel_start_x,
                           self.accel_start_y,
                           self.accel_start_z,
                           self.accel_end_x,
                           self.accel_end_y,
                           self.accel_end_z,
                           self.magnify_start_x,
                           self.magnify_start_y,
                           self.magnify_start_z,
                           self.magnify_end_x,
                           self.magnify_end_y,
                           self.magnify_end_z,
                           self.collide, self.start_speed,
                           self.context_number, self.context_life_time,
                           self.context_start_gen, self.context_stop_gen,
                           self.gen_rate, self.lifetime,
                           self.start_size, self.end_size,
                           self.noise)

    def get_data(self):
        if self.is_ptcl_atts or hasattr(self, "context_life_time"):  # TODO: REMOVE HACK: After all ptcl_atts JSON files are updated with is_ptcl_atts value
            return self._get_data_particle()

        ret = bytes()
        for atts in self.atts_entries:
            ret += struct.pack(">hBBBB",
                               atts["poly_id"],
                               atts["color_val"], atts["shade_val"],
                               atts["tracy_val"], atts["pad"])

        return ret

    def _to_json_particle(self):
        return {self.chunk_id: {"is_particle_atts": self.is_ptcl_atts,
                                "version": self.version,
                                "accel_start_x": self.accel_start_x,
                                "accel_start_y": self.accel_start_y,
                                "accel_start_z": self.accel_start_z,
                                "accel_end_x": self.accel_end_x,
                                "accel_end_y": self.accel_end_y,
                                "accel_end_z": self.accel_end_z,
                                "magnify_start_x": self.magnify_start_x,
                                "magnify_start_y": self.magnify_start_y,
                                "magnify_start_z": self.magnify_start_z,
                                "magnify_end_x": self.magnify_end_x,
                                "magnify_end_y": self.magnify_end_y,
                                "magnify_end_z": self.magnify_end_z,
                                "collide": self.collide,
                                "start_speed": self.start_speed,
                                "context_number": self.context_number,
                                "context_life_time": self.context_life_time,
                                "context_start_gen": self.context_start_gen,
                                "context_stop_gen": self.context_stop_gen,
                                "gen_rate": self.gen_rate,
                                "lifetime": self.lifetime,
                                "start_size": self.start_size,
                                "end_size": self.end_size,
                                "noise": self.noise,
                                }
                }

    def _to_json_generic(self):
        return {self.chunk_id: {"is_particle_atts": self.is_ptcl_atts,
                                "atts_entries": self.atts_entries,
                                }
                }

    def to_json(self):
        if self.is_ptcl_atts:
            return self._to_json_particle()

        return self._to_json_generic()


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L128
class Poo2(Chunk):
    def __init__(self, chunk_id="POO2"):
        super(Poo2, self).__init__(chunk_id)
        self.points = []

    def points_as_list(self):
        return [[point["x"], point["y"], point["z"]] for point in self.points]

    def set_binary_data(self, binary_data):
        if len(binary_data) % 12 != 0:
            logging.error("Poo2.convert_binary_data(): Length of binary data was not a multiple of 12!")

        num = int(len(binary_data) / 12)
        poo2_points = []

        for i in range(num):
            offset = int(i * 12)

            x, y, z = struct.unpack(">fff", binary_data[offset:offset + 12])
            new_poo2_point = {"x": x,
                              "y": y,
                              "z": z}
            poo2_points.append(new_poo2_point)

            self.points = poo2_points
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for point in self.points:
            ret += struct.pack(">fff", point["x"], point["y"], point["z"])

        return ret

    def to_json(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


class Sen2(Poo2):
    def __init__(self, chunk_id="SEN2"):
        super(Sen2, self).__init__(chunk_id)


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L207
class Pol2(Chunk):
    def __init__(self, chunk_id="POL2"):
        super(Pol2, self).__init__(chunk_id)
        self.edges = []

    def set_binary_data(self, binary_data):
        offset = 0
        pol2_edges = []

        pol_count = int(struct.unpack(">I", binary_data[0:4])[0])
        offset += 4

        for i in range(pol_count):
            num_vertex = struct.unpack(">H", binary_data[offset + 0:offset + 2])[0]
            offset += 2
            new_vertex = []
            for j in range(num_vertex):
                new_vertex.append(struct.unpack(">H", binary_data[offset + 0:offset + 2])[0])
                offset += 2
            pol2_edges.append(new_vertex)

        self.edges = pol2_edges
        assert binary_data == self.get_data()

    def get_data(self):
        ret = struct.pack(">I", len(self.edges))
        for pol2 in self.edges:
            ret += struct.pack(">H", len(pol2))
            for coordinate in pol2:
                ret += struct.pack(">H", coordinate)

        return ret

    def to_json(self):
        return {self.chunk_id: {"edges": self.edges,
                                }
                }


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/amesh.cpp#L301
class Olpl(Chunk):
    def __init__(self, chunk_id="OLPL"):
        super(Olpl, self).__init__(chunk_id)
        self.points = []

    def set_binary_data(self, binary_data):
        offset = 0
        olpl_entries = []

        while offset < len(binary_data):
            poly_nums = int(struct.unpack(">H", binary_data[offset + 0:offset + 2])[0])
            offset += 2

            poly = []
            for i in range(poly_nums):
                x, y = struct.unpack(">BB", binary_data[offset + 0:offset + 2])
                offset += 2
                poly.append([x, y])

            olpl_entries.append(poly)

        self.points = olpl_entries
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for olpl_entry in self.points:
            ret += struct.pack(">H", len(olpl_entry))
            for coordinates in olpl_entry:
                ret += struct.pack(">BB", *coordinates)

        return ret

    def to_json(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


class Otl2(Chunk):
    def __init__(self, chunk_id="OTL2"):
        super(Otl2, self).__init__(chunk_id)
        self.points = []

    def set_binary_data(self, binary_data):
        offset = 0
        otl2_count = int(len(binary_data) / 2)

        poly = []
        for i in range(otl2_count):
            x, y = struct.unpack(">BB", binary_data[offset + 0:offset + 2])
            offset += 2
            poly.append([x, y])

        self.points = poly
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for point in self.points:
            ret += struct.pack(">BB", *point)

        return ret

    def to_json(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


class Vbmp(Form):
    def __init__(self, chunk_id="VBMP", sub_chunks=list()):
        super(Vbmp, self).__init__(chunk_id, sub_chunks)

    def load_from_ilbm(self, file_name):
        pass

    def save_to_ilbm(self, file_name):
        pass

    def load_from_bmp(self, file_name):
        pass

    def save_to_bmp(self, file_name):
        pass


class Embd(Form):
    def __init__(self, form_type="EMBD", sub_chunks=list()):
        super(Embd, self).__init__(form_type, [Form("ROOT")] + sub_chunks)
        self.emrs_resources = {}
        self.parse_emrs()

    def parse_emrs(self):
        emrs_name = None
        self.emrs_resources = {}
        for i, chunk in enumerate(self.sub_chunks):
            if i == 0:
                if not isinstance(chunk, Form) and chunk.form_type == "ROOT":
                    raise ValueError("Embd().parse_emrs() expects first sub_chunk to be Form() with type ROOT")
            elif i % 2:
                emrs_name = chunk.emrs_name
            else:
                self.emrs_resources[emrs_name] = chunk

    def emrs_index_by_name(self, emrs_name):
        if not self.emrs_resources:
            self.parse_emrs()

        if emrs_name not in self.emrs_resources:
            return None

        return self.sub_chunks.index(self.emrs_resources[emrs_name])

    def add_emrs_resource(self, class_id, emrs_name, incoming_form):
        emrs_chunk = Emrs().from_json({"class_id": class_id,
                                       "emrs_name": emrs_name
                                       })
        self.add_chunk(emrs_chunk)
        self.add_chunk(incoming_form)
        self.parse_emrs()

    def add_sklt(self, file_name, sklt_form):
        # if not isinstance(sklt_form, Sklt)
        self.add_emrs_resource("sklt.class", file_name, sklt_form)

    def add_vbmp(self, file_name, vbmp_form):
        if not isinstance(vbmp_form, Vbmp):
            logging.warning("Adding non-vbmp instance to Embd!")
        self.add_emrs_resource("ilbm.class", file_name, vbmp_form)

    def add_vanm(self, file_name, vanm_form):
        self.add_emrs_resource("bmpanim.class", file_name, vanm_form)

    def extract_resources(self, output_location):
        print("extracting resources")

        if not os.path.isdir(output_location):
            os.mkdir(output_location)

        asset_name = None
        for i, chunk in enumerate(self.sub_chunks):  # type: Tuple[int, Union[Chunk, Form]]
            if i == 0:
                if not isinstance(chunk, Form) and chunk.form_type == "ROOT":
                    raise ValueError("Embd().extract_resources() expects first sub_chunk to be Form() with type ROOT")
            elif i % 2:
                # EMRS
                asset_name = chunk.emrs_name
            else:
                # Asset
                if chunk.form_type == "VBMP":
                    from PyQt5 import QtGui
                    data = chunk.get_single_chunk_by_id("BODY").get_data()

                    mirror_horizontal = True
                    mirror_vertical = False
                    image = QtGui.QImage(data, 256, 256, QtGui.QImage.Format_Indexed8)
                    image = image.mirrored(mirror_horizontal, mirror_vertical)
                    image.setColorTable(color_table)
                    image.save(os.path.join(output_location, "%s.bmp" % asset_name))
                elif chunk.form_type == "SKLT" or chunk.form_type == "VANM":
                    # TODO: Using the base name is not really compatible with MC2 forms which
                    # TODO:   expect the file name to be Skeleton/blah.sklt
                    base_name = os.path.basename(asset_name)
                    with open(os.path.join(output_location, base_name + ".json"), "w") as f:
                        f.write(chunk.to_json())
                else:
                    raise ValueError("extract_resources() unimplemented for %s", chunk.form_type)


class Mc2(Form):
    def __init__(self, form_type="MC2 "):
        super(Mc2, self).__init__(form_type)
        self.embd = Embd()
        self.vehicles = Form("KIDS")
        self.buildings = Form("KIDS")
        self.ground = Form("KIDS")

        # Add convenience functions
        self.add_sklt = self.embd.add_sklt
        self.add_vbmp = self.embd.add_vbmp
        self.add_vanm = self.embd.add_vanm


class Strc(Chunk):
    STRC_ADE = "STRC_ADE "
    STRC_AREA = "STRC_AREA"
    STRC_BANI = "STRC_BANI"
    STRC_BASE = "STRC_BASE"
    STRC_UNKNOWN = "STRC_UNKNOWN"

    def __init__(self, chunk_id="STRC"):
        super(Strc, self).__init__(chunk_id)
        # BASE STRC
        self.strc_type = Strc.STRC_BASE
        self.version = 0
        self.pos = [0.0, 0.0, 0.0]
        self.vec = [0.0, 0.0, 0.0]
        self.scale = [0.0, 0.0, 0.0]
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.att_flags = 0
        self._un1 = 0
        self.vis_limit = 0
        self.ambient_light = 0
        # ADE STRC
        self.strc_type = Strc.STRC_ADE
        self.version = 0
        self._nul = 0
        self.flags = 0
        self.point = 0
        self.poly = 0
        self._nu2 = 0
        # AREA STRC
        self.strc_type = Strc.STRC_AREA
        self.version = 0
        self.flags = 0
        self.polFlags = 0
        self._un1 = 0
        self.clrVal = 0
        self.trcVal = 0
        self.shdVal = 0
        # BANI STRC
        self.strc_type = Strc.STRC_BANI
        self.version = 0
        self.offset = 0
        self.anim_type = 0
        self.anim_name = ""
        # GENERIC STRC
        self.strc_type = Strc.STRC_UNKNOWN

    def set_binary_data(self, binary_data):
        if len(binary_data) == 62:
            # BASE STRC
            return self._set_binary_data_base(binary_data)
        if len(binary_data) == 10:
            version = struct.unpack(">h", binary_data[0:2])[0]
            if version == 1:
                # ADE STRC
                return self._set_binary_data_ade(binary_data)
            if version == 256:
                # AREA STRC
                return self._set_binary_data_area(binary_data)
            raise ValueError("strc_factory() received invalid data:", binary_data)
        if binary_data[0:5] == b"\x00\x01\x00\x06\x00":
            # BANI STRC
            return self._set_binary_data_bani(binary_data)

        raise ValueError("Strc().set_data() received invalid data: %s" % binary_data)

    def get_data(self):
        if self.strc_type == Strc.STRC_BASE:
            return self._get_data_base()
        if self.strc_type == Strc.STRC_ADE:
            return self._get_data_ade()
        if self.strc_type == Strc.STRC_AREA:
            return self._get_data_area()
        if self.strc_type == Strc.STRC_BANI:
            return self._get_data_bani()

        raise ValueError("Can't get_data() from strc_type STRC_UNKNOWN!!")

    def _set_binary_data_base(self, binary_data):
        if len(binary_data) != 62:
            raise ValueError("Length of binary_data was not 62 bytes! Not valid for STRC_BASE objects!")
        # int16_t version;
        # xyz pos;
        # xyz vec;
        # xyz scale;
        # int16_t ax;
        # int16_t ay;
        # int16_t az;
        # int16_t rx;
        # int16_t ry;
        # int16_t rz;
        # int16_t attFlags;
        # int16_t _un1;
        # int32_t visLimit;
        # int32_t ambientLight;
        unpacked_data = struct.unpack(">hfffffffffhhhhhhhhll", binary_data)
        self.version = unpacked_data[0]
        self.pos = [unpacked_data[1], unpacked_data[2], unpacked_data[3]]
        self.vec = [unpacked_data[4], unpacked_data[5], unpacked_data[6]]
        self.scale = [unpacked_data[7], unpacked_data[8], unpacked_data[9]]
        self.ax = unpacked_data[10]
        self.ay = unpacked_data[11]
        self.az = unpacked_data[12]
        self.rx = unpacked_data[13]
        self.ry = unpacked_data[14]
        self.rz = unpacked_data[15]
        self.att_flags = unpacked_data[16]
        self._un1 = unpacked_data[17]
        self.vis_limit = unpacked_data[18]
        self.ambient_light = unpacked_data[19]
        self.strc_type = "STRC_BASE"
        assert binary_data == self.get_data()

    def _get_data_base(self):
        return struct.pack(">hfffffffffhhhhhhhhll",
                           self.version,
                           *self.pos, *self.vec, *self.scale,
                           self.ax, self.ay, self.az,
                           self.rx, self.ry, self.rz,
                           self.att_flags, self._un1,
                           self.vis_limit, self.ambient_light)

    def _set_binary_data_ade(self, binary_data):
        version = struct.unpack(">h", binary_data[0:2])[0]
        if len(binary_data) != 10:
            raise ValueError("Length of binary_data was not 10 bytes! Not valid for STRC_ADE objects!")
        if version != 1:
            raise ValueError("Version of binary_data was not 1! Not valid for STRC_ADE objects!")
        # int16_t version;
        # int8_t _nu1; // Not used
        # int8_t flags;
        # int16_t point;
        # int16_t poly;
        # int16_t _nu2; // Not used
        unpacked_data = struct.unpack(">hbbhhh", binary_data)
        self.version = unpacked_data[0]
        self._nul = unpacked_data[1]
        self.flags = unpacked_data[2]
        self.point = unpacked_data[3]
        self.poly = unpacked_data[4]
        self._nu2 = unpacked_data[5]
        self.strc_type = "STRC_ADE "
        assert binary_data == self.get_data()

    def _get_data_ade(self):
        return struct.pack(">hbbhhh",
                           self.version,
                           self._nul, self.flags,
                           self.point, self.poly, self._nu2)

    def _set_binary_data_area(self, binary_data):
        version = struct.unpack(">h", binary_data[0:2])[0]
        if len(binary_data) != 10:
            raise ValueError("Length of binary_data was not 10 bytes! Not valid for STRC_AREA objects!")
        if version != 256:
            raise ValueError("Version of binary_data was not 256! Not valid for STRC_AREA objects!")
        # int16_t version;
        # uint16_t flags;
        # uint16_t polFlags;
        # uint8_t _un1;
        # uint8_t clrVal;
        # uint8_t trcVal;
        # uint8_t shdVal;
        unpacked_data = struct.unpack(">hHHBBBB", binary_data)
        self.version = unpacked_data[0]
        self.flags = unpacked_data[1]
        self.polFlags = unpacked_data[2]
        self._un1 = unpacked_data[3]
        self.clrVal = unpacked_data[4]
        self.trcVal = unpacked_data[5]
        self.shdVal = unpacked_data[6]
        self.strc_type = "STRC_AREA"
        assert binary_data == self.get_data()

    def _get_data_area(self):
        return struct.pack(">hHHBBBB",
                           self.version,
                           self.flags, self.polFlags,
                           self._un1, self.clrVal,
                           self.trcVal, self.shdVal)

    def _set_binary_data_bani(self, binary_data):
        version, offset, anim_type = struct.unpack(">hhh", binary_data[0:6])
        self.version = version
        self.offset = offset
        self.anim_type = anim_type
        self.anim_name = bytes(binary_data[6:-1]).decode()
        self.strc_type = "STRC_BANI"
        assert binary_data == self.get_data()

    def _get_data_bani(self):
        return struct.pack(">hhh",
                           self.version,
                           self.offset,
                           self.anim_type) + bytes(self.anim_name, "ascii") + b"\x00"

    def to_json(self):
        if self.strc_type == Strc.STRC_BASE:
            return {self.chunk_id: {"strc_type": self.strc_type,
                                    "version": self.version,
                                    "pos": self.pos,
                                    "vec": self.vec,
                                    "scale": self.scale,
                                    "ax": self.ax,
                                    "ay": self.ay,
                                    "az": self.az,
                                    "rx": self.rx,
                                    "ry": self.ry,
                                    "rz": self.rz,
                                    "att_flags": self.att_flags,
                                    "_un1": self._un1,
                                    "vis_limit": self.vis_limit,
                                    "ambient_light": self.ambient_light,
                                }
                }
        if self.strc_type == Strc.STRC_ADE:
            return {self.chunk_id: {"strc_type": self.strc_type,
                                    "version": self.version,
                                    "_nul": self._nul,
                                    "flags": self.flags,
                                    "point": self.point,
                                    "poly": self.poly,
                                    "_nu2": self._nu2,
                                }
                }
        if self.strc_type == Strc.STRC_AREA:
            return {self.chunk_id: {"strc_type": self.strc_type,
                                    "version": self.version,
                                    "flags": self.flags,
                                    "polFlags": self.polFlags,
                                    "_un1": self._un1,
                                    "clrVal": self.clrVal,
                                    "trcVal": self.trcVal,
                                    "shdVal": self.shdVal,
                                }
                }
        if self.strc_type == Strc.STRC_BANI:
            return {self.chunk_id: {"strc_type": self.strc_type,
                                    "version": self.version,
                                    "offset": self.offset,
                                    "anim_type": self.anim_type,
                                    "anim_name": self.anim_name,
                                    }
                    }

        raise ValueError("STRC().to_json() Can't get json for unknown STRC!")


master_list = {
    "ADE ": Form,
    "ADES": Form,
    "AMSH": Form,
    "AREA": Form,
    "BANI": Form,
    "BASE": Form,
    "CIBO": Form,
    "EMBD": Embd,
    "KIDS": Form,
    "MC2 ": Mc2,
    "OBJT": Form,
    "PTCL": Form,
    "ROOT": Form,
    "SKLC": Form,
    "SKLT": Form,
    "VANM": Form,
    "VBMP": Vbmp,
    "ATTS": Atts,
    "BODY": Body,
    "CLID": Clid,
    "DATA": Data,
    "EMRS": Emrs,
    "HEAD": Head,
    "NAM2": Nam2,
    "NAME": Name,
    "OLPL": Olpl,
    "OTL2": Otl2,
    "POL2": Pol2,
    "POO2": Poo2,
    "SEN2": Sen2,
    "STRC": Strc,
}


import glob

#for bas_file in glob.glob("/home/user/Desktop/urban_assault_decompiled/set1/**/*.bas", recursive=True):
#    f = Form().load_from_file(bas_file)
#    print(f.to_json())

for json_file in glob.glob("/home/user/Desktop/urban_assault_decompiled/set1/**/*.json", recursive=True):
    f = Form().from_json(open(json_file, "rt").read())
    with open(json_file.replace(".json", ""), "rb") as a:
        b = a.read()
        print(json_file)
        print(b)
        print(f.full_data())
        assert b == f.full_data()