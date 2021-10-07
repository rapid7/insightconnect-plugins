import sys
import os
from unittest import TestCase
from komand_google_drive.actions.upload_file import UploadFile
from komand_google_drive.actions.upload_file.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestUploadFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UploadFile())

    @parameterized.expand(
        [
            [
                "upload_file",
                {"filename": "upload.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "Docs",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                "upload_file",
                "https://docs.google.com/document/d/upload_file",
            ],
            [
                "upload_file2",
                {"filename": "upload.ppt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "Slides",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                "upload_file2",
                "https://docs.google.com/presentation/d/upload_file2",
            ],
            [
                "upload_file3",
                {"filename": "upload.csv", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "Sheets",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                "upload_file3",
                "https://docs.google.com/spreadsheets/d/upload_file3",
            ],
            [
                "without_file_id",
                {"filename": "upload.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "Docs",
                None,
                "upload_file",
                "https://docs.google.com/document/d/upload_file",
            ],
        ]
    )
    def test_upload_file(self, name, file, file_type, folder_id, expected_id, expected_link):
        actual = self.action.run(
            {
                Input.FILE: file,
                Input.GOOGLE_FILE_TYPE: file_type,
                Input.FOLDER_ID: folder_id,
            }
        )
        expected = {Output.FILE_ID: expected_id, Output.FILE_LINK: expected_link}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_folder_id",
                {"filename": "Folder Not Found", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                "Docs",
                "11111",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "Folder not found".'
                ' Details: "Folder not found">',
            ]
        ]
    )
    def test_upload_file_bad(self, name, file, file_type, folder_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FILE: file, Input.GOOGLE_FILE_TYPE: file_type, Input.FOLDER_ID: folder_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
