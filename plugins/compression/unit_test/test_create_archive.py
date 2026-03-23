import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from jsonschema.validators import validate
from komand_compression.actions.create_archive import CreateArchive
from komand_compression.actions.create_archive.schema import Input, Output
from parameterized import parameterized

TEST_FILES = [
    {"filename": "test1.txt", "content": "Hello from file one."},
    {"filename": "test2.txt", "content": "Hello from file two."},
]


class TestCreateArchive(TestCase):
    def setUp(self) -> None:
        self.action = CreateArchive()

    @parameterized.expand(
        [
            ("zip", "test_archive.zip"),
            ("tarball", "test_archive.tar.gz"),
        ]
    )
    def test_create_archive(self, algorithm: str, filename: str) -> None:
        params = {
            Input.ALGORITHM: algorithm,
            Input.FILENAME: filename,
            Input.FILES: TEST_FILES,
        }
        response = self.action.run(params)
        validate(response, self.action.output.schema)
        archive = response.get(Output.ARCHIVE)
        self.assertIsNotNone(archive)
        self.assertIn("filename", archive)
        self.assertIn("content", archive)
        self.assertEqual(archive["filename"], filename)
        self.assertGreater(len(archive["content"]), 0)
