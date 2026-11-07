import compile
import hashlib
import io
import json
import os
import tempfile
import unittest

from PIL import Image


class TestChunk(unittest.TestCase):

    def test_init(self):
        test_chunk_id = "TEST"
        c = compile.Chunk(test_chunk_id)
        self.assertEqual(c.chunk_id, test_chunk_id)

    def test_validated_id_1(self):
        test_chunk_id = "TEST"
        c = compile.Chunk(test_chunk_id)
        self.assertEqual(c.validate_id(test_chunk_id), test_chunk_id)

    def test_validated_id_2(self):
        c = compile.Chunk()
        with self.assertRaises(ValueError) as context:
            c.validate_id(b"TEST")
        self.assertTrue("chunk_id must be a string" in str(context.exception))

    def test_validated_id_3(self):
        c = compile.Chunk()
        with self.assertRaises(ValueError) as context:
            c.validate_id("TES")
        self.assertTrue("chunk_id must be 4" in str(context.exception))

    def test_validate_data_1(self):
        c = compile.Chunk()
        data_bytes = b"This is bytes"
        self.assertEqual(c.validate_data(data_bytes), data_bytes)

    def test_validate_data_2(self):
        c = compile.Chunk()
        data_string = "This is not bytes"
        with self.assertRaises(ValueError) as context:
            c.validate_data(data_string)
        self.assertTrue("chunk_data must be bytes" in str(context.exception))

    def test_set_binary_data(self):
        test_chunk_id = "TEST"
        c = compile.Chunk(test_chunk_id)
        data_bytes = b"This is bytes"
        c.set_binary_data(data_bytes)
        self.assertEqual(c.get_data(), data_bytes)

    def test_full_data(self):
        c = compile.Chunk()
        data_bytes = b"This is bytes"
        c.chunk_id = "TEST"
        c.set_binary_data(data_bytes)
        self.assertEqual(c.full_data(), b"TEST\x00\x00\x00\rThis is bytes\x00")

    def test_size(self):
        c = compile.Chunk()
        data_bytes = b"This is bytes"
        c.set_binary_data(data_bytes)
        self.assertEqual(c.size(), len(data_bytes))

    def test_load_data_from_file_1(self):
        c = compile.Chunk()
        with self.assertRaises(FileNotFoundError) as context:
            c.load_data_from_file("a_file_not_exist")
        self.assertTrue("could not be found" in str(context.exception))

    def test_load_data_from_file_2(self):
        c = compile.Chunk()
        with self.assertRaises(ValueError) as context:
            data_file = os.path.join("test", "bin", "test_form.bin")
            c.load_data_from_file(data_file)
        self.assertTrue("FORM file into a chunk" in str(context.exception))

    def test_load_data_from_file_3(self):
        c = compile.Chunk()
        data_bytes = b"This is bytes"
        c.set_binary_data(data_bytes)
        data_file = os.path.join("test", "bin", "test_chunk.bin")
        c.load_data_from_file(data_file)
        self.assertNotEqual(c.get_data(), data_bytes)
        self.assertNotEqual(c.data, data_bytes)

    # TODO save_data_to_file (Can use io.BytesIO to provide a fake file stream)
    # TODO save_to_file (Can use io.BytesIO to provide a fake file stream)

    def test_to_json(self):
        c = compile.Chunk()
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        j = c.to_dict()
        self.assertTrue("name" in j["NAME"])
        self.assertEqual(j["NAME"]["name"], "TEST")
        self.assertTrue("zero_terminated" in j["NAME"])
        self.assertTrue(j["NAME"]["zero_terminated"])


    # TODO from_json
    # TODO from_json_generic

    def test_chunk_classes(self):
        import glob
        chunks = glob.glob("test/bin/chunks/*.bin")
        for chunk in chunks:
            with open(chunk, "rb") as f:
                data = f.read()
            parsed = compile.Form().parse_stream(io.BytesIO(data))[0]
            self.assertEqual(parsed.full_data(), data)

    def test_form_classes(self):
        import glob
        chunks = glob.glob("test/bin/forms/*.bin")
        for chunk in chunks:
            with open(chunk, "rb") as f:
                data = f.read()
            parsed = compile.Form().parse_stream(io.BytesIO(data))[0]
            self.assertEqual(parsed.full_data(), data)

    def test_original_form_fixtures(self):
        import glob
        fixtures = glob.glob(os.path.join("test", "bin", "orig", "*.bin"))
        self.assertTrue(fixtures)
        for fixture in fixtures:
            with self.subTest(form=os.path.basename(fixture)):
                with open(fixture, "rb") as f:
                    data = f.read()
                parsed = compile.Form().parse_stream(io.BytesIO(data))[0]

                expected_class = compile.form_registry[parsed.form_type]
                self.assertIs(type(parsed), expected_class)
                self.assertEqual(parsed.full_data(), data)

                rebuilt = compile.Form().from_json(parsed.to_json())
                self.assertEqual(rebuilt.full_data(), data)

                if isinstance(parsed, compile.Area):
                    self.assertEqual(parsed.validate(), [])
                if isinstance(parsed, compile.Ade):
                    self.assertEqual(parsed.validate(), [])

    def test_parser_uses_registered_types(self):
        name = compile.Nam2()
        name.name = "texture"
        name.zero_terminated = True
        amsh = compile.Amsh()
        amsh.add_chunk(name)

        parsed = compile.Form().parse_stream(io.BytesIO(amsh.full_data()))[0]

        self.assertIsInstance(parsed, compile.Amsh)
        self.assertIsInstance(parsed.get_single("NAM2"), compile.Nam2)

    def test_registries_are_separate(self):
        self.assertIs(compile.chunk_registry["NAME"], compile.Name)
        self.assertIs(compile.form_registry["VBMP"], compile.Vbmp)
        self.assertFalse(set(compile.chunk_registry) & set(compile.form_registry))

    def test_form_constructors_accept_sub_chunks(self):
        root = compile.Root()
        embd = compile.Embd("EMBD", [root])

        self.assertEqual(embd.sub_chunks, [root])

    def test_vanm_area_and_cibo_forms(self):
        data = compile.Data()
        data.class_id = "ilbm.class"
        data.frames = [{"frame_time": 80,
                        "vbmp_name": "FX2.ILBM",
                        "vbmp_coords": [[0, 0], [1, 0], [1, 1]]}]
        vanm = compile.Vanm(sub_chunks=[data])

        nam2 = compile.Nam2()
        nam2.name = "FX2.ILBM"
        outline = compile.Otl2()
        outline.points = [[0, 0], [1, 0], [1, 1]]
        cibo = compile.Cibo(sub_chunks=[nam2, outline])
        definition_strc = compile.Strc()
        definition_strc.strc_type = compile.Strc.STRC_ADE
        definition_strc.version = 1
        definition_strc.poly = 3
        definition = compile.Ade(sub_chunks=[definition_strc])
        area = compile.Area(sub_chunks=[definition, cibo])

        parsed_vanm = compile.Form().parse_stream(io.BytesIO(vanm.full_data()))[0]
        parsed_area = compile.Form().parse_stream(io.BytesIO(area.full_data()))[0]

        self.assertIsInstance(parsed_vanm, compile.Vanm)
        self.assertEqual(parsed_vanm.bitmap_names, ["FX2.ILBM"])
        self.assertIsInstance(parsed_area, compile.Area)
        self.assertEqual(parsed_area.bitmap_name, "FX2.ILBM")
        self.assertEqual(parsed_area.polygon_index, 3)
        self.assertEqual(parsed_area.outline.points, outline.points)
        self.assertFalse(parsed_area.is_animated)

    def test_direct_child_lookup_does_not_descend(self):
        nested_name = compile.Name()
        nested_name.name = "nested"
        nested = compile.Form("NEST", [nested_name])
        form = compile.Form("TEST", [nested])

        self.assertEqual(form.get_direct_all("NAME"), [])
        self.assertIsNone(form.get_direct_single("NAME"))
        self.assertIs(form.get_single("NAME"), nested_name)

    def test_ades_objects_only_returns_direct_objt_forms(self):
        direct_object = compile.Objt()
        nested_object = compile.Objt()
        ades = compile.Ades(sub_chunks=[direct_object, compile.Kids(sub_chunks=[nested_object])])

        parsed_ades = compile.Form().parse_stream(io.BytesIO(ades.full_data()))[0]

        self.assertIsInstance(parsed_ades, compile.Ades)
        self.assertEqual(parsed_ades.objects, [parsed_ades.sub_chunks[0]])
        self.assertIsInstance(parsed_ades.objects[0], compile.Objt)

    def test_sklc_exposes_its_direct_skeleton_name(self):
        name = compile.Name()
        name.name = "Skeleton/VP_NEU05.sklt"
        sklc = compile.Sklc(sub_chunks=[name])

        parsed_sklc = compile.Form().parse_stream(io.BytesIO(sklc.full_data()))[0]

        self.assertIsInstance(parsed_sklc, compile.Sklc)
        self.assertEqual(parsed_sklc.skeleton_name, "Skeleton/VP_NEU05.sklt")

    def test_validate_reports_missing_direct_children(self):
        # A form with no children at all misses every mandatory reference.
        self.assertEqual(compile.Ade().validate(), ["ADE : missing direct STRC chunk"])
        self.assertEqual(compile.Vanm().validate(), ["VANM: missing direct DATA chunk"])
        self.assertEqual(compile.Cibo().validate(), ["CIBO: missing direct NAM2 chunk"])
        self.assertEqual(compile.Area().validate(), ["AREA: missing direct ADE  form"])

        ade = compile.Ade(sub_chunks=[compile.Strc()])
        self.assertEqual(ade.validate(), ["ADE : direct STRC chunk is not a STRC_ADE structure"])

        nam2 = compile.Nam2()
        nam2.name = "FX2.ILBM"
        complete_cibo = compile.Cibo(sub_chunks=[nam2])
        complete_vanm = compile.Vanm(sub_chunks=[compile.Data()])
        self.assertEqual(complete_cibo.validate(), [])
        self.assertEqual(complete_vanm.validate(), [])

    def test_validate_reports_duplicate_direct_children(self):
        self.assertEqual(compile.Ade(sub_chunks=[compile.Strc(), compile.Strc()]).validate(),
                         ["ADE : duplicate direct STRC chunks", "ADE : direct STRC chunk is not a STRC_ADE structure"])
        self.assertEqual(compile.Vanm(sub_chunks=[compile.Data(), compile.Data()]).validate(),
                         ["VANM: duplicate direct DATA chunks"])
        self.assertEqual(compile.Cibo(sub_chunks=[compile.Nam2(), compile.Nam2()]).validate(),
                         ["CIBO: duplicate direct NAM2 chunks"])
        self.assertEqual(compile.Area(sub_chunks=[compile.Ade(), compile.Ade()]).validate(),
                         ["AREA: duplicate direct ADE  forms",
                          "AREA/ADE : missing direct STRC chunk"])

    def test_area_validate_reports_duplicate_bitmap_references(self):
        definition = compile.Ade()
        self.assertEqual(compile.Area(sub_chunks=[definition]).validate(),
                         ["AREA/ADE : missing direct STRC chunk"])

        complete_objt = self.make_textured_area().get_direct_single("OBJT")
        complete_ade = self.make_textured_area().get_direct_single("ADE ")
        objt = compile.Objt(sub_chunks=[compile.Clid()])
        self.assertEqual(compile.Area(sub_chunks=[complete_ade, objt, objt]).validate(),
                         ["AREA: duplicate OBJT/CIBO/NAM2 bitmap references",
                          "AREA: missing OBJT/CIBO/NAM2 bitmap reference"])

        nam2 = compile.Nam2()
        nam2.name = "BAGGER.ILBM"
        objt = compile.Objt(sub_chunks=[compile.Clid(),
                                        compile.Cibo(sub_chunks=[nam2, compile.Nam2()])])
        self.assertEqual(compile.Area(sub_chunks=[complete_ade, objt]).validate(),
                         ["AREA: duplicate OBJT/CIBO/NAM2 bitmap references"])

    def test_area_validate_reports_paths_with_context(self):
        # AREA/ADE : missing direct STRC
        definition = compile.Ade()
        self.assertEqual(compile.Area(sub_chunks=[definition]).validate(),
                         ["AREA/ADE : missing direct STRC chunk"])

    def test_textured_area_validate_requires_complete_bitmap_reference(self):
        structure = compile.Strc()
        structure.strc_type = compile.Strc.STRC_ADE
        definition = compile.Ade(sub_chunks=[structure])
        textured_area = self.make_textured_area()
        self.assertEqual(textured_area.validate(), [])

        # OBJT without a CIBO is an incomplete bitmap reference.
        objt = compile.Objt(sub_chunks=[compile.Clid()])
        broken = compile.Area(sub_chunks=[definition, objt])
        self.assertEqual(broken.validate(), ["AREA: missing OBJT/CIBO/NAM2 bitmap reference"])

        # A chunk with the OBJT ID is not a bitmap-reference form.
        broken = compile.Area(sub_chunks=[definition, compile.Chunk("OBJT")])
        self.assertEqual(broken.validate(), ["AREA: missing OBJT/CIBO/NAM2 bitmap reference"])

        # CIBO without a NAM2 is an incomplete bitmap reference.
        objt = compile.Objt(sub_chunks=[compile.Clid(), compile.Cibo()])
        broken = compile.Area(sub_chunks=[definition, objt])
        self.assertEqual(broken.validate(), ["AREA: missing OBJT/CIBO/NAM2 bitmap reference"])

    @staticmethod
    def make_textured_area():
        structure = compile.Strc()
        structure.strc_type = compile.Strc.STRC_ADE
        definition = compile.Ade(sub_chunks=[structure])
        nam2 = compile.Nam2()
        nam2.name = "BAGGER.ILBM"
        objt = compile.Objt(sub_chunks=[compile.Clid(), compile.Cibo(sub_chunks=[nam2])])
        return compile.Area(sub_chunks=[definition, objt])

    def test_real_textured_area_fixture_validates(self):
        fixture = os.path.join("assets", "sets", "set3_xp", "objects",
                               "vehicles", "VPwRT.bas.json")
        parsed = compile.Form().from_json_file(fixture)
        areas = parsed.get_all("AREA")
        self.assertTrue(areas)
        for area in areas:
            self.assertEqual(area.validate(), [])

    def test_vbmp_image_round_trip_uses_pillow(self):
        with tempfile.TemporaryDirectory() as directory:
            source = os.path.join(directory, "source.bmp")
            output = os.path.join(directory, "output.bmp")
            Image.new("RGB", (256, 256), "red").save(source)

            vbmp = compile.Vbmp().load_image(source)
            vbmp.save_to_bmp(output)

            self.assertEqual(vbmp.get_single("BODY").size(), 256 * 256)
            with Image.open(output) as exported:
                self.assertEqual(exported.size, (256, 256))

    def test_standard_palette_is_loaded_from_cmap(self):
        palette = compile.palette_from_pal(compile.DEFAULT_PALETTE_FILE)

        self.assertEqual(len(palette), 256)
        self.assertEqual(palette[:2], [0xFFFFFF00, 0xFFFFFFFF])
        self.assertEqual(compile.palette_data(palette)[:6], b"\xff\xff\x00\xff\xff\xff")


