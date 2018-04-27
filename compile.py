import io
import logging
import myjson
import os
import struct
import warnings

from typing import Union


class ConversionClass(object):
    pass


class Chunk(object):
    def __init__(self, chunk_id=str(), chunk_data=bytes()):
        self.chunk_id = self.validate_id(chunk_id)
        self.chunk_data = self.validate_data(chunk_data)
        self.conversion_class = ConversionClass()

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

    # Returns only chunk data
    def get_data(self):
        """

        :rtype: bytes
        """
        return self.chunk_data

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
        return len(self.chunk_data)

    def load_data_from_file(self, file_name):
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as f:
            data = f.read()
            if data[0:4] == bytes("FORM", "ascii"):
                raise ValueError("You shouldn't load a FORM file into a chunk!")
            self.chunk_data = data

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
                self.chunk_data = rest_of_file_data[:chunk_size]
                self.chunk_id = chunk_id

            return self

    def save_data_to_file(self, file_name):
        with open(file_name, "wb") as f:
            f.write(self.get_data())

    def save_to_file(self, file_name):
        with open(file_name, "wb") as f:
            f.write(self.full_data())

    def to_json(self):
        # return myjson.dumps({self.chunk_id: self.conversion_class.__dict__}, sort_keys=True)
        try:
            return myjson.dumps({self.chunk_id: self.conversion_class.__dict__})
        except TypeError:
            return myjson.dumps({self.chunk_id: {"TypeError": "Cannot Deocde Data"}})

    def from_json(self, json_dict):
        self.conversion_class.__dict__ = json_dict
        return self


class Form(object):
    def __init__(self, form_type: str="", sub_chunks: list=None):
        self.form_type = self.validate_form_type(form_type)
        self.sub_chunks = self.validate_sub_chunks(sub_chunks)

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
        children = []
        for child in self.sub_chunks:
            children.append(myjson.loads(child.to_json()))
        ret_string = {self.form_type: children}
        return myjson.dumps(ret_string, indent=1, sort_keys=True)

    def from_json(self, json_dict):
        if isinstance(json_dict, str):
            json_dict = myjson.loads(json_dict)

        if isinstance(json_dict, list):
            ret_list = []
            for child in json_dict:
                # print(child)
                ret_list.append(self.from_json(child))
            return ret_list

        if isinstance(json_dict, dict):
            for k, v in json_dict.items():
                if isinstance(v, list):
                    return Form(k, self.from_json(v))
                if isinstance(v, dict):
                    # return Chunk(k).from_json(v)
                    return all_ua_python_objects[k]().from_json(v)
                raise ValueError("not dict or list :(", k, v)

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
                print("Found Form", form_type, form_size)
                ret_chunks.append(Form(form_type, self.parse_stream(form_data_stream)))
                continue

            if chunk_id != "FORM":
                chunk_size = struct.unpack(">I", bas_data.read(4))[0]
                chunk_data = bas_data.read(chunk_size)
                if chunk_size % 2:
                    bas_data.read(1)  # Discard pad byte
                print("Found Chunk", chunk_id, chunk_size)
                a = all_ua_python_objects.get(chunk_id, Chunk)
                ret_chunks.append(a(data=chunk_data))

        return ret_chunks

    def add_chunk(self, chunk):
        self.sub_chunks.append(chunk)


class Clid(Chunk):
    def __init__(self, data=bytes()):
        super(Clid, self).__init__("CLID", data)
        self.conversion_class.class_id = ""
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        # binary_data = b"base.class\x00"
        self.conversion_class.class_id = bytes(binary_data[:-1]).decode()
        assert binary_data == self.get_data()

    def get_data(self):
        return bytes(self.conversion_class.class_id, "ascii") + b"\x00"


class Name(Chunk):
    def __init__(self, data=bytes()):
        super(Name, self).__init__("NAME", data)
        self.conversion_class.zero_terminated = False
        self.conversion_class.name = ""
        self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        # binary_data = b"Skeleton/DUMMY.sklt\x00"
        # binary_data = b"VPfFLAK2"
        # binary_data = b"joh_mei_2.ade"
        self.conversion_class.zero_terminated = binary_data[-1:] == b"\x00"
        self.conversion_class.name = bytes(binary_data.split(b"\x00")[0]).decode()
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes(self.conversion_class.name, "ascii")
        if self.conversion_class.zero_terminated:
            return ret + b"\x00"
        else:
            return ret


class Emrs(Chunk):
    def __init__(self, data=bytes()):
        super(Emrs, self).__init__("EMRS", data)
        self.conversion_class.class_id = ""
        self.conversion_class.emrs_name = ""
        self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        # binary_data = b"sklt.class\x00Skeleton/S00H.sklt\x00\x00"
        if binary_data:
            temp = binary_data.split(b"\x00")
            self.conversion_class.class_id = bytes(temp[0]).decode()
            self.conversion_class.emrs_name = bytes(temp[1]).decode()
            assert binary_data == self.get_data()

    def get_data(self):
        return bytes(self.conversion_class.class_id, "ascii") + b"\x00" + bytes(self.conversion_class.emrs_name, "ascii") + b"\x00\x00"


