from __future__ import annotations

import base64
import glob
import io
import logging
import os
import shutil
import struct
import sys
from typing import Any, BinaryIO, Callable, Dict, List, Optional, Type, Union

from PIL import Image, UnidentifiedImageError

try:
    import myjson as json
except ImportError:
    import json

logging.basicConfig(level=logging.INFO)

GFX_MAX_VERTEX = 12
unsigned_int_be = "<I"
size_of_unsigned_int = 4
unsigned_short_be = "<H"
size_of_unsigned_short = 2
DEFAULT_PALETTE_FILE = os.path.join("assets", "sets", "set1", "palette", "standard.pal")


chunk_registry: Dict[str, Type[Chunk]] = {}
form_registry: Dict[str, Type[Form]] = {}


def _register(registry: Dict[str, Type[Any]], *identifiers: str) -> Callable[[Type[Any]], Type[Any]]:
    """Return a decorator that registers a class for four-character IDs."""
    def decorator(class_type):
        for identifier in identifiers:
            if not isinstance(identifier, str) or len(identifier) != 4:
                raise ValueError("registered identifiers must be four-character strings")
            if identifier in registry:
                raise ValueError("%s is already registered" % identifier)
            registry[identifier] = class_type
        return class_type
    return decorator


def register_chunk(*identifiers: str) -> Callable[[Type[Chunk]], Type[Chunk]]:
    """Register a chunk class for one or more chunk IDs."""
    return _register(chunk_registry, *identifiers)


def register_form(*identifiers: str) -> Callable[[Type[Form]], Type[Form]]:
    """Register a form class for one or more form types."""
    return _register(form_registry, *identifiers)


class InvalidImage(Exception):
    pass


class Meshy(object):
    """
    ### A `Meshy` object contains exactly
    - one object name
    - one set of vertices
    - many meshes
      - one material
      - one set of faces
      - zero or one uv map

    - [ ] Can set object name from UA mesh definition at: MC2/OBJT/BASE/ROOT/NAME.name
    - [ ] Can load vertices from skeleton referenced in UA mesh defintion at: MC2/OBJT/BASE/OBJT/SKLC/NAME.name
    - [ ] Can load materials, faces, and uv maps from UA mesh definition at: MC2/OBJT/BASE/ADES/*/AMSH/**/{NAM2,ATTS,OLPL}
    """
    def __init__(self, name, vertices, meshes):
        pass


class Chunk(object):
    def __init__(self, chunk_id: str = "?!!?") -> None:
        self.chunk_id = chunk_id
        self.data: bytes = bytes("", "ascii")

    @staticmethod
    def validate_id(chunk_id: str) -> str:
        if not isinstance(chunk_id, str):
            raise ValueError("chunk_id must be a string. Supplied type was %s" % type(chunk_id))
        if chunk_id and not len(chunk_id) == 4:
            raise ValueError("length of chunk_id must be 4.")
        return chunk_id

    @staticmethod
    def validate_data(chunk_data: bytes) -> bytes:
        if not isinstance(chunk_data, bytes):
            raise ValueError("chunk_data must be bytes. Supplied type was %s" % type(chunk_data))
        return chunk_data

    def set_binary_data(self, binary_data: bytes) -> None:
        self.data = binary_data

    # Returns only chunk data
    def get_data(self) -> bytes:
        return self.data

    # Returns chunk_id, size, chunk_data and pad byte
    def full_data(self) -> bytes:
        data = self.get_data()
        data_length = len(data)
        if len(data) % 2:
            data += b"\x00"
        return bytes(self.chunk_id, "ascii") + struct.pack(">I", data_length) + data

    def size(self) -> int:
        return len(self.data)

    def load_data_from_file(self, file_name: str) -> bytes:
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as f:
            data = f.read()
            if data[0:4] == bytes("FORM", "ascii"):
                raise ValueError("You shouldn't load a FORM file into a chunk!")
            self.data = data

        return data

    def load_from_file(self, file_name: str) -> Chunk:
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)  # No Test Coverage

        with open(file_name, "rb") as f:
            data = f.read()
            if data[0:4] == bytes("FORM", "ascii"):
                raise ValueError("You shouldn't load a FORM file into a chunk!")  # No Test Coverage

            chunk_id = bytes(data[0:4]).decode()
            chunk_size = struct.unpack(">I", data[4:8])[0]
            rest_of_file_data = data[8:]
            if chunk_size <= len(rest_of_file_data):
                self.data = rest_of_file_data[:chunk_size]
                self.chunk_id = chunk_id

            return self

    def save_data_to_file(self, file_name: str) -> None:
        with open(file_name, "wb") as f:
            f.write(self.get_data())

    def save_to_file(self, file_name: str) -> None:
        with open(file_name, "wb") as f:
            f.write(self.full_data())

    def to_dict(self) -> Dict[str, Dict[str, Any]]:
        if self.chunk_id in chunk_registry:
            o = chunk_registry[self.chunk_id]()
            o.set_binary_data(self.data)
            return o.to_dict()
        # Generic json support for all IFF chunks
        return {self.chunk_id: {"data": base64.b64encode(self.data).decode("ascii")}}  # No Test Coverage

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True)

    def from_json(self, json_dict: Union[str, Dict[str, Dict[str, Any]]]) -> Chunk:
        if isinstance(json_dict, str):
            json_dict = json.loads(json_dict)  # No Test Coverage
        self.chunk_id, attributes_dict = json_dict.popitem()
        if self.chunk_id in chunk_registry:
            o = chunk_registry[self.chunk_id]()
        else:
            raise ValueError("Cant call from_json() on unknown Chunk type")  # No Test Coverage
        o.from_json_generic({self.chunk_id: attributes_dict})
        self.set_binary_data(o.get_data())
        return self

    def from_json_generic(self, json_string: Union[str, Dict[str, Dict[str, Any]]]) -> Chunk:
        # Generic json support for all IFF chunks
        if isinstance(json_string, str):
            json_dict = json.loads(json_string)  # No Test Coverage
        else:
            json_dict = json_string

        self.chunk_id, attributes_dict = json_dict.popitem()
        for k, v in attributes_dict.items():
            setattr(self, k, v)
        return self


