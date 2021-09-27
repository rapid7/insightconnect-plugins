import sys
import os
from unittest import TestCase
from komand_google_drive.actions.get_file_contents import GetFileContents
from komand_google_drive.actions.get_file_contents.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized


sys.path.append(os.path.abspath("../"))


class TestGetFileContents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFileContents())

    @parameterized.expand([["get_file_contents", "get_content", "text/plain", "77u/VGVzdA=="]])
    def test_get_file_contents(self, name, file_id, mime_type, expected):
        actual = self.action.run({Input.FILE_ID: file_id, Input.MIME_TYPE: mime_type})
        expected = {Output.FILE: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                "not_found",
                "text/plain",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "File not found".'
                ' Details: "File not found">',
            ]
        ]
    )
    def test_get_file_contents_bad(self, name, file_id, mime_type, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FILE_ID: file_id, Input.MIME_TYPE: mime_type})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