class Strc(Chunk):
    def __init__(self, data=bytes()):
        super(Strc, self).__init__("STRC", data)
        self.conversion_class.strc_type = "STRC_UNKNOWN"

    def set_text_data(self, text_data):
        print(text_data)
        json_data = myjson.loads(text_data)
        if "strc_type" in json_data:
            strc = Strc()
            strc_type = json_data["strc_type"]

            if "STRC_UNKNOWN" == strc_type:
                return None
            if "STRC_BASE" == strc_type:
                strc = BaseStrc()
            if "STRC_ADE " == strc_type:
                strc = AdeStrc()
            if "STRC_AREA" == strc_type:
                strc = AreaStrc()
            if "STRC_BANI" == strc_type:
                strc = BaniStrc()

            strc.from_json(myjson.loads(text_data))
            self.conversion_class.__dict__ = strc.conversion_class__dict__

    def get_data(self):
        if "strc_type" in self.conversion_class.__dict__:
            strc = Strc()
            if self.conversion_class.__dict__["strc_type"] == "STRC_UNKNOWN":
                return bytes()
            if self.conversion_class.__dict__["strc_type"] == "STRC_BASE":
                strc = BaseStrc()
            if self.conversion_class.__dict__["strc_type"] == "STRC_ADE ":
                strc = AdeStrc()
            if self.conversion_class.__dict__["strc_type"] == "STRC_AREA":
                strc = AreaStrc()
            if self.conversion_class.__dict__["strc_type"] == "STRC_BANI":
                strc = BaniStrc()

            a = self.to_json()
            b = myjson.loads(a)["STRC"]  # HACK HACK
            strc.from_json(b)
            return strc.get_data()


class BaseStrc(Chunk):
    def __init__(self, data=bytes()):
        super(BaseStrc, self).__init__("STRC", data)
        self.conversion_class.strc_type = "STRC_BASE"
        self.conversion_class.version = 0
        self.conversion_class.pos = [0.0, 0.0, 0.0]
        self.conversion_class.vec = [0.0, 0.0, 0.0]
        self.conversion_class.scale = [0.0, 0.0, 0.0]
        self.conversion_class.ax = 0
        self.conversion_class.ay = 0
        self.conversion_class.az = 0
        self.conversion_class.rx = 0
        self.conversion_class.ry = 0
        self.conversion_class.rz = 0
        self.conversion_class.att_flags = 0
        self.conversion_class._un1 = 0
        self.conversion_class.vis_limit = 0
        self.conversion_class.ambient_light = 0
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
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
        self.conversion_class.version = unpacked_data[0]
        self.conversion_class.pos = [unpacked_data[1], unpacked_data[2], unpacked_data[3]]
        self.conversion_class.vec = [unpacked_data[4], unpacked_data[5], unpacked_data[6]]
        self.conversion_class.scale = [unpacked_data[7], unpacked_data[8], unpacked_data[9]]
        self.conversion_class.ax = unpacked_data[10]
        self.conversion_class.ay = unpacked_data[11]
        self.conversion_class.az = unpacked_data[12]
        self.conversion_class.rx = unpacked_data[13]
        self.conversion_class.ry = unpacked_data[14]
        self.conversion_class.rz = unpacked_data[15]
        self.conversion_class.att_flags = unpacked_data[16]
        self.conversion_class._un1 = unpacked_data[17]
        self.conversion_class.vis_limit = unpacked_data[18]
        self.conversion_class.ambient_light = unpacked_data[19]
        assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">hfffffffffhhhhhhhhll",
                           self.conversion_class.version,
                           *self.conversion_class.pos, *self.conversion_class.vec, *self.conversion_class.scale,
                           self.conversion_class.ax, self.conversion_class.ay, self.conversion_class.az,
                           self.conversion_class.rx, self.conversion_class.ry, self.conversion_class.rz,
                           self.conversion_class.att_flags, self.conversion_class._un1,
                           self.conversion_class.vis_limit, self.conversion_class.ambient_light)


