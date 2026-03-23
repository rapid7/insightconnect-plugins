import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from jsonschema.validators import validate
from komand_compression.actions.compress_bytes import CompressBytes
from komand_compression.actions.compress_bytes.schema import Input, Output
from parameterized import parameterized

TEST_INPUT_STRING = "Hello, World! This is a test string for compression."
TEST_INPUT_B64 = base64.b64encode(TEST_INPUT_STRING.encode("utf-8")).decode("utf-8")


class TestCompressBytes(TestCase):
    def setUp(self) -> None:
        self.action = CompressBytes()

    @parameterized.expand(
        [
            ("gzip",),
            ("bzip",),
            ("lz",),
            ("xz",),
            ("zip",),
        ]
    )
    def test_compress_bytes(self, algorithm: str) -> None:
        params = {
            Input.ALGORITHM: algorithm,
            Input.BYTES: TEST_INPUT_B64,
        }
        response = self.action.run(params)
        validate(response, self.action.output.schema)
        compressed = response.get(Output.COMPRESSED)
        self.assertIsNotNone(compressed)
        self.assertIsInstance(compressed, str)
        self.assertGreater(len(compressed), 0)
