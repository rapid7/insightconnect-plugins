import sys
import os
from unittest import TestCase
from komand_google_drive.actions.move_file import MoveFile
from komand_google_drive.actions.move_file.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized


sys.path.append(os.path.abspath("../"))


class TestMoveFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MoveFile())

    @parameterized.expand(
        [
            [
                "move_file",
                "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]},
            ]
        ]
    )
    def test_move_file(self, name, file_id, folder_id, expected):
        actual = self.action.run({Input.FOLDER_ID: folder_id, Input.FILE_ID: file_id})
        expected = {Output.RESULT: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                "File Not Found",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "File not found".'
                ' Details: "File not found">',
            ]
        ]
    )
    def test_move_file_bad(self, name, file_id, folder_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FOLDER_ID: folder_id, Input.FILE_ID: file_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