class AdeStrc(Chunk):
    def __init__(self, data=bytes()):
        super(AdeStrc, self).__init__("STRC", data)
        self.conversion_class.strc_type = "STRC_ADE "
        self.conversion_class.version = 0
        self.conversion_class._nul = 0
        self.conversion_class.flags = 0
        self.conversion_class.point = 0
        self.conversion_class.poly = 0
        self.conversion_class._nu2 = 0
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        version = struct.unpack(">h", binary_data[0:2])[0]
        if len(binary_data) != 10:
            raise ValueError("Length of binary_data was not 10 bytes! Not valid for STRC_ADE  objects!")
        if version != 1:
            raise ValueError("Version of binary_data was not 1! Not valid for STRC_ADE  objects!")
        # int16_t version;
        # int8_t _nu1; // Not used
        # int8_t flags;
        # int16_t point;
        # int16_t poly;
        # int16_t _nu2; // Not used
        unpacked_data = struct.unpack(">hbbhhh", binary_data)
        self.conversion_class.version = unpacked_data[0]
        self.conversion_class._nul = unpacked_data[1]
        self.conversion_class.flags = unpacked_data[2]
        self.conversion_class.point = unpacked_data[3]
        self.conversion_class.poly = unpacked_data[4]
        self.conversion_class._nu2 = unpacked_data[5]
        assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">hbbhhh",
                           self.conversion_class.version,
                           self.conversion_class._nul, self.conversion_class.flags,
                           self.conversion_class.point, self.conversion_class.poly, self.conversion_class._nu2)


class AreaStrc(Chunk):
    def __init__(self, data=bytes()):
        super(AreaStrc, self).__init__("STRC", data)
        self.conversion_class.strc_type = "STRC_AREA"
        self.conversion_class.version = 0
        self.conversion_class.flags = 0
        self.conversion_class.polFlags = 0
        self.conversion_class._un1 = 0
        self.conversion_class.clrVal = 0
        self.conversion_class.trcVal = 0
        self.conversion_class.shdVal = 0
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
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
        self.conversion_class.version = unpacked_data[0]
        self.conversion_class.flags = unpacked_data[1]
        self.conversion_class.polFlags = unpacked_data[2]
        self.conversion_class._un1 = unpacked_data[3]
        self.conversion_class.clrVal = unpacked_data[4]
        self.conversion_class.trcVal = unpacked_data[5]
        self.conversion_class.shdVal = unpacked_data[6]
        assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">hHHBBBB",
                           self.conversion_class.version,
                           self.conversion_class.flags, self.conversion_class.polFlags,
                           self.conversion_class._un1, self.conversion_class.clrVal,
                           self.conversion_class.trcVal, self.conversion_class.shdVal)


class BaniStrc(Chunk):
    def __init__(self, data=bytes()):
        super(BaniStrc, self).__init__("STRC", data)
        self.conversion_class.strc_type = "STRC_BANI"
        self.conversion_class.version = 0
        self.conversion_class.offset = 0
        self.conversion_class.anim_type = 0
        self.conversion_class.anim_name = ""
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        version, offset, anim_type = struct.unpack(">hhh", binary_data[0:6])
        self.conversion_class.version = version
        self.conversion_class.offset = offset
        self.conversion_class.anim_type = anim_type
        self.conversion_class.anim_name = bytes(binary_data[6:-1]).decode()
        assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">hhh",
                           self.conversion_class.version,
                           self.conversion_class.offset,
                           self.conversion_class.anim_type) + bytes(self.conversion_class.anim_name, "ascii") + b"\x00"


def strc_factory(data=bytes()):
    binary_data = data
    if not binary_data:
        return Strc(data)
    if len(binary_data) == 62:
        return BaseStrc(data)
    if len(binary_data) == 10:
        version = struct.unpack(">h", binary_data[0:2])[0]
        if version == 1:
            return AdeStrc(data)
        if version == 256:
            return AreaStrc(data)
        raise ValueError("strc_factory() received invalid data:", binary_data)
    if binary_data[0:5] == b"\x00\x01\x00\x06\x00":
        return BaniStrc(data)

    warnings.warn("strc_factory() received invalid data: %s" % binary_data)
    return Strc(data)


class Nam2(Name):
    def __init__(self, data=bytes()):
        super(Nam2, self).__init__(data)
        self.chunk_id = "NAM2"
        self.conversion_class.zero_terminated = False
        self.conversion_class.name = ""
        self.set_binary_data(data)


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

    def __init__(self, data=bytes()):
        super(Data, self).__init__("DATA", data)
        self.conversion_class.class_id = ""
        self.conversion_class.frames = []
        if data:
            self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        vanm_data = binary_data
        vanm_data_len = len(vanm_data)

        idx = 0
        # Handle the source class ID, it's safer than just stepping +13
        source_class_id_len = struct.unpack(">H", vanm_data[idx:idx + 2])[0]
        idx += 2
        self.conversion_class.class_id = bytes(vanm_data[idx:idx + source_class_id_len].strip(b"\x00")).decode()
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

            self.conversion_class.frames.append(temp_vframe)

        return None

    def get_data(self):
        class_id = self.conversion_class.class_id + "\x00"
        vbmp_names = []
        poly = []
        frame_times = []
        for frame in self.conversion_class.frames:
            print(frame)
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


