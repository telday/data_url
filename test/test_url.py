import unittest
import uuid
import base64

from data_url import *

class TestUrlCreation(unittest.TestCase):
    # TODO tests with characters that need percent encoding
    def test_construct_data_url(self):
        mime_type = "text/plain"
        base64_encoded = False
        data = str(uuid.uuid4()).strip()
        url = construct_data_url(mime_type, base64_encoded, data)

        deconstructed_url = DataURL.from_url(url)

        self.assertEqual(mime_type, deconstructed_url.mime_type)
        self.assertEqual(base64_encoded, deconstructed_url.is_base64_encoded)
        self.assertEqual(data, deconstructed_url.data)

    def test_construct_data_url(self):
        mime_type = "text/plain"
        base64_encoded = False
        data = str(uuid.uuid4()).strip()
        raw_data = bytes(str(uuid.uuid4()), "UTF-8")
        data = base64.b64encode(raw_data).decode("UTF-8")

        url = construct_data_url(mime_type, base64_encoded, raw_data)

        deconstructed_url = DataURL.from_url(url)

        self.assertEqual(mime_type, deconstructed_url.mime_type)
        self.assertEqual(True, deconstructed_url.is_base64_encoded)
        self.assertEqual(raw_data, deconstructed_url.data)
        self.assertEqual(data, deconstructed_url.encoded_data)

class TestFromData(unittest.TestCase):
    def test_typing(self):
        with self.assertRaises(Exception) as context:
            DataURL.from_data("type", True, b"string")

        self.assertTrue('Data must be a string type' in str(context.exception))

    def test_string_no_encoding(self):
        self.mime_type = "text/plain"
        self.base64_encoded = False
        self.data = str(uuid.uuid4())
        self.raw_data = self.data
        self.expected_url = f"data:{self.mime_type},{self.data}"

        self.url = DataURL.from_data(self.mime_type, self.base64_encoded, self.data)

        self.assertEqual(type(self.url.data), str)
        self.run_assertions()

    def test_string_with_encoding(self):
        self.mime_type = "text/plain"
        self.base64_encoded = True
        self.raw_data = bytes(str(uuid.uuid4()), "UTF-8")
        self.data = base64.b64encode(self.raw_data).decode("UTF-8")
        self.expected_url = f"data:{self.mime_type};base64,{self.data}"

        self.url = DataURL.from_data(self.mime_type, self.base64_encoded, self.data)
        self.assertEqual(type(self.url.data), bytes)
        self.run_assertions()

    def run_assertions(self):
        self.assertEqual(self.url.mime_type, self.mime_type)
        self.assertEqual(self.url.data, self.raw_data)
        if self.base64_encoded:
            self.assertEqual(self.url.encoded_data, self.data)

        self.assertEqual(self.url.is_base64_encoded, self.base64_encoded)
        self.assertEqual(self.expected_url, self.url.url)

class TestFromByteData(unittest.TestCase):
    def test_byte_data(self):
        self.mime_type = "text/plain"
        self.base64_encoded = True
        self.raw_data = bytes(str(uuid.uuid4()), "UTF-8")
        self.data = base64.b64encode(self.raw_data).decode("UTF-8")
        self.expected_url = f"data:{self.mime_type};base64,{self.data}"

        self.url = DataURL.from_byte_data(self.mime_type, self.raw_data)
        self.assertEqual(type(self.url.data), bytes)
        self.run_assertions()

    def test_typing(self):
        with self.assertRaises(Exception) as context:
            DataURL.from_byte_data("type", "string")

        self.assertTrue('Data must be a bytes type' in str(context.exception))

    def run_assertions(self):
        self.assertEqual(self.url.mime_type, self.mime_type)
        self.assertEqual(self.url.data, self.raw_data)
        self.assertEqual(self.url.encoded_data, self.data)

        self.assertEqual(self.url.is_base64_encoded, self.base64_encoded)
        self.assertEqual(self.expected_url, self.url.url)