class TestForm(unittest.TestCase):

    def test_init_1(self):
        form_type = "TEST"
        f = compile.Form(form_type)
        self.assertEqual(f.form_type, form_type)
        self.assertEqual(f.sub_chunks, [])

    def test_init_2(self):
        form_type = "TEST"
        sc = compile.Chunk()
        f = compile.Form(form_type, [sc])
        self.assertEqual(f.form_type, form_type)
        self.assertEqual(f.sub_chunks, [sc])

    def test_validate_form_type_1(self):
        f = compile.Form()
        with self.assertRaises(ValueError) as context:
            f.validate_form_type(b"BYTE")

    def test_validate_form_type_2(self):
        f = compile.Form()
        with self.assertRaises(ValueError) as context:
            f.validate_form_type("FORM")

    def test_validate_form_type_3(self):
        f = compile.Form()
        with self.assertRaises(ValueError) as context:
            f.validate_form_type("TOOLONG")

    def test_validate_form_type_4(self):
        f = compile.Form()
        f.validate_form_type("GOOD")

    def test_validate_sub_chunks_1(self):
        f = compile.Form()
        sc = compile.Chunk()
        self.assertEqual(f.validate_sub_chunks([sc]), [sc])

    def test_validate_sub_chunks_2(self):
        f = compile.Form()
        self.assertEqual(f.validate_sub_chunks(None), [])

    def test_validate_sub_chunks_3(self):
        f = compile.Form()
        sc = compile.Chunk()
        with self.assertRaises(ValueError) as context:
            f.validate_sub_chunks(sc)
        self.assertTrue("must be a list" in str(context.exception))

    def test_child(self):
        c1 = compile.Chunk()
        c2 = compile.Chunk()
        c3 = compile.Chunk()
        f = compile.Form("TEST", [c1, c2, c3])
        self.assertEqual(f.child(0), c1)
        self.assertEqual(f.child(1), c2)
        self.assertEqual(f.child(2), c3)

    def test_get_data(self):
        c = compile.Chunk("CHNK")
        c.data = b"TEST CHUNK DATA"
        f = compile.Form("TFRM", [c])
        self.assertEqual(f.get_data(), b"TFRMCHNK\x00\x00\x00\x0fTEST CHUNK DATA\x00")

    def test_full_data(self):
        c = compile.Chunk("CHNK")
        c.data = b"TEST CHUNK DATA"
        f = compile.Form("TFRM", [c])
        self.assertEqual(f.full_data(), b"FORM\x00\x00\x00\x1cTFRMCHNK\x00\x00\x00\x0fTEST CHUNK DATA\x00")

    def test_to_json(self):
        c = compile.Chunk("NAME")
        c.data = b"this_is_name\x00"
        f = compile.Form("TFRM", [c])
        j = f.to_dict()
        self.assertDictEqual(j, {"TFRM":[{"NAME":{"name":"this_is_name","zero_terminated":True}}]})

    # TODO from_json x4

    def test_size(self):
        c = compile.Chunk("CHNK")
        c.data = b"TEST CHUNK DATA"
        f = compile.Form("TFRM", [c])
        self.assertEqual(f.size(), len(b'TFRMCHNK\x00\x00\x00\x0fTEST CHUNK DATA\x00'))

    def test_get_all_1(self):
        m = compile.Mc2()
        v = compile.Vbmp()
        s = compile.Strc()
        f = compile.Form("SKLT", [m, v, s])
        self.assertEqual(f.get_all("MC2 "), [m])
        self.assertEqual(f.get_all("NONE"), [])

    def test_get_all_2(self):
        c1 = compile.Chunk("TEST")
        c2 = compile.Chunk("TEST")
        c3 = compile.Form("TEST")
        c4 = compile.Chunk("NEXT")
        c5 = compile.Chunk("TEXT")
        f = compile.Form("ABCD", [c1, c2, c3, c4, c5])
        # https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order
        import collections
        l1 = collections.Counter(f.get_all("TEST"))
        l2 = collections.Counter([c1, c2, c3])
        self.assertEqual(l1, l2)

    def test_get_single_1(self):
        c1 = compile.Form("ABC1")
        c2 = compile.Form("ABC2")
        c3 = compile.Form("ABC3")
        c4 = compile.Form("ABC3")  # c4 comes after c3 and so it should not get returned
        f = compile.Form("TEST", [c1, c2, c3, c4])
        self.assertEqual(f.get_single("ABCD"), None)
        self.assertEqual(f.get_single("ABC3"), c3)

    def test_get_single_2(self):
        c1 = compile.Chunk("ABC1")
        c2 = compile.Chunk("ABC2")
        c3 = compile.Chunk("ABC3")
        c4 = compile.Chunk("ABC3")  # c4 comes after c3 and so it should not get returned
        f = compile.Form("TEST", [c1, c2, c3, c4])
        self.assertEqual(f.get_single("ABCD"), None)
        self.assertEqual(f.get_single("ABC3"), c3)

    def test_load_from_file_1(self):
        f = compile.Form()
        with self.assertRaises(FileNotFoundError) as context:
            f.load_from_file("not_a_file")
        self.assertTrue("file could not be found" in str(context.exception))

    def test_load_from_file_2(self):
        f = compile.Form("TEST")
        data_file = os.path.join("test", "bin", "test_form.bin")
        f.load_from_file(data_file)
        self.assertNotEqual(f.sub_chunks, [])
        self.assertNotEqual(f.form_type, "TEST")

    # TODO save_to_file (Can use io.BytesIO to provide a fake file stream)
    # TODO parse_stream

    def test_add_chunk(self):
        c1 = compile.Chunk()
        c2 = compile.Chunk()
        f = compile.Form()
        f.add_chunk(c1)
        f.add_chunk(c2)
        self.assertEqual(f.child(0), c1)
        self.assertEqual(f.child(1), c2)