class Head(Chunk):
    def __init__(self, data=bytes()):
        super(Head, self).__init__("HEAD", data)
        self.conversion_class.width = 0
        self.conversion_class.height = 0
        self.conversion_class.flags = 0
        self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        if binary_data:
            width, height, flags = struct.unpack(">HHH", binary_data)
            self.conversion_class.width = width
            self.conversion_class.height = height
            self.conversion_class.flags = flags
            assert binary_data == self.get_data()

    def get_data(self):
        return struct.pack(">HHH",
                           self.conversion_class.width, self.conversion_class.height, self.conversion_class.flags)


class Body(Chunk):
    def __init__(self, data=bytes()):
        super(Body, self).__init__("BODY", data)
        self.conversion_class.file_name = "not_used.vbmp"
        self.data = bytes()
        self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        self.data = binary_data
        assert binary_data == self.get_data()

    def get_data(self):
        return self.data


# https://github.com/Marisa-Chan/UA_source/blob/master/src/amesh.cpp#L262
# Particle.class has its own binary format https://github.com/Marisa-Chan/UA_source/blob/master/src/particle.cpp#L681
class Atts(Chunk):
    def __init__(self, data=bytes()):
        super(Atts, self).__init__("ATTS", data)
        self.conversion_class.atts_entries = []
        self.set_binary_data(data)

    @staticmethod
    def atts_entry(poly_id=0, color_val=0, shade_val=0, tracy_val=0, pad=0):
        return {"poly_id": poly_id,
                "color_val": color_val,
                "shade_val": shade_val,
                "tracy_val": tracy_val,
                "pad": pad,
                }

    def _set_binary_data_particle(self, binary_data):
        if hasattr(self.conversion_class, "atts_entries"):  # HACK
            del self.conversion_class.atts_entries
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

        self.conversion_class.version = version
        self.conversion_class.accel_start_x = accel_start_x
        self.conversion_class.accel_start_y = accel_start_y
        self.conversion_class.accel_start_z = accel_start_z
        self.conversion_class.accel_end_x = accel_end_x
        self.conversion_class.accel_end_y = accel_end_y
        self.conversion_class.accel_end_z = accel_end_z
        self.conversion_class.magnify_start_x = magnify_start_x
        self.conversion_class.magnify_start_y = magnify_start_y
        self.conversion_class.magnify_start_z = magnify_start_z
        self.conversion_class.magnify_end_x = magnify_end_x
        self.conversion_class.magnify_end_y = magnify_end_y
        self.conversion_class.magnify_end_z = magnify_end_z
        self.conversion_class.collide = collide
        self.conversion_class.start_speed = start_speed
        self.conversion_class.context_number = context_number
        self.conversion_class.context_life_time = context_life_time
        self.conversion_class.context_start_gen = context_start_gen
        self.conversion_class.context_stop_gen = context_stop_gen
        self.conversion_class.gen_rate = gen_rate
        self.conversion_class.lifetime = lifetime
        self.conversion_class.start_size = start_size
        self.conversion_class.end_size = end_size
        self.conversion_class.noise = noise

    def set_binary_data(self, binary_data):
        if len(binary_data) == 94:
            self._set_binary_data_particle(binary_data)
            return

        if len(binary_data) % 6 != 0:
            logging.error("Atts.convert_binary_data(): Length of binary data was not a multiple of 6! Size: %i" % len(binary_data))

        poly_cnt = int(len(binary_data) / 6)
        atts_entries = []

        for i in range(poly_cnt):
            offset = int(i * 6)

            poly_id, color_val, shade_val, tracy_val, pad = struct.unpack(">hBBBB", binary_data[offset:offset + 6])

            new_atts_entry = self.atts_entry(poly_id, color_val, shade_val, tracy_val, pad)
            atts_entries.append(new_atts_entry)

        self.conversion_class.atts_entries = atts_entries
        assert binary_data[0:len(self.get_data())] == self.get_data()

    def _get_data_particle(self):
        return struct.pack(">hfffffffffffflllllllllll",
                           self.conversion_class.version,
                           self.conversion_class.accel_start_x,
                           self.conversion_class.accel_start_y,
                           self.conversion_class.accel_start_z,
                           self.conversion_class.accel_end_x,
                           self.conversion_class.accel_end_y,
                           self.conversion_class.accel_end_z,
                           self.conversion_class.magnify_start_x,
                           self.conversion_class.magnify_start_y,
                           self.conversion_class.magnify_start_z,
                           self.conversion_class.magnify_end_x,
                           self.conversion_class.magnify_end_y,
                           self.conversion_class.magnify_end_z,
                           self.conversion_class.collide, self.conversion_class.start_speed,
                           self.conversion_class.context_number, self.conversion_class.context_life_time,
                           self.conversion_class.context_start_gen, self.conversion_class.context_stop_gen,
                           self.conversion_class.gen_rate, self.conversion_class.lifetime,
                           self.conversion_class.start_size, self.conversion_class.end_size,
                           self.conversion_class.noise)

    def get_data(self):
        if not hasattr(self.conversion_class, "atts_entries"):  # HACK, although its a lot better than how STRC is doing
            return self._get_data_particle()

        ret = bytes()
        for atts in self.conversion_class.atts_entries:
            ret += struct.pack(">hBBBB",
                               atts["poly_id"],
                               atts["color_val"], atts["shade_val"],
                               atts["tracy_val"], atts["pad"])

        return ret


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L128
class Poo2(Chunk):
    def __init__(self, data=bytes()):
        super(Poo2, self).__init__("POO2", data)
        self.conversion_class.points = []
        self.set_binary_data(data)

    def points_as_list(self):
        return [[point["x"], point["y"], point["z"]] for point in self.conversion_class.points]

    def set_binary_data(self, binary_data):
        if len(binary_data) % 12 != 0:
            print("Poo2.convert_binary_data(): Length of binary data was not a multiple of 12!")

        num = int(len(binary_data) / 12)
        poo2_points = []

        for i in range(num):
            offset = int(i * 12)

            x, y, z = struct.unpack(">fff", binary_data[offset:offset + 12])
            new_poo2_point = {"x": x,
                              "y": y,
                              "z": z}
            poo2_points.append(new_poo2_point)

            self.conversion_class.points = poo2_points
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for point in self.conversion_class.points:
            ret += struct.pack(">fff", point["x"], point["y"], point["z"])

        return ret