@register_form("PTCL")
class Form(object):
    def __init__(self, form_type: str = "!??!", sub_chunks: Optional[List[Union[Form, Chunk]]] = None) -> None:
        self.form_type = form_type
        if sub_chunks is None:
            sub_chunks = []

        if not isinstance(sub_chunks, list):
            raise ValueError("sub_chunks must be a list. Supplied type was %s" % type(sub_chunks))

        self.sub_chunks: List[Union[Form, Chunk]] = sub_chunks

    @staticmethod
    def validate_form_type(form_type: str) -> str:
        if not isinstance(form_type, str):
            raise ValueError("form_type must be a string. Supplied type was %s" % type(form_type))
        if form_type == "FORM":
            raise ValueError("form_type should not be FORM.")
        if form_type and not len(form_type) == 4:
            raise ValueError("length of form_type must be 4.")
        return form_type

    @staticmethod
    def validate_sub_chunks(sub_chunks: Optional[List[Union[Form, Chunk]]]) -> List[Union[Form, Chunk]]:
        if sub_chunks is None:
            return []
        if not isinstance(sub_chunks, list):
            raise ValueError("sub_chunks must be a list. Supplied type was %s" % type(sub_chunks))
        return sub_chunks

    def child(self, child_num: int) -> Union[Form, Chunk]:
        return self.sub_chunks[child_num]

    # Returns only form_data
    def get_data(self) -> bytes:
        form_header = bytes(self.form_type, "ascii")
        form_data = bytes()
        for c in self.sub_chunks:
            form_data += c.full_data()
        return form_header + form_data

    # Returns form_type, size, form_data
    def full_data(self) -> bytes:
        data = self.get_data()
        data_length = len(data)
        return bytes("FORM", "ascii") + struct.pack(">I", data_length) + data

    def to_dict(self) -> Dict[str, List[Dict[str, Any]]]:
        # Generic json support for all IFF forms
        children = []
        for child in self.sub_chunks:
            children.append(child.to_dict())
        return {self.form_type: children}

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True)

    def from_json(self, json_dict: Union[str, List[Any], Dict[str, Any]]) -> Union[Form, Chunk, List[Union[Form, Chunk]]]:
        # Generic json support for all IFF forms
        if isinstance(json_dict, str):
            json_dict = json.loads(json_dict)  # No Test Coverage

        if isinstance(json_dict, list):
            ret_list = []
            for child in json_dict:
                ret_list.append(self.from_json(child))
            return ret_list

        if isinstance(json_dict, dict):
            for k, v in json_dict.items():
                if isinstance(v, list):
                    return make_form(k, self.from_json(v))
                if isinstance(v, dict):
                    chunk = Chunk(chunk_id=k).from_json({k: v})
                    return make_chunk(chunk.chunk_id, chunk.get_data())
                raise ValueError("not dict or list :(", k, v)  # No Test Coverage

        raise ValueError("Fall through error. This shouldnt happen on well formed data "
                         "Check that you didn't send bytes to this function")  # No Test Coverage

    def from_json_file(self, file_name: str) -> Union[Form, Chunk, List[Union[Form, Chunk]]]:
        with open(file_name, "r") as f:
            return self.from_json(json.loads(f.read()))

    def size(self) -> int:
        return len(self.get_data())

    def get_all(self, ckid: str, max_count: int = 9999) -> List[Union[Form, Chunk]]:
        ret_chunks = []
        for child in self.sub_chunks:
            if len(ret_chunks) >= max_count:
                break
            if isinstance(child, Chunk) and child.chunk_id == ckid:
                ret_chunks.append(child)
            if isinstance(child, Form):
                if child.form_type == ckid:
                    ret_chunks.append(child)
                ret_chunks.extend(child.get_all(ckid, max_count - len(ret_chunks)))
        return ret_chunks

    def get_single(self, ckid: str) -> Optional[Union[Form, Chunk]]:
        ret_form = self.get_all(ckid, max_count=1)
        if ret_form:
            return ret_form[0]
        return None

    def get_direct_all(self, identifier: str) -> List[Union[Form, Chunk]]:
        """Return immediate children whose chunk ID or form type matches *identifier*."""
        return [child for child in self.sub_chunks
                if (isinstance(child, Chunk) and child.chunk_id == identifier)
                or (isinstance(child, Form) and child.form_type == identifier)]

    def get_direct_single(self, identifier: str) -> Optional[Union[Form, Chunk]]:
        """Return the first matching immediate child, without descending into forms."""
        children = self.get_direct_all(identifier)
        return children[0] if children else None

    def load_from_file(self, file_name: str) -> Form:
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The specified file could not be found: %s" % file_name)

        with open(file_name, "rb") as bas_file:
            parsed_bas = Form().parse_stream(bas_file)[0]
            self.sub_chunks = parsed_bas.sub_chunks
            self.form_type = parsed_bas.form_type

        return self

    def save_to_file(self, file_name: str) -> None:
        with open(file_name, "wb") as f:
            f.write(self.full_data())

    def save_to_json_file(self, file_name: str) -> None:
        with open(file_name, "wt") as f:
            f.write(self.to_json())

    def parse_stream(self, bas_data: BinaryIO) -> List[Union[Form, Chunk]]:
        ret_chunks = []
        while True:
            magic = bytes(bas_data.read(4)).decode()
            if not magic:
                break

            if magic == "FORM":
                form_size = struct.unpack(">I", bas_data.read(4))[0] - 4
                form_type = bytes(bas_data.read(4)).decode()
                form_data_stream = io.BytesIO(bas_data.read(form_size))
                logging.debug("Found Form", form_type, form_size)
                ret_chunks.append(make_form(form_type, self.parse_stream(form_data_stream)))
                continue

            if magic != "FORM":
                chunk_size = struct.unpack(">I", bas_data.read(4))[0]
                chunk_id = magic
                chunk_data = bas_data.read(chunk_size)
                if chunk_size % 2:
                    bas_data.read(1)  # Discard pad byte
                logging.debug("Found Chunk", chunk_id, chunk_size)
                ret_chunks.append(make_chunk(chunk_id, chunk_data))

        return ret_chunks

    def add_chunk(self, chunk: Union[Form, Chunk]) -> None:
        self.sub_chunks.append(chunk)


def palette_from_pal(file_name: str) -> List[int]:
    """Load an IFF/ILBM CMAP chunk as opaque ARGB palette entries."""
    form = Form().load_from_file(file_name)
    cmap = form.get_single("CMAP")
    if not isinstance(cmap, Chunk):
        raise ValueError("%s does not contain a CMAP chunk" % file_name)

    data = cmap.get_data()
    if len(data) % 3:
        raise ValueError("CMAP data in %s is not RGB triplets" % file_name)

    return [0xFF000000 | (red << 16) | (green << 8) | blue
            for red, green, blue in zip(data[0::3], data[1::3], data[2::3])]


