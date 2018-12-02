import compile
import unittest


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
            c.load_data_from_file("test/bin/test_form.bin")
        self.assertTrue("FORM file into a chunk" in str(context.exception))

    def test_load_data_from_file_3(self):
        c = compile.Chunk()
        data_bytes = b"This is bytes"
        c.set_binary_data(data_bytes)
        c.load_data_from_file("test/bin/test_chunk.bin")
        self.assertNotEqual(c.get_data(), data_bytes)
        self.assertNotEqual(c.data, data_bytes)

    # TODO save_data_to_file (Can use io.BytesIO to provide a fake file stream)
    # TODO save_to_file (Can use io.BytesIO to provide a fake file stream)

    def test_to_class(self):
        c = compile.Chunk()
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        cl = c.to_class()
        self.assertTrue(isinstance(cl, compile.Name))
        self.assertTrue(cl.zero_terminated)
        self.assertEqual(cl.full_data(), b'NAME\x00\x00\x00\x05TEST\x00\x00')

    # TODO to_class (error condition)

    def test_to_json(self):
        c = compile.Chunk()
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        j = c.to_json()
        self.assertTrue('"name": "TEST"' in j)
        self.assertTrue('"zero_terminated": true' in j)

    # TODO from_json
    # TODO from_json_generic

    def test_chunk_classes(self):
        import glob
        chunks = glob.glob("test/bin/chunks/*.bin")
        for chunk in chunks:
            c = compile.Chunk().load_from_file(chunk)
            cl = c.to_class()
            fd = cl.full_data()
            j = cl.to_json()

    def test_form_classes(self):
        import glob
        chunks = glob.glob("test/bin/forms/*.bin")
        for chunk in chunks:
            c = compile.Form().load_from_file(chunk)
            cl = c.to_class()
            fd = cl.full_data()
            j = cl.to_json()


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

    def test_to_class_1(self):
        c = compile.Chunk()
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        f = compile.Form("VBMP", [c])
        cl = f.to_class()
        self.assertTrue(isinstance(cl, compile.Vbmp))
        self.assertTrue(isinstance(cl.child(0).to_class(), compile.Name))

    # TODO to_class (error condition)

    def test_to_json(self):
        c = compile.Chunk("NAME")
        c.data = b"this_is_name\x00"
        f = compile.Form("TFRM", [c])
        j = f.to_json()
        j_mod = j.replace("\n", "").replace(" ", "")
        self.assertEqual(j_mod, '{"TFRM":[{"NAME":{"name":"this_is_name","zero_terminated":true}}]}')

    # TODO from_json x4

    def test_size(self):
        c = compile.Chunk("CHNK")
        c.data = b"TEST CHUNK DATA"
        f = compile.Form("TFRM", [c])
        self.assertEqual(f.size(), len(b'TFRMCHNK\x00\x00\x00\x0fTEST CHUNK DATA\x00'))

    def test_get_all_form_by_type_1(self):
        m = compile.Mc2()
        v = compile.Vbmp()
        s = compile.Strc()
        f = compile.Form("SKLT", [m, v, s])
        self.assertEqual(f.get_all_form_by_type("MC2 "), [m])
        self.assertEqual(f.get_all_form_by_type("NONE"), [])

    def test_get_all_chunks_by_id_1(self):
        c1 = compile.Chunk("TEST")
        c2 = compile.Chunk("TEST")
        c3 = compile.Form("TEST")  # This is a Form() and should not be returned
        c4 = compile.Chunk("NEXT")
        c5 = compile.Chunk("TEXT")
        f = compile.Form("ABCD", [c1, c2, c3, c4, c5])
        # https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order
        import collections
        l1 = collections.Counter(f.get_all_chunks_by_id("TEST"))
        l2 = collections.Counter([c1, c2])
        self.assertEqual(l1, l2)

    def test_get_all_chunks_by_id_2(self):
        c1 = compile.Chunk("TEST")
        c2 = compile.Chunk("TEST")
        c3 = compile.Chunk("NEXT")
        c4 = compile.Chunk("TEXT")
        c5 = compile.Form("XYZZ")  # This is a Form() and should not be returned
        f = compile.Form("ABCD", [c1, c2, c3, c4, c5])
        l1 = f.get_all_chunks_by_id("XYZZ")
        self.assertEqual(l1, [])

    def test_get_single_form_by_type_1(self):
        c1 = compile.Form("ABC1")
        c2 = compile.Form("ABC2")
        c3 = compile.Form("ABC3")
        f = compile.Form("TEST", [c1, c2, c3])
        self.assertEqual(f.get_single_form_by_type("ABCD"), None)
        self.assertEqual(f.get_single_form_by_type("ABC3"), c3)

    def test_get_single_form_by_type_2(self):
        c = compile.Chunk("ABCD")
        f = compile.Form("TEST", [c])
        self.assertEqual(f.get_single_form_by_type("ABCD"), None)

    def test_get_single_chunk_by_id_1(self):
        c1 = compile.Chunk("ABC1")
        c2 = compile.Chunk("ABC2")
        c3 = compile.Chunk("ABC3")
        f = compile.Form("TEST", [c1, c2, c3])
        self.assertEqual(f.get_single_chunk_by_id("ABCD"), None)
        self.assertEqual(f.get_single_chunk_by_id("ABC3"), c3)

    def test_get_single_chunk_by_id_2(self):
        c = compile.Form("ABCD")
        f = compile.Form("TEST", [c])
        self.assertEqual(f.get_single_chunk_by_id("ABCD"), None)

    def test_load_from_file_1(self):
        f = compile.Form()
        with self.assertRaises(FileNotFoundError) as context:
            f.load_from_file("not_a_file")
        self.assertTrue("file could not be found" in str(context.exception))

    def test_load_from_file_2(self):
        f = compile.Form("TEST")
        f.load_from_file("test/bin/test_form.bin")
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


if __name__ == "__main__":
    unittest.main()