class Sen2(Poo2):
    def __init__(self, data=bytes()):
        super(Sen2, self).__init__(data)
        self.chunk_id = "SEN2"


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L207
class Pol2(Chunk):
    def __init__(self, data=bytes()):
        super(Pol2, self).__init__("POL2", data)
        self.conversion_class.edges = []
        if data:
            self.set_binary_data(data)

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

        self.conversion_class.edges = pol2_edges
        assert binary_data == self.get_data()

    def get_data(self):
        ret = struct.pack(">I", len(self.conversion_class.edges))
        for pol2 in self.conversion_class.edges:
            ret += struct.pack(">H", len(pol2))
            for coordinate in pol2:
                ret += struct.pack(">H", coordinate)

        return ret


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/amesh.cpp#L301
class Olpl(Chunk):
    def __init__(self, data=bytes()):
        super(Olpl, self).__init__("OLPL", data)
        self.conversion_class.points = []
        self.set_binary_data(data)

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

        self.conversion_class.points = olpl_entries
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for olpl_entry in self.conversion_class.points:
            ret += struct.pack(">H", len(olpl_entry))
            for coordinates in olpl_entry:
                ret += struct.pack(">BB", *coordinates)

        return ret


class Otl2(Chunk):
    def __init__(self, data=bytes()):
        super(Otl2, self).__init__("OTL2", data)
        self.conversion_class.points = []
        self.set_binary_data(data)

    def set_binary_data(self, binary_data):
        offset = 0
        otl2_count = int(len(binary_data) / 2)

        poly = []
        for i in range(otl2_count):
            x, y = struct.unpack(">BB", binary_data[offset + 0:offset + 2])
            offset += 2
            poly.append([x, y])

        self.conversion_class.points = poly
        assert binary_data == self.get_data()

    def get_data(self):
        ret = bytes()
        for point in self.conversion_class.points:
            ret += struct.pack(">BB", *point)

        return ret


class Vbmp(Form):
    def __init__(self, sub_chunks=list()):
        super(Vbmp, self).__init__("VBMP", sub_chunks)

    def load_from_ilbm(self, file_name):
        pass

    def save_to_ilbm(self, file_name):
        pass

    def load_from_bmp(self, file_name):
        pass

    def save_to_bmp(self, file_name):
        pass


class Embd(Form):
    def __init__(self, sub_chunks=list()):
        super(Embd, self).__init__("EMBD", [Form("ROOT")] + sub_chunks)

    def add_emrs_resource(self, class_id, emrs_name, incoming_form):
        emrs_chunk = Emrs().from_json({"class_id": class_id,
                                       "emrs_name": emrs_name
                                       })
        self.add_chunk(emrs_chunk)
        self.add_chunk(incoming_form)

    def add_sklt(self, file_name, sklt_form):
        # if not isinstance(sklt_form, Sklt)
        self.add_emrs_resource("sklt.class", file_name, sklt_form)

    def add_vbmp(self, file_name, vbmp_form):
        if not isinstance(vbmp_form, Vbmp):
            logging.warning("Adding non-vbmp instance to Embd!")
        self.add_emrs_resource("ilbm.class", file_name, vbmp_form)

    def add_vanm(self, file_name, vanm_form):
        self.add_emrs_resource("bmpanim.class", file_name, vanm_form)


