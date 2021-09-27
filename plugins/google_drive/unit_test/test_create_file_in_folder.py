import sys
import os
from unittest import TestCase
from komand_google_drive.actions.create_file_in_folder import CreateFileInFolder
from komand_google_drive.actions.create_file_in_folder.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestCreateFileInFolder(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateFileInFolder())

    @parameterized.expand(
        [
            [
                "csv_file",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                {
                    "filename": "test.csv",
                    "content": "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFsdWU1LHZhbHVlNg0K",
                },
                "1jizwcfNK7JqHtn9kszitKSCWVOborMV8",
            ],
            [
                "txt_file",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                {"filename": "test.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
            ],
            [
                "without_file_extension",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                {"filename": "test", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ",
            ],
            [
                "without_file_name",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                {"filename": "", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ",
            ],
        ]
    )
    def test_create_in_folder(self, name, folder_id, file, expected):
        actual = self.action.run({Input.FOLDER_ID: folder_id, Input.FILE: file})
        expected = {Output.FILE_ID: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_folder_id",
                {"filename": "Folder Not Found", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "11111",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "Folder not found".'
                ' Details: "Folder not found">',
            ]
        ]
    )
    def test_create_file_in_folder_bad(self, name, file, folder_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FILE: file, Input.FOLDER_ID: folder_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