class TestClasses(unittest.TestCase):
    # TODO Atts
    # TODO Atts (particle)
    # TODO Body
    # TODO Clid
    # TODO Data
    # TODO Emrs
    # TODO Head
    # TODO Nam2
    # TODO Name
    # TODO Olpl
    # TODO Otl2
    # TODO Pol2
    # TODO Poo2
    # TODO Sen2
    # TODO Strc (ADE)
    # TODO Strc (AREA)
    # TODO Strc (BANI)
    # TODO Strc (BASE)
    # TODO Strc (Unknown)

    def test_todo(self):
        pass


class TestIntegration(unittest.TestCase):

    # sha256 of the original game files "DATA/SETn/OBJECTS/SET.BAS", all
    # byte-identical with build_set(). Achieved via decompile_set_bas.py's
    # per-set resource manifest + Vbmp lossless palette-image loading.
    golden_shas = {
        "1": "cf1b7051108542d8892cde8c689141249c90069d9a00c97af230d2c5315ea5b5",
        "2": "c22568918da20a96986b3a3ef8ac4d1e70f071a0fb3293bca63b750feea79b2d",
        "3": "f5e5dd71480c44e1bd228d86e157af3d0f4eaf4e86f3fedd1d49b6bf0d7b5dcf",
        "4": "697c73e9e9d56046d5afb1f000b0f73d31ff054fe65530fbfe2125369e3b30fc",
        "5": "6caa5ed31e96cc8cc16ce1275f470557071deebe2aa160505e590ac536764667",
        "6": "60bb9f0980cb87285456b4e0a2691e75a4cdd51b875d6cfa293b982483efb63b",
    }

    def test_set1_golden_build(self):
        compiled_set = compile.build_set("1").full_data()
        self.assertByteExactSha(compiled_set, self.golden_shas["1"])

    def test_manifest_source_sha256(self):
        """Each resource manifest must record the sha256 of the original
        SET.BAS it was derived from, and it must match the golden sha."""
        for set_number, expected_sha in self.golden_shas.items():
            with self.subTest(set=set_number):
                path = compile.build_resource_manifest_path(set_number)
                if not os.path.isfile(path):
                    continue
                with open(path, "r") as f:
                    manifest = json.load(f)
                self.assertIn("resources", manifest)
                self.assertEqual(expected_sha,
                                 manifest["source_sha256"], "set" + set_number)

    def test_all_sets_byte_exact(self):
        for set_number, expected_sha in self.golden_shas.items():
            with self.subTest(set=set_number):
                compiled_set = compile.build_set(set_number).full_data()
                self.assertByteExactSha(compiled_set, expected_sha)

    def assertByteExactSha(self, compiled_bytes: bytes, expected_sha: str) -> None:
        self.assertEqual(hashlib.sha256(compiled_bytes).hexdigest(), expected_sha)



if __name__ == "__main__":
    unittest.main()