class Mc2(Form):
    def __init__(self):
        super(Mc2, self).__init__("MC2 ")
        self.embd = Embd()
        self.vehicles = Form("KIDS")
        self.buildings = Form("KIDS")
        self.ground = Form("KIDS")
        self.init_mc2()

        # Add convenience functions
        self.add_sklt = self.embd.add_sklt
        self.add_vbmp = self.embd.add_vbmp
        self.add_vanm = self.embd.add_vanm

    def init_mc2(self):
        # Populate MC2 /OBJT
        mc2_objt = Form("OBJT")
        self.add_chunk(mc2_objt)

        # Populate MC2 /OBJT/CLID
        mc2_objt_clid = Clid().from_json(myjson.loads("""{ "class_id": "base.class" }"""))
        mc2_objt.add_chunk(mc2_objt_clid)

        # Populate MC2 /OBJT/BASE and
        # Populate MC2 /OBJT/BASE/ROOT
        mc2_objt_base = Form("BASE", [Form("ROOT")])
        mc2_objt.add_chunk(mc2_objt_base)

        # Populate MC2 /OBJT/BASE/OBJT
        mc2_objt_base_objt = Form("OBJT")
        mc2_objt_base.add_chunk(mc2_objt_base_objt)

        # Populate MC2 /OBJT/BASE/OBJT/CLID
        mc2_objt_base_objt_clid = Clid().from_json(myjson.loads("""{ "class_id": "embed.class" }"""))
        mc2_objt_base_objt.add_chunk(mc2_objt_base_objt_clid)

        # Populate MC2 /OBJT/BASE/OBJT/EMBD
        mc2_objt_base_objt_embd = self.embd
        mc2_objt_base_objt.add_chunk(mc2_objt_base_objt_embd)

        # Populate MC2 /OBJT/BASE/STRC
        mc2_objt_base_strc = Strc().from_json(myjson.loads("""{
                                                            "_un1": 0,
                                                            "ambient_light": 255,
                                                            "att_flags": 72,
                                                            "ax": 0,
                                                            "ay": 0,
                                                            "az": 0,
                                                            "pos": [ 0.0, 0.0, 0.0 ],
                                                            "rx": 0,
                                                            "ry": 0,
                                                            "rz": 0,
                                                            "scale": [ 1.0, 1.0, 1.0 ],
                                                            "strc_type": "STRC_BASE",
                                                            "vec": [ 0.0, 0.0, 0.0 ],
                                                            "version": 1,
                                                            "vis_limit": 4096
                                                        }"""))
        mc2_objt_base.add_chunk(mc2_objt_base_strc)

        # Populate MC2 /OBJT/BASE/KIDS
        mc2_objt_base_kids = Form("KIDS")
        mc2_objt_base.add_chunk(mc2_objt_base_kids)

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT
        clid_base = Clid().from_json(myjson.loads("""{ "class_id": "base.class" }"""))
        mc2_objt_base_kids_objt0 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids_objt1 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids_objt2 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt0)
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt1)
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt2)

        base_strc = Strc().from_json(myjson.loads("""{
                                                    "_un1": 0,
                                                    "ambient_light": 255,
                                                    "att_flags": 72,
                                                    "ax": 0,
                                                    "ay": 0,
                                                    "az": 0,
                                                    "pos": [ 0.0, 0.0, 0.0 ],
                                                    "rx": 0,
                                                    "ry": 0,
                                                    "rz": 0,
                                                    "scale": [ 1.0, 1.0, 1.0 ],
                                                    "strc_type": "STRC_BASE",
                                                    "vec": [ 0.0, 0.0, 0.0 ],
                                                    "version": 1,
                                                    "vis_limit": 4096
                                                }"""))

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT/STRC
        mc2_objt_base_kids_objt0.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt1.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt2.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT/KIDS
        mc2_objt_base_kids_objt0.sub_chunks[1].add_chunk(self.vehicles)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt1.sub_chunks[1].add_chunk(self.buildings)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt2.sub_chunks[1].add_chunk(self.ground)  # Hack with sub_chunks[1]


all_ua_python_objects = {
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
    "VBMP": Vbmp,  # TODO Needs abstraction to load from and save to VBMP/FORM or BMP
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
    "STRC": strc_factory,
}


import glob
import struct

unsigned_int_be = "<I"
size_of_unsigned_int = 4
unsigned_short_be = "<H"
size_of_unsigned_short = 2


