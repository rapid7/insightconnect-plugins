import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from jsonschema.validators import validate
from komand_compression.actions.create_archive import CreateArchive
from komand_compression.actions.create_archive.schema import Input as CreateInput
from komand_compression.actions.create_archive.schema import Output as CreateOutput
from komand_compression.actions.extract_archive import ExtractArchive
from komand_compression.actions.extract_archive.schema import Input, Output
from parameterized import parameterized

TEST_FILES = [
    {"filename": "test1.txt", "content": "Hello from file one."},
    {"filename": "test2.txt", "content": "Hello from file two."},
]


class TestExtractArchive(TestCase):
    def setUp(self) -> None:
        self.create_action = CreateArchive()
        self.extract_action = ExtractArchive()

    @parameterized.expand(
        [
            ("zip", "test_archive.zip"),
            ("tarball", "test_archive.tar.gz"),
        ]
    )
    def test_extract_archive(self, algorithm: str, filename: str) -> None:
        # First create an archive
        create_params = {
            CreateInput.ALGORITHM: algorithm,
            CreateInput.FILENAME: filename,
            CreateInput.FILES: TEST_FILES,
        }
        create_response = self.create_action.run(create_params)
        archive = create_response.get(CreateOutput.ARCHIVE)

        # Then extract it
        extract_params = {
            Input.ARCHIVE: archive,
        }
        response = self.extract_action.run(extract_params)
        validate(response, self.extract_action.output.schema)
        files = response.get(Output.FILES)
        self.assertIsNotNone(files)
        self.assertIsInstance(files, list)
        self.assertGreater(len(files), 0)
        for file_entry in files:
            self.assertIn("filename", file_entry)
            self.assertIn("content", file_entry)
            self.assertGreater(len(file_entry["filename"]), 0)
            self.assertGreater(len(file_entry["content"]), 0)
