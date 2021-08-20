from unittest import TestCase
from icon_extractit.actions.filepath_extractor import FilepathExtractor
from icon_extractit.actions.filepath_extractor.schema import Input, Output


class TestFilepathExtractor(TestCase):
    def test_extract_filepath_from_string(self):
        action = FilepathExtractor()
        actual = action.run(
            {
                Input.STR: "/tmp/image.jpg and /tmp/script are example file paths",
            }
        )
        expected = {Output.FILEPATHS: ["/tmp/image.jpg", "/tmp/script"]}
        self.assertEqual(actual, expected)

    def test_extract_filepath_from_file(self):
        action = FilepathExtractor()
        actual = action.run(
            {
                Input.FILE: "L3RtcC9pbWFnZS5qcGcgYW5kIC90bXAvc2NyaXB0IGFyZSBleGFtcGxlIGZpbGUgcGF0aHM=",
            }
        )
        expected = {Output.FILEPATHS: ["/tmp/image.jpg", "/tmp/script"]}
        self.assertEqual(actual, expected)