def palette_data(palette: Optional[List[int]] = None) -> bytes:
    """Return a palette as Pillow's RGB byte sequence."""
    if palette is None:
        palette = palette_from_pal(DEFAULT_PALETTE_FILE)
    return bytes(component
                 for color in palette
                 for component in ((color >> 16) & 0xff, (color >> 8) & 0xff, color & 0xff))


@register_form("AMSH")
class Amsh(Form):
    def __init__(self, form_type: str = "AMSH", sub_chunks: Optional[List[Union[Form, Chunk]]] = None) -> None:
        super(Amsh, self).__init__(form_type, sub_chunks)

    @property
    def has_uv(self) -> bool:
        if self.get_single("OLPL"):
            return True
        return False

    @property
    def get_texture_name(self) -> str:
        return self.get_single("NAM2").name

    @property
    def get_polys(self) -> List[int]:
        return [x["poly_id"] for x in self.get_single("ATTS").atts_entries]

    @property
    def get_uv_mapping(self) -> List[List[List[float]]]:
        olpl = self.get_single("OLPL")
        olpl.normalize()
        return olpl.points


@register_chunk("NAME")
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

    def to_dict(self):
        return {self.chunk_id: {"zero_terminated": self.zero_terminated,
                                "name": self.name
                                }
                }


@register_chunk("CLID")
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

    def to_dict(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                }
                }


@register_chunk("EMRS")
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

    def to_dict(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                "emrs_name": self.emrs_name,
                                }
                }


@register_chunk("NAM2")
class Nam2(Name):
    def __init__(self, chunk_id="NAM2"):
        super(Nam2, self).__init__(chunk_id)


@register_chunk("DATA")
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
        self.vbmp_names = []
        self.polygons = []
        self.frames = []

    def set_binary_data(self, binary_data):
        vanm_data = binary_data
        # vanm_data_len = len(vanm_data)

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
        self.vbmp_names = vbmp_fnames

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

        self.polygons = vanm_polygons

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

        # When parsed from binary data the original name and polygon tables
        # are preserved byte-for-byte (the polygon table keeps one entry per
        # frame usage); otherwise they are rebuilt from the frames.
        poly = self.polygons if self.polygons else [frame["vbmp_coords"] for frame in self.frames]
        vbmp_names = self.vbmp_names if self.vbmp_names else []
        if not self.vbmp_names:
            for frame in self.frames:
                if frame["vbmp_name"] not in vbmp_names:
                    vbmp_names.append(frame["vbmp_name"])

        frame_times = []
        for frame in self.frames:
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

    def to_dict(self):
        return {self.chunk_id: {"class_id": self.class_id,
                                "vbmp_names": self.vbmp_names,
                                "polygons": self.polygons,
                                "frames": self.frames,
                                }
                }


@register_chunk("HEAD")
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

    def to_dict(self):
        return {self.chunk_id: {"width": self.width,
                                "height": self.height,
                                "flags": self.flags,
                                }
                }


@register_chunk("BODY")
class Body(Chunk):
    def __init__(self, chunk_id="BODY"):
        super(Body, self).__init__(chunk_id)
        self.data = bytes()

    def set_binary_data(self, binary_data):
        self.data = binary_data
        assert binary_data == self.get_data()

    def get_data(self):
        return self.data

    def to_dict(self):
        return {self.chunk_id: {"data": base64.b64encode(self.get_data()).decode("ascii")}}

    def from_json_generic(self, json_string):
        if isinstance(json_string, str):
            json_string = json.loads(json_string)  # No Test Coverage
        self.chunk_id, attributes_dict = json_string.popitem()  # No Test Coverage
        self.data = base64.b64decode(attributes_dict["data"])  # No Test Coverage


