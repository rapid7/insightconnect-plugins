import sys
import os
from unittest import TestCase
from komand_google_drive.actions.overwrite_file import OverwriteFile
from komand_google_drive.actions.overwrite_file.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestOverwriteFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(OverwriteFile())

    @parameterized.expand(
        [
            ["overwrite_file", "overwrite_1", "New Filename", "Docs", "77u/VGVzdA==", "overwrite_1"],
            ["overwrite_file2", "overwrite_2", "New Filename", "Sheets", "77u/VGVzdA==", "overwrite_2"],
            ["overwrite_file3", "overwrite_3", "New Filename", "Slides", "77u/VGVzdA==", "overwrite_3"],
            ["without_new_filename", "without_new_filename", None, "Slides", "77u/VGVzdA==", "without_new_filename"],
        ]
    )
    def test_overwrite_file(self, name, file_id, new_file_name, new_mime_type, content, expected):
        actual = self.action.run(
            {
                Input.FILE_ID: file_id,
                Input.NEW_FILE_NAME: new_file_name,
                Input.NEW_MIME_TYPE: new_mime_type,
                Input.CONTENT: content,
            }
        )
        expected = {Output.FILE_ID: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                "not_found",
                "Docs",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "File not found".'
                ' Details: "File not found">',
            ]
        ]
    )
    def test_get_file_contents_bad(self, file_id, new_mime_type, content, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FILE_ID: file_id, Input.NEW_MIME_TYPE: new_mime_type, Input.CONTENT: content})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