def compile_set_bas(visproto, sdf, slurps, set_number=1):
    mc2 = Mc2()

    embd = mc2.embd

    # TODO Bitmap function (in Embd class)
    bitmaps = glob.glob("set%i/*.bmp" % set_number)

    # Add bitmaps to Embd
    for bitmap in bitmaps:
        print(bitmap)

        with open(bitmap, "rb") as f:
            f.seek(10)
            data_offset = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

            f.seek(18)
            width = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]
            height = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

            f.seek(28)
            bpp = struct.unpack(unsigned_short_be, f.read(size_of_unsigned_short))[0]

            if bpp != 8 or width != 256 or height != 256:
                print("Bitmap must be 256x256 and using an indexed 8bit color map!\n"
                      "Image was: %sw*%sh*%sb" % (str(width), str(height), str(bpp)))
                raise ValueError("Selected bitmap was not in the correct format.")

            f.seek(data_offset)
            bitmap_data = f.read(65536)

            from PyQt5 import QtGui
            mirror_horizontal = False
            mirror_vertical = True
            image = QtGui.QImage(bitmap_data, width, height, QtGui.QImage.Format_Indexed8)
            image = image.mirrored(mirror_horizontal, mirror_vertical)
            ptr_image_data = image.bits()
            ptr_image_data.setsize(image.byteCount())
            bitmap_data = ptr_image_data.asstring()

            new_vbmp_head = Head().from_json(myjson.loads("""{ "flags": 0, "height": 256, "width": 256 }"""))
            new_vbmp_body = Body()
            new_vbmp_body.set_binary_data(bitmap_data)
            new_vbmp = Vbmp([new_vbmp_head, new_vbmp_body])
            embd.add_vbmp(os.path.splitext(os.path.basename(bitmap))[0] + "M", new_vbmp)  # HACK make .ILBM

    # TODO Skeleton functions (in Embd class)
    skeletons = glob.glob("set%i/Skeleton/*.json" % set_number)

    # Add skeletons to Embd
    for skeleton in skeletons:
        resource_name = "Skeleton/" + os.path.splitext(os.path.basename(skeleton))[0] + "t"  # HACK make .sklt

        with open(skeleton, "r") as f:
            sklt_form = Form().from_json(myjson.loads(f.read()))
            embd.add_sklt(resource_name, sklt_form)

    # TODO Animation functions (in Embd class)
    animations = glob.glob("set%i/rsrcpool/*.json" % set_number)

    # Add animations to Embd
    for animation in animations:
        resource_name = os.path.splitext(os.path.basename(animation))[0]

        with open(animation, "r") as f:
            vanm_form = Form().from_json(myjson.loads(f.read()))
            embd.add_vanm(resource_name, vanm_form)

    # TODO Move vehicles functions to MC2 object
    # vehicles = glob.glob("set%i/objects/vehicles/*.json" % set_number)
    vehicles2 = ["set%i/objects/vehicles/%s.json" % (set_number, x.replace("base", "bas")) for x in visproto]

    for vehicle in vehicles2:
        print(vehicle)
        with open(vehicle, "r") as f:
            vehicle_form = Form().from_json(myjson.loads(f.read()))  # TODO Eliminate junk code like this

        for chunk in vehicle_form.sub_chunks:
            mc2.vehicles.add_chunk(chunk)

    # TODO Move buildings functions to MC2 object
    # buildings = glob.glob("set%i/objects/buildings/*.json" % set_number)
    buildings2 = ["set%i/objects/buildings/%s.json" % (set_number, x.replace("base", "bas")) for x in sdf]

    for building in buildings2:
        print(building)
        with open(building, "r") as f:
            building_form = Form().from_json(myjson.loads(f.read()))  # TODO Eliminate junk code like this

        for chunk in building_form.sub_chunks:
            mc2.buildings.add_chunk(chunk)

    # TODO Move ground functions to MC2 object
    # grounds = glob.glob("set%i/objects/ground/*.json" % set_number)
    grounds2 = ["set%i/objects/ground/%s.json" % (set_number, x.replace("base", "bas")) for x in slurps]

    for ground in grounds2:
        print(ground)
        with open(ground, "r") as f:
            ground_form = Form().from_json(myjson.loads(f.read()))  # TODO Eliminate junk code like this

        for chunk in ground_form.sub_chunks:
            mc2.ground.add_chunk(chunk)

    pass
    # print(mc2.to_json())
    mc2.save_to_file("output/set_compiled.bas")


