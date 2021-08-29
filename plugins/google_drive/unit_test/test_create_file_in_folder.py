import sys
import os
from unittest import TestCase
from komand_google_drive.actions.create_file_in_folder import CreateFileInFolder
from komand_google_drive.actions.create_file_in_folder.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestCreateFileInFolder(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateFileInFolder())

    def test_create_csv_file_in_folder(self):
        actual = self.action.run(
            {
                Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                Input.FILE: {
                    "filename": "test.csv",
                    "content": "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFsdWU1LHZhbHVlNg0K",
                },
            }
        )
        expected = {Output.FILE_ID: "1jizwcfNK7JqHtn9kszitKSCWVOborMV8"}
        self.assertEqual(actual, expected)

    def test_create_txt_file_in_folder(self):
        actual = self.action.run(
            {
                Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                Input.FILE: {"filename": "test.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
            }
        )
        expected = {Output.FILE_ID: "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR"}
        self.assertEqual(actual, expected)

    def test_create_file_in_folder_without_filename_extension(self):
        actual = self.action.run(
            {
                Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                Input.FILE: {"filename": "test", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
            }
        )
        expected = {Output.FILE_ID: "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        self.assertEqual(actual, expected)

    def test_create_file_in_folder_without_filename(self):
        actual = self.action.run(
            {
                Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                Input.FILE: {"filename": "", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
            }
        )
        expected = {Output.FILE_ID: "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        self.assertEqual(actual, expected)

    def test_create_file_in_folder_not_found(self):
        with self.assertRaises(Exception):
            self.action.run(
                {
                    Input.FOLDER_ID: "11111",
                    Input.FILE: {"filename": "Folder Not Found", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="},
                }
            )
