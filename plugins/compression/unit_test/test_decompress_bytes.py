import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from jsonschema.validators import validate
from komand_compression.actions.compress_bytes import CompressBytes
from komand_compression.actions.compress_bytes.schema import Input as CompressInput
from komand_compression.actions.compress_bytes.schema import Output as CompressOutput
from komand_compression.actions.decompress_bytes import DecompressBytes
from komand_compression.actions.decompress_bytes.schema import Input, Output
from parameterized import parameterized

TEST_INPUT_STRING = "Hello, World! This is a test string for compression."
TEST_INPUT_B64 = base64.b64encode(TEST_INPUT_STRING.encode("utf-8")).decode("utf-8")


class TestDecompressBytes(TestCase):
    def setUp(self) -> None:
        self.compress_action = CompressBytes()
        self.decompress_action = DecompressBytes()

    @parameterized.expand(
        [
            ("gzip",),
            ("bzip",),
            ("lz",),
            ("xz",),
            ("zip",),
        ]
    )
    def test_decompress_bytes(self, algorithm: str) -> None:
        # First compress the data
        compress_params = {
            CompressInput.ALGORITHM: algorithm,
            CompressInput.BYTES: TEST_INPUT_B64,
        }
        compressed_response = self.compress_action.run(compress_params)
        compressed_b64 = compressed_response.get(CompressOutput.COMPRESSED)

        # Then decompress it
        decompress_params = {
            Input.BYTES: compressed_b64,
        }
        response = self.decompress_action.run(decompress_params)
        validate(response, self.decompress_action.output.schema)
        decompressed = response.get(Output.DECOMPRESSED)
        self.assertIsNotNone(decompressed)
        self.assertIsInstance(decompressed, str)
        self.assertEqual(decompressed, TEST_INPUT_B64)
