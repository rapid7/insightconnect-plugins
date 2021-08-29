import sys
import os
from unittest import TestCase
from komand_google_drive.actions.create_folder import CreateFolder
from komand_google_drive.actions.create_folder.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestCreateFolder(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateFolder())

    def test_create_folder(self):
        actual = self.action.run({Input.FOLDER_NAME: "New Folder"})
        expected = {Output.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"}
        self.assertEqual(actual, expected)

    def test_create_folder_in_specified_folder(self):
        actual = self.action.run(
            {Input.FOLDER_NAME: "New Folder 2", Input.PARENT_FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"}
        )
        expected = {Output.FOLDER_ID: "0aWwC6yCVab22oS9iaa2WajYdR9o"}
        self.assertEqual(actual, expected)

    def test_create_folder_not_found(self):
        with self.assertRaises(Exception):
            self.action.run({Input.FOLDER_NAME: "Folder Not Found", Input.PARENT_FOLDER_ID: "11111"})