# https://github.com/Marisa-Chan/UA_source/blob/master/src/amesh.cpp#L262
# Particle.class has its own binary format https://github.com/Marisa-Chan/UA_source/blob/master/src/particle.cpp#L681
@register_chunk("ATTS")
class Atts(Chunk):
    def __init__(self, chunk_id="ATTS"):
        super(Atts, self).__init__(chunk_id)
        self.is_particle_atts = False
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
        self.is_particle_atts = True
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
            logging.error("Atts.convert_binary_data(): "
                          "Length of binary data was not a multiple of 6! "  # No Test Coverage
                          "Size: %i" % len(binary_data))

        self.is_particle_atts = False
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
        if self.is_particle_atts:
            return self._get_data_particle()

        ret = bytes()

        for atts in self.atts_entries:
            ret += struct.pack(">hBBBB",
                               atts["poly_id"],
                               atts["color_val"], atts["shade_val"],
                               atts["tracy_val"], atts["pad"])

        return ret

    def _to_json_particle(self):
        return {self.chunk_id: {"is_particle_atts": self.is_particle_atts,
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
        return {self.chunk_id: {"is_particle_atts": self.is_particle_atts,
                                "atts_entries": self.atts_entries,
                                }
                }

    def to_dict(self):
        if self.is_particle_atts:
            return self._to_json_particle()

        return self._to_json_generic()


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L128
@register_chunk("POO2")
class Poo2(Chunk):
    def __init__(self, chunk_id="POO2"):
        super(Poo2, self).__init__(chunk_id)
        self.points = []

    def scale_down(self, scaling_factor):
        self.points = [{"x": point["x"] / scaling_factor,
                        "y": point["y"] / scaling_factor,
                        "z": point["z"] / scaling_factor} for point in self.points]

    def scale_up(self, scaling_factor):
        self.scale_down(1 / scaling_factor)

    def change_coordinate_system(self):
        self.points = [{"x": point["x"] * -1,
                        "y": point["z"] * -1,
                        "z": point["y"] * -1} for point in self.points]

    def points_as_list(self):
        return [[point["x"], point["y"], point["z"]] for point in self.points]  # No Test Coverage

    def points_as_flattened_list(self):
        return [item for sublist in self.points_as_list() for item in sublist]  # No Test Coverage

    def set_points_from_list(self, points):
        self.points = [{"x": x,
                        "y": y,
                        "z": z} for x, y, z in points]  # No Test Coverage

    def round_points(self):
        self.points = [{"x": round(point["x"]),
                        "y": round(point["y"]),
                        "z": round(point["z"])} for point in self.points]  # No Test Coverage

    def points_as_vectors(self):
        return [Vector(*xyz) for xyz in self.points_as_list()]

    def set_binary_data(self, binary_data):
        if len(binary_data) % 12 != 0:  # No Test Coverage
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

    def to_dict(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


@register_chunk("SEN2")
class Sen2(Poo2):
    def __init__(self, chunk_id="SEN2"):
        super(Sen2, self).__init__(chunk_id)


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/sklt.cpp#L207
@register_chunk("POL2")
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
            if len(pol2) > GFX_MAX_VERTEX:
                raise ValueError("Too many faces in polygon detected ({}). Max number of faces per polygon is 12. "
                                 "Check GFX_MAX_VERTEX in engine_gfx.h".format(len(pol2)))
            for coordinate in pol2:
                ret += struct.pack(">H", coordinate)

        return ret

    def to_dict(self):
        return {self.chunk_id: {"edges": self.edges,
                                }
                }


# https://github.com/Marisa-Chan/UA_source/blob/44bb2284bf15fd55085ccca160d5bc2f6032e345/src/amesh.cpp#L301
@register_chunk("OLPL")
class Olpl(Chunk):
    def __init__(self, chunk_id="OLPL"):
        super(Olpl, self).__init__(chunk_id)
        self.points = []

    def _int_to_float(self, inp):
        if isinstance(inp, int):
            return float(inp) / float(255)
        if isinstance(inp, list):
            return [self._int_to_float(x) for x in inp]
        raise ValueError("int_to_float(): Invalid data type")

    def as_floats(self):
        return self._int_to_float(self.points)

    def normalize(self):
        ret = []
        for i in self.points:
            j_ret = []
            for j in i:
                k_ret = []
                for index, k in enumerate(j):
                    if index % 2:
                        k = 255 - k
                    k_ret.append(k / 256)
                j_ret.append(k_ret)
            ret.append(j_ret)
        self.points = ret

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

    def to_dict(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


@register_chunk("OTL2")
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

    def to_dict(self):
        return {self.chunk_id: {"points": self.points,
                                }
                }


@register_form("VBMP")
class Vbmp(Form):
    def __init__(self, form_type="VBMP", sub_chunks=None):
        super(Vbmp, self).__init__(form_type, sub_chunks)
        self.file_name = "not_used.vbmp"  # TODO USE THIS

    def load_from_ilbm(self, file_name):
        form = Form().load_from_file(file_name)

        new_vbmp_head = Head()
        new_vbmp_head.set_binary_data(form.sub_chunks[0].get_data())
        new_vbmp_body = Body()
        new_vbmp_body.set_binary_data(form.sub_chunks[1].get_data())
        self.sub_chunks = []
        self.add_chunk(new_vbmp_head)
        self.add_chunk(new_vbmp_body)

        return self

    def save_to_ilbm(self, file_name):
        pass

    def load_image(self, file_name):
        try:
            with Image.open(file_name) as source_image:
                image = source_image.convert("RGB")
        except (FileNotFoundError, UnidentifiedImageError, OSError) as error:
            raise InvalidImage("WARNING: Not loading invalid image file: {}".format(file_name)) from error

        if image.size != (256, 256):
            logging.warning("WARNING: The file %s has a size that is not 256x256!", file_name)
            image = image.resize((256, 256), Image.Resampling.LANCZOS)

        palette = Image.new("P", (1, 1))
        palette.putpalette(palette_data())
        bitmap_data = image.quantize(palette=palette).tobytes()

        new_vbmp_head = Head()
        new_vbmp_head.height = 256
        new_vbmp_head.width = 256
        new_vbmp_body = Body()
        new_vbmp_body.set_binary_data(bitmap_data)
        self.sub_chunks = []
        self.add_chunk(new_vbmp_head)
        self.add_chunk(new_vbmp_body)

        # set self.file_name = "new_sky.ilbm" chopping off ".bmp"
        self.file_name = os.path.splitext(os.path.basename(file_name))[0]

        return self

    def save_to_bmp(self, file_name):
        data = self.sub_chunks[1].get_data()
        image = Image.frombytes("P", (256, 256), data)
        image.putpalette(palette_data())
        image.save(file_name)


@register_form("EMBD")
class Embd(Form):
    def __init__(self, form_type="EMBD", sub_chunks=None):
        if sub_chunks is None:
            sub_chunks = [Root()]
        super(Embd, self).__init__(form_type, sub_chunks)
        self.emrs_resources = {}
        self.parse_emrs()

    def parse_emrs(self):
        emrs_name = None
        self.emrs_resources = {}
        for i, sub_chunk in enumerate(self.sub_chunks):
            if i == 0:
                # noinspection PyUnresolvedReferences
                if not isinstance(sub_chunk, Form) and sub_chunk.form_type == "ROOT":  # No Test Coverage
                    raise ValueError("Embd().parse_emrs() expects first sub_chunk to be Form() with type ROOT")
            elif i % 2:
                # noinspection PyUnresolvedReferences
                emrs_name = sub_chunk.emrs_name
            else:
                self.emrs_resources[emrs_name] = sub_chunk

    def emrs_index_by_name(self, emrs_name):
        if not self.emrs_resources:
            self.parse_emrs()

        if emrs_name not in self.emrs_resources:
            return None

        return self.sub_chunks.index(self.emrs_resources[emrs_name])

    def add_emrs_resource(self, class_id, emrs_name, incoming_form):
        emrs_chunk = Emrs()
        emrs_chunk.class_id = class_id
        emrs_chunk.emrs_name = emrs_name

        self.add_chunk(emrs_chunk)
        self.add_chunk(incoming_form)
        self.parse_emrs()

    def add_sklt(self, file_name, sklt_form):
        # if not isinstance(sklt_form, Sklt)
        self.add_emrs_resource("sklt.class", file_name, sklt_form)

    def add_vbmp(self, file_name, vbmp_form):
        if not isinstance(vbmp_form, Vbmp):
            logging.warning("Adding non-vbmp instance to Embd!")  # No Test Coverage
        self.add_emrs_resource("ilbm.class", file_name, vbmp_form)

    def add_vanm(self, file_name, vanm_form):
        self.add_emrs_resource("bmpanim.class", file_name, vanm_form)

    def extract_resources(self, output_location):
        logging.info("extracting resources")

        if not os.path.isdir(output_location):
            os.mkdir(output_location)

        asset_name = None
        for i, sub_chunk in enumerate(self.sub_chunks):
            if i == 0:
                # noinspection PyUnresolvedReferences
                if not isinstance(sub_chunk, Form) and sub_chunk.form_type == "ROOT":
                    raise ValueError("Embd().extract_resources() expects first sub_chunk to be Form() with type ROOT")
            elif i % 2:
                # EMRS
                # noinspection PyUnresolvedReferences
                asset_name = sub_chunk.emrs_name
            else:
                # Asset
                if sub_chunk.form_type == "VBMP":
                    # noinspection PyUnresolvedReferences
                    sub_chunk.save_to_bmp(os.path.join(output_location, "%s.bmp" % asset_name))
                elif sub_chunk.form_type == "SKLT" or sub_chunk.form_type == "VANM":
                    # TODO: Using the asset name is not compatible with MC2 forms which
                    # TODO:   expect the file name to be Skeleton/blah.sklt
                    base_name = os.path.basename(asset_name)
                    with open(os.path.join(output_location, base_name + ".json"), "w") as f:
                        f.write(sub_chunk.to_json())
                else:
                    raise ValueError("extract_resources() unimplemented for %s", sub_chunk.form_type)


@register_form("MC2 ")
class Mc2(Form):
    def __init__(self, form_type="MC2 ", sub_chunks=None):
        super(Mc2, self).__init__(form_type, sub_chunks)
        self.embd = Embd()
        self.vehicles = Kids()
        self.buildings = Kids()
        self.ground = Kids()

        if sub_chunks is None:
            self.init_mc2()

    def init_mc2(self):
        # Populate MC2 /OBJT
        mc2_objt = Objt()
        self.add_chunk(mc2_objt)

        # Populate MC2 /OBJT/CLID
        mc2_objt_clid = Clid()
        mc2_objt_clid.class_id = "base.class"
        mc2_objt.add_chunk(mc2_objt_clid)

        # Populate MC2 /OBJT/BASE and
        # Populate MC2 /OBJT/BASE/ROOT
        mc2_objt_base = Form("BASE", [Form("ROOT")])
        mc2_objt.add_chunk(mc2_objt_base)

        # Populate MC2 /OBJT/BASE/OBJT
        mc2_objt_base_objt = Objt()
        mc2_objt_base.add_chunk(mc2_objt_base_objt)

        # Populate MC2 /OBJT/BASE/OBJT/CLID
        mc2_objt_base_objt_clid = Clid()
        mc2_objt_base_objt_clid.class_id = "embed.class"
        mc2_objt_base_objt.add_chunk(mc2_objt_base_objt_clid)

        # Populate MC2 /OBJT/BASE/OBJT/EMBD
        mc2_objt_base_objt_embd = self.embd
        mc2_objt_base_objt.add_chunk(mc2_objt_base_objt_embd)

        # Populate MC2 /OBJT/BASE/STRC
        mc2_objt_base_strc = Strc()
        mc2_objt_base_strc.ambient_light = 255
        mc2_objt_base_strc.att_flags = 72
        mc2_objt_base_strc.scale = [1.0, 1.0, 1.0]
        mc2_objt_base_strc.strc_type = "STRC_BASE"
        mc2_objt_base_strc.version = 1
        mc2_objt_base_strc.vis_limit = 4096
        mc2_objt_base.add_chunk(mc2_objt_base_strc)

        # Populate MC2 /OBJT/BASE/KIDS
        mc2_objt_base_kids = Kids()
        mc2_objt_base.add_chunk(mc2_objt_base_kids)

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT
        clid_base = Clid()
        clid_base.class_id = "base.class"
        mc2_objt_base_kids_objt0 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids_objt1 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids_objt2 = Form("OBJT", [clid_base, Form("BASE", [Form("ROOT")])])
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt0)
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt1)
        mc2_objt_base_kids.add_chunk(mc2_objt_base_kids_objt2)

        base_strc = Strc()
        base_strc.ambient_light = 255
        base_strc.att_flags = 72
        base_strc.scale = [1.0, 1.0, 1.0]
        base_strc.strc_type = "STRC_BASE"
        base_strc.version = 1
        base_strc.vis_limit = 4096

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT/STRC
        mc2_objt_base_kids_objt0.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt1.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt2.sub_chunks[1].add_chunk(base_strc)  # Hack with sub_chunks[1]

        # Populate MC2 /OBJT/BASE/KIDS/OBJT {0,1,2}/BASE/ROOT/KIDS
        mc2_objt_base_kids_objt0.sub_chunks[1].add_chunk(self.vehicles)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt1.sub_chunks[1].add_chunk(self.buildings)  # Hack with sub_chunks[1]
        mc2_objt_base_kids_objt2.sub_chunks[1].add_chunk(self.ground)  # Hack with sub_chunks[1]

    def add_vehicle_from_json_file(self, file_name):
        vehicle_form = Form().from_json_file(file_name)

        for sub_chunk in vehicle_form.sub_chunks:
            self.vehicles.add_chunk(sub_chunk)

    def add_building_from_json_file(self, file_name):
        building_form = Form().from_json_file(file_name)

        for sub_chunk in building_form.sub_chunks:
            self.buildings.add_chunk(sub_chunk)

    def add_ground_from_json_file(self, file_name):
        ground_form = Form().from_json_file(file_name)

        for sub_chunk in ground_form.sub_chunks:
            self.ground.add_chunk(sub_chunk)

    def add_image_from_file(self, file_name):
        resource_name = os.path.splitext(os.path.basename(file_name))[0] + "M"  # HACK make .ILBM
        vbmp_form = Vbmp().load_image(file_name)
        self.embd.add_vbmp(resource_name, vbmp_form)

    def add_skeleton_from_json_file(self, file_name):
        resource_name = "Skeleton/" + os.path.splitext(os.path.basename(file_name))[0] + "t"  # HACK make .sklt
        sklt_form = Form().from_json_file(file_name)
        self.embd.add_sklt(resource_name, sklt_form)

    def add_animation_from_json_file(self, file_name):
        resource_name = os.path.splitext(os.path.basename(file_name))[0]
        vanm_form = Form().from_json_file(file_name)
        self.embd.add_vanm(resource_name, vanm_form)


@register_chunk("STRC")
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
            raise ValueError("strc_factory() received invalid data:", binary_data)  # No Test Coverage
        if binary_data[0:5] == b"\x00\x01\x00\x06\x00":
            # BANI STRC
            return self._set_binary_data_bani(binary_data)

        raise ValueError("Strc().set_data() received invalid data: %s" % binary_data)  # No Test Coverage

    def get_data(self):
        if self.strc_type == Strc.STRC_BASE:
            return self._get_data_base()
        if self.strc_type == Strc.STRC_ADE:
            return self._get_data_ade()
        if self.strc_type == Strc.STRC_AREA:
            return self._get_data_area()
        if self.strc_type == Strc.STRC_BANI:
            return self._get_data_bani()

        raise ValueError("Can't get_data() from strc_type STRC_UNKNOWN!!")  # No Test Coverage

    def _set_binary_data_base(self, binary_data):
        if len(binary_data) != 62:
            # No Test Coverage
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
            # No Test Coverage
            raise ValueError("Length of binary_data was not 10 bytes! Not valid for STRC_ADE objects!")
        if version != 1:
            raise ValueError("Version of binary_data was not 1! Not valid for STRC_ADE objects!")  # No Test Coverage
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
            # No Test Coverage
            raise ValueError("Length of binary_data was not 10 bytes! Not valid for STRC_AREA objects!")
        if version != 256:
            # No Test Coverage
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

    def to_dict(self):
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

        raise ValueError("STRC().to_dict() Can't get json for unknown STRC!")  # No Test Coverage


@register_form("ADE ")
class Ade(Form):
    """An area-definition form with a direct ``STRC`` descriptor."""
    def __init__(self, form_type="ADE ", sub_chunks=None):
        super(Ade, self).__init__(form_type, sub_chunks)

    @property
    def structure(self) -> Optional[Strc]:
        structure = self.get_direct_single("STRC")
        return structure if isinstance(structure, Strc) else None

    def validate(self) -> List[str]:
        """Return a list of structural-error paths; an empty list means valid."""
        errors = []
        structures = self.get_direct_all("STRC")
        if not structures:
            errors.append("ADE : missing direct STRC chunk")
        else:
            if len(structures) > 1:
                errors.append("ADE : duplicate direct STRC chunks")
            structure = structures[0]
            if not isinstance(structure, Strc):
                errors.append("ADE : direct STRC chunk is not a STRC chunk")
            elif structure.strc_type != Strc.STRC_ADE:
                errors.append("ADE : direct STRC chunk is not a STRC_ADE structure")
        return errors


@register_form("BANI")
class Bani(Form):
    """A bone-animation form with a direct ``STRC`` descriptor."""
    def __init__(self, form_type="BANI", sub_chunks=None):
        super(Bani, self).__init__(form_type, sub_chunks)

    @property
    def animation(self) -> Optional[Strc]:
        animation = self.get_direct_single("STRC")
        return animation if isinstance(animation, Strc) else None


@register_form("VANM")
class Vanm(Form):
    """A bitmap animation form containing a single ``DATA`` chunk."""
    def __init__(self, form_type="VANM", sub_chunks=None):
        super(Vanm, self).__init__(form_type, sub_chunks)

    @property
    def data(self) -> Optional[Data]:
        data = self.get_direct_single("DATA")
        return data if isinstance(data, Data) else None

    @property
    def frames(self) -> List[Dict[str, Any]]:
        return self.data.frames if self.data else []

    @property
    def bitmap_names(self) -> List[str]:
        return list(dict.fromkeys(frame["vbmp_name"] for frame in self.frames))

    def validate(self) -> List[str]:
        """Return a list of structural-error paths; an empty list means valid."""
        errors = []
        data_chunks = self.get_direct_all("DATA")
        if not data_chunks:
            errors.append("VANM: missing direct DATA chunk")
        else:
            if len(data_chunks) > 1:
                errors.append("VANM: duplicate direct DATA chunks")
            if not isinstance(data_chunks[0], Data):
                errors.append("VANM: direct DATA chunk is not a DATA chunk")
        return errors


@register_form("CIBO")
class Cibo(Form):
    """A bitmap reference form containing a ``NAM2`` chunk."""
    def __init__(self, form_type="CIBO", sub_chunks=None):
        super(Cibo, self).__init__(form_type, sub_chunks)

    @property
    def bitmap_name(self) -> Optional[str]:
        name = self.get_direct_single("NAM2")
        return name.name if isinstance(name, Nam2) else None

    @property
    def outline(self) -> Optional[Otl2]:
        outline = self.get_direct_single("OTL2")
        return outline if isinstance(outline, Otl2) else None

    def validate(self) -> List[str]:
        """Return a list of structural-error paths; an empty list means valid."""
        errors = []
        name_chunks = self.get_direct_all("NAM2")
        if not name_chunks:
            errors.append("CIBO: missing direct NAM2 chunk")
        else:
            if len(name_chunks) > 1:
                errors.append("CIBO: duplicate direct NAM2 chunks")
            if not isinstance(name_chunks[0], Nam2):
                errors.append("CIBO: direct NAM2 chunk is not a NAM2 chunk")
        return errors


@register_form("SKLC")
class Sklc(Form):
    """A skeleton resource reference containing a direct ``NAME`` chunk."""
    def __init__(self, form_type="SKLC", sub_chunks=None):
        super(Sklc, self).__init__(form_type, sub_chunks)

    @property
    def skeleton_name(self) -> Optional[str]:
        name = self.get_direct_single("NAME")
        return name.name if isinstance(name, Name) else None


@register_form("AREA")
class Area(Form):
    """A textured or animated mesh area definition."""
    def __init__(self, form_type="AREA", sub_chunks=None):
        super(Area, self).__init__(form_type, sub_chunks)

    @property
    def definition(self) -> Optional[Ade]:
        definition = self.get_direct_single("ADE ")
        return definition if isinstance(definition, Ade) else None

    @property
    def polygon_index(self) -> Optional[int]:
        if not self.definition:
            return None
        return self.definition.structure.poly if self.definition.structure else None

    @property
    def outline(self) -> Optional[Otl2]:
        bitmap = self.get_single("CIBO")
        return bitmap.outline if isinstance(bitmap, Cibo) else None

    @property
    def bitmap_name(self) -> Optional[str]:
        bitmap = self.get_single("CIBO")
        if isinstance(bitmap, Cibo):
            return bitmap.bitmap_name
        name = self.get_single("NAM2")
        return name.name if isinstance(name, Nam2) else None

    @property
    def is_animated(self) -> bool:
        return self.get_single("BANI") is not None

    def validate(self) -> List[str]:
        """Return a list of structural-error paths; an empty list means valid.

        An ``AREA`` is considered textured when it has a direct ``OBJT``
        bitmap reference container; that container must then provide a
        complete ``OBJT/CIBO/NAM2`` bitmap reference path.
        """
        errors = []
        definitions = self.get_direct_all("ADE ")
        if not definitions:
            errors.append("AREA: missing direct ADE  form")
        else:
            if len(definitions) > 1:
                errors.append("AREA: duplicate direct ADE  forms")
            definition = definitions[0]
            if not isinstance(definition, Ade):
                errors.append("AREA: direct ADE  child is not an ADE  form")
            else:
                errors.extend("AREA/" + error for error in definition.validate())

        bitmap_refs = self.get_direct_all("OBJT")
        if bitmap_refs:
            if len(bitmap_refs) > 1:
                errors.append("AREA: duplicate OBJT/CIBO/NAM2 bitmap references")
            bitmap_ref = bitmap_refs[0]
            if not isinstance(bitmap_ref, Objt):
                errors.append("AREA: missing OBJT/CIBO/NAM2 bitmap reference")
            else:
                cibo_refs = bitmap_ref.get_direct_all("CIBO")
                if len(cibo_refs) == 1 and isinstance(cibo_refs[0], Cibo):
                    nam2_refs = cibo_refs[0].get_direct_all("NAM2")
                    if len(nam2_refs) > 1:
                        errors.append("AREA: duplicate OBJT/CIBO/NAM2 bitmap references")
                    elif len(nam2_refs) != 1 or not isinstance(nam2_refs[0], Nam2):
                        errors.append("AREA: missing OBJT/CIBO/NAM2 bitmap reference")
                else:
                    if len(cibo_refs) > 1:
                        errors.append("AREA: duplicate OBJT/CIBO/NAM2 bitmap references")
                    errors.append("AREA: missing OBJT/CIBO/NAM2 bitmap reference")
        return errors


@register_form("ROOT")
class Root(Form):
    def __init__(self, form_type="ROOT", sub_chunks=None):
        super(Root, self).__init__(form_type, sub_chunks)


@register_form("KIDS")
class Kids(Form):
    def __init__(self, form_type="KIDS", sub_chunks=None):
        super(Kids, self).__init__(form_type, sub_chunks)


@register_form("OBJT")
class Objt(Form):
    def __init__(self, form_type="OBJT", sub_chunks=None):
        super(Objt, self).__init__(form_type, sub_chunks)


@register_form("ADES")
class Ades(Form):
    """A collection of direct object definitions."""
    def __init__(self, form_type="ADES", sub_chunks=None):
        super(Ades, self).__init__(form_type, sub_chunks)

    @property
    def objects(self) -> List[Objt]:
        return [child for child in self.get_direct_all("OBJT") if isinstance(child, Objt)]


@register_form("BASE")
class Base(Form):
    def __init__(self, form_type="BASE", sub_chunks=None):
        super(Base, self).__init__(form_type, sub_chunks)


@register_form("SKLT")
class Sklt(Form):
    def __init__(self, form_type="SKLT", sub_chunks=None):
        super(Sklt, self).__init__(form_type, sub_chunks)


def make_chunk(chunk_id: str, binary_data: bytes) -> Chunk:
    """Create the concrete chunk type registered for *chunk_id*."""
    chunk_class = chunk_registry.get(chunk_id, Chunk)
    chunk = chunk_class(chunk_id)
    chunk.set_binary_data(binary_data)
    return chunk


def make_form(form_type: str, sub_chunks: List[Union[Form, Chunk]]) -> Form:
    """Create the concrete form type registered for *form_type*.

    Parsing constructs the registered form directly, so children are
    immediately usable through their concrete interfaces (for example,
    ``Emrs.emrs_name`` and ``Vbmp.save_to_bmp``).
    """
    form_class = form_registry.get(form_type, Form)
    return form_class(form_type, sub_chunks)


def parse_set_descriptor(set_number="1"):
    sdf = []
    path = os.path.join("assets", "sets", "set{}", "scripts", "set.sdf")
    with open(path.format(set_number), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b" ")[0].decode("ascii")
            sdf.append(base)
    logging.info("sdf: {}".format(sdf))
    return sdf


def parse_visproto(set_number="1"):
    visproto = []
    path = os.path.join("assets", "sets", "set{}", "scripts", "visproto.lst")
    with open(path.format(set_number), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            visproto.append(base)
    logging.info("visproto: {}".format(visproto))
    return visproto


def parse_slurps(set_number="1"):
    slurps = []
    path = os.path.join("assets", "sets", "set{}", "scripts", "slurps.lst")
    with open(path.format(set_number), "rb") as f:
        for line in f:
            if b">" in line:
                break
            base = line.split(b";")[0].decode("ascii").strip()
            slurps.append(base)
    logging.info("slurps: {}".format(slurps))
    return slurps


def build_set(set_number="1") -> Mc2:
    """Build an MC2 form for a set without writing an output file."""
    sdf = parse_set_descriptor(set_number)
    visproto = parse_visproto(set_number)
    slurps = parse_slurps(set_number)
    mc2 = Mc2()

    path = os.path.join("assets", "sets", "set{}", "*.*")
    bitmaps = glob.glob(path.format(set_number))
    bitmaps.sort()

    # Add bitmaps to Embd
    for bitmap in bitmaps:
        logging.info(bitmap)
        mc2.add_image_from_file(bitmap)

    path = os.path.join("assets", "sets", "set{}", "Skeleton", "*.json")
    skeletons = glob.glob(path.format(set_number))
    skeletons.sort()

    # Add skeletons to Embd
    for skeleton in skeletons:
        logging.info(skeleton)
        mc2.add_skeleton_from_json_file(skeleton)

    path = os.path.join("assets", "sets", "set{}", "rsrcpool", "*.json")
    animations = glob.glob(path.format(set_number))
    animations.sort()

    # Add animations to Embd
    for animation in animations:
        logging.info(animation)
        mc2.add_animation_from_json_file(animation)

    path = os.path.join("assets", "sets", "set{}", "objects", "vehicles", "{}.json")
    vehicles = [path.format(set_number, x.replace("base", "bas")) for x in visproto]
    # vehicles.sort()  # DONT SORT SET.BAS!! ORDER MUST MATCH THE SCRIPT

    for vehicle in vehicles:
        logging.info(vehicle)
        mc2.add_vehicle_from_json_file(vehicle)

    path = os.path.join("assets", "sets", "set{}", "objects", "buildings", "{}.json")
    buildings = [path.format(set_number, x.replace("base", "bas")) for x in sdf]
    # buildings.sort()  # DONT SORT SET.BAS!! ORDER MUST MATCH THE SCRIPT

    for building in buildings:
        logging.info(building)
        mc2.add_building_from_json_file(building)

    path = os.path.join("assets", "sets", "set{}", "objects", "ground", "{}.json")
    grounds = [path.format(set_number, x.replace("base", "bas")) for x in slurps]
    # grounds.sort()  # DONT SORT SET.BAS!! ORDER MUST MATCH THE SCRIPT

    for ground in grounds:
        logging.info(ground)
        mc2.add_ground_from_json_file(ground)

    return mc2


def compile_set_bas(set_number="1") -> None:
    """Build a set and save its MC2 form to the standard output path."""
    path = os.path.join("output", "set{}_compiled.bas")
    build_set(set_number).save_to_file(path.format(set_number))


def compile_bee_box(set_number="1"):
    path = os.path.join("assets", "sets", "set{}", "objects", "beebox.bas.json")
    bee_box = Form().from_json_file(path.format(set_number))

    path = os.path.join("output", "data", "set", "objects", "beebox.bas")
    bee_box.save_to_file(path)


def compile_mc2_res():
    path = os.path.join("assets", "mc2res", "skeleton", "*")
    for resource in glob.glob(path):
        s = Form().from_json_file(resource)
        file_name = os.path.basename(resource.replace(".json", ""))
        path = os.path.join("output", "data", "mc2res", "skeleton", "{}")
        s.save_to_file(path.format(file_name))


def compile_single_files(set_number="1"):
    # Delete output folder if it exists
    if os.path.exists("output"):
        shutil.rmtree("output")

    # Create necessary folders that have not been created yet
    check_dirs = [os.path.join("output", "data", "set", "rsrcpool"),
                  os.path.join("output", "data", "set", "Skeleton"),
                  os.path.join("output", "data", "set", "objects"),
                  os.path.join("output", "data", "mc2res", "skeleton"),
                  ]
    for dirs in check_dirs:
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    # Copy static files
    for static_asset in ["hi", "palette", "remap", "scripts"]:
        src = os.path.join("assets", "sets", "set{}", "{}")
        dst = os.path.join("output", "data", "set", "{}")
        shutil.copytree(src.format(set_number, static_asset),
                        dst.format(static_asset))

    # Compile beebox scripts and mc2 resources
    compile_bee_box(set_number)
    compile_mc2_res()

    # Compile images
    path = os.path.join("assets", "sets", "set{}", "*.*")
    bitmaps = glob.glob(path.format(set_number))
    bitmaps.sort()

    for bitmap in bitmaps:
        logging.info(bitmap)
        try:
            new_vbmp = Vbmp().load_image(bitmap)
            path = os.path.join("output", "data", "set", "{}")
            new_vbmp.save_to_file(path.format(os.path.splitext(os.path.basename(bitmap))[0]))
        except InvalidImage:
            logging.WARN("Skipping invalid image file {}".format(bitmap))

    # Compile animations
    path = os.path.join("assets", "sets", "set{}", "rsrcpool", "*.json")
    animations = glob.glob(path.format(set_number))
    animations.sort()

    for animation in animations:
        logging.info(animation)
        resource_name = os.path.splitext(os.path.basename(animation))[0]

        vanm_form = Form().from_json_file(animation)
        path = os.path.join("output", "data", "set", "rsrcpool", "{}")
        vanm_form.save_to_file(path.format(resource_name))

    # Compile skeletons
    path = os.path.join("assets", "sets", "set{}", "Skeleton", "*.json")
    skeletons = glob.glob(path.format(set_number))
    skeletons.sort()

    for skeleton in skeletons:
        logging.info(skeleton)

        sklt_form = Form().from_json_file(skeleton)
        path = os.path.join("output", "data", "set", "Skeleton", "{}")
        sklt_form.save_to_file(path.format(os.path.splitext(os.path.basename(skeleton))[0]))

    # Compile vehicles
    path = os.path.join("assets", "sets", "set{}", "objects", "vehicles", "*.json")
    vehicles = glob.glob(path.format(set_number))
    vehicles.sort()

    for vehicle in vehicles:
        logging.info(vehicle)
        resource_name = os.path.splitext(os.path.basename(vehicle))[0]

        sklt_form = Form().from_json_file(vehicle)
        path = os.path.join("output", "data", "set", "objects", "{}")
        sklt_form.save_to_file(path.format(resource_name))

    # Compile buildings
    path = os.path.join("assets", "sets", "set{}", "objects", "buildings", "*.json")
    buildings = glob.glob(path.format(set_number))
    buildings.sort()

    for building in buildings:
        logging.info(building)
        resource_name = os.path.splitext(os.path.basename(building))[0]

        sklt_form = Form().from_json_file(building)
        path = os.path.join("output", "data", "set", "objects", "{}")
        sklt_form.save_to_file(path.format(resource_name))

    # Compile ground
    path = os.path.join("assets", "sets", "set{}", "objects", "ground", "*.json")
    grounds = glob.glob(path.format(set_number))
    grounds.sort()

    for ground in grounds:
        logging.info(ground)
        resource_name = os.path.splitext(os.path.basename(ground))[0]

        sklt_form = Form().from_json_file(ground)
        path = os.path.join("output", "data", "set", "objects", "{}")
        sklt_form.save_to_file(path.format(resource_name))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        set_num = sys.argv[1]
    else:
        set_num = "1"

    # Remove leading "set" if found
    if set_num.startswith("set"):
        set_num = set_num[3:]

    # Remove trailing slash if found
    if set_num.endswith("/") or set_num.endswith("\\"):
        set_num = set_num[:-1]

    compile_single_files(set_num)
    compile_set_bas(set_num)
