import compile
import unittest

test_chunk_id = "TEST"
data_bytes = b"This is bytes"
data_string = "This is not bytes"
c = compile.Chunk(test_chunk_id)


class TestChunk(unittest.TestCase):

    def test_init(self):
        self.assertEqual(c.chunk_id, test_chunk_id)

    def test_validated_id_1(self):
        self.assertEqual(c.validate_id(test_chunk_id), test_chunk_id)

    def test_validated_id_2(self):
        with self.assertRaises(ValueError) as context:
            c.validate_id(b"TEST")
        self.assertTrue("chunk_id must be a string" in str(context.exception))

    def test_validated_id_3(self):
        with self.assertRaises(ValueError) as context:
            c.validate_id("TES")
        self.assertTrue("chunk_id must be 4" in str(context.exception))

    def test_validate_data_1(self):
        self.assertEqual(c.validate_data(data_bytes), data_bytes)

    def test_validate_data_2(self):
        with self.assertRaises(ValueError) as context:
            c.validate_data(data_string)
        self.assertTrue("chunk_data must be bytes" in str(context.exception))

    def test_set_binary_data(self):
        c.set_binary_data(data_bytes)
        self.assertEqual(c.get_data(), data_bytes)

    def test_full_data(self):
        c.chunk_id = test_chunk_id
        c.set_binary_data(data_bytes)
        self.assertEqual(c.full_data(), b"TEST\x00\x00\x00\rThis is bytes\x00")

    def test_size(self):
        c.set_binary_data(data_bytes)
        self.assertEqual(c.size(), len(data_bytes))

    def test_load_data_from_file_1(self):
        with self.assertRaises(FileNotFoundError) as context:
            c.load_data_from_file("a_file_not_exist")
        self.assertTrue("could not be found" in str(context.exception))

    def test_load_data_from_file_2(self):
        with self.assertRaises(ValueError) as context:
            c.load_data_from_file("test/test_form.bin")
        self.assertTrue("FORM file into a chunk" in str(context.exception))

    def test_load_data_from_file_3(self):
        c.set_binary_data(data_bytes)
        c.load_data_from_file("test/test_chunk.bin")
        self.assertNotEqual(c.get_data(), data_bytes)
        self.assertNotEqual(c.data, data_bytes)

    # TODO save_data_to_file
    # TODO save_to_file

    def test_save_to_class(self):
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        cl = c.to_class()
        self.assertTrue(isinstance(cl, compile.Name))
        self.assertTrue(cl.zero_terminated)
        self.assertEqual(cl.full_data(), b'NAME\x00\x00\x00\x05TEST\x00\x00')

    def test_to_json(self):
        c.chunk_id = "NAME"
        c.data = b"TEST\x00"
        j = c.to_json()
        self.assertTrue('"name": "TEST"' in j)
        self.assertTrue('"zero_terminated": true' in j)

    # TODO from_json
    # TODO from_json_generic


class TestForm(unittest.TestCase):

    def test_finish_me(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