def compile_single_files(set_number=1):
    import shutil
    # Delete output folder if it exists
    if os.path.exists(os.getcwd() + "/output"):
        shutil.rmtree(os.getcwd() + "/output")

    # Create necessary folders that have not been created yet
    check_dirs = ["/output/data/set/rsrcpool",
                  "/output/data/set/Skeleton",
                  "/output/data/set/objects",
                  ]
    for dirs in check_dirs:
        if not os.path.exists(os.getcwd() + dirs):
            os.makedirs(os.getcwd() + dirs)

    # Copy static files
    shutil.copytree(os.getcwd() + "/mc2res", os.getcwd() + "/output/data/mc2res")
    shutil.copytree(os.getcwd() + "/set%i/hi" % set_number, os.getcwd() + "/output/data/set/hi")
    shutil.copytree(os.getcwd() + "/set%i/palette" % set_number, os.getcwd() + "/output/data/set/palette")
    shutil.copytree(os.getcwd() + "/set%i/remap" % set_number, os.getcwd() + "/output/data/set/remap")
    shutil.copytree(os.getcwd() + "/set%i/scripts" % set_number, os.getcwd() + "/output/data/set/scripts")
    shutil.copy(os.getcwd() + "/set%i/objects/beebox.bas" % set_number, os.getcwd() + "/output/data/set/objects/beebox.bas")

    # Compile images
    for bitmap in glob.glob("set%i/*.bmp" % set_number):
        print(bitmap)

        with open(bitmap, "rb") as f:
            f.seek(10)
            data_offset = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

            f.seek(18)
            width = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]
            height = struct.unpack(unsigned_int_be, f.read(size_of_unsigned_int))[0]

            f.seek(28)
            bpp = struct.unpack(unsigned_short_be, f.read(size_of_unsigned_short))[0]

            if bpp != 8 or width != 256 or height != 256:
                print("Bitmap must be 256x256 and using an indexed 8bit color map!\n"
                      "Image was: %sw*%sh*%sb" % (str(width), str(height), str(bpp)))
                raise ValueError("Selected bitmap was not in the correct format.")

            f.seek(data_offset)
            bitmap_data = f.read(65536)

            from PyQt5 import QtGui
            mirror_horizontal = False
            mirror_vertical = True
            image = QtGui.QImage(bitmap_data, width, height, QtGui.QImage.Format_Indexed8)
            image = image.mirrored(mirror_horizontal, mirror_vertical)
            ptr_image_data = image.bits()
            ptr_image_data.setsize(image.byteCount())
            bitmap_data = ptr_image_data.asstring()

            new_vbmp_head = Head().from_json(myjson.loads("""{ "flags": 0, "height": 256, "width": 256 }"""))
            new_vbmp_body = Body()
            new_vbmp_body.set_binary_data(bitmap_data)
            new_vbmp = Vbmp([new_vbmp_head, new_vbmp_body])
            new_vbmp.save_to_file("output/data/set/" + os.path.splitext(os.path.basename(bitmap))[0])

    # Compile animations
    for animation in glob.glob("set%i/rsrcpool/*.json" % set_number):
        resource_name = os.path.splitext(os.path.basename(animation))[0]

        with open(animation, "r") as f:
            vanm_form = Form().from_json(myjson.loads(f.read()))
            vanm_form.save_to_file("output/data/set/rsrcpool/" + resource_name)

    # Compile skeletons
    for skeleton in glob.glob("set%i/Skeleton/*.json" % set_number):
        resource_name = "Skeleton/" + os.path.splitext(os.path.basename(skeleton))[0]

        with open(skeleton, "r") as f:
            sklt_form = Form().from_json(myjson.loads(f.read()))
            sklt_form.save_to_file("output/data/set/" + resource_name)

    # Compile vehicles (Inside MC2 class)
    for vehicle in glob.glob("set%i/objects/vehicles/*.json" % set_number):
        resource_name = os.path.splitext(os.path.basename(vehicle))[0]

        with open(vehicle, "r") as f:
            sklt_form = Form().from_json(myjson.loads(f.read()))
            sklt_form.save_to_file("output/data/set/objects/" + resource_name)

    # Compile buildings (Inside MC2 class)
    for building in glob.glob("set%i/objects/buildings/*.json" % set_number):
        resource_name = os.path.splitext(os.path.basename(building))[0]

        with open(building, "r") as f:
            sklt_form = Form().from_json(myjson.loads(f.read()))
            sklt_form.save_to_file("output/data/set/objects/" + resource_name)

    # Compile ground (Inside MC2 class)
    for ground in glob.glob("set%i/objects/ground/*.json" % set_number):
        resource_name = os.path.splitext(os.path.basename(ground))[0]

        with open(ground, "r") as f:
            sklt_form = Form().from_json(myjson.loads(f.read()))
            sklt_form.save_to_file("output/data/set/objects/" + resource_name)


def parse_set_descriptor(set_number=1):
    sdf = []
    with open(os.path.join("set%i" % set_number, "scripts", "set.sdf"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b" ")[0].decode("ascii")
            sdf.append(base)
    print("sdf:", sdf)
    return sdf


def parse_visproto(set_number=1):
    visproto = []
    with open(os.path.join("set%i" % set_number, "scripts", "visproto.lst"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            visproto.append(base)
    print("visproto:", visproto)
    return visproto


def parse_slurps(set_number=1):
    slurps = []
    with open(os.path.join("set%i" % set_number, "scripts", "slurps.lst"), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            slurps.append(base)
    print("slurps:", slurps)
    return slurps


if __name__ == "__main__":
    compile_single_files(1)

    sdf = parse_set_descriptor(1)
    visproto = parse_visproto(1)
    slurps = parse_slurps(1)

    compile_set_bas(visproto, sdf, slurps, 1)
