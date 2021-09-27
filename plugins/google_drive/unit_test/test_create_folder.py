import sys
import os
from unittest import TestCase
from komand_google_drive.actions.create_folder import CreateFolder
from komand_google_drive.actions.create_folder.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestCreateFolder(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateFolder())

    @parameterized.expand(
        [
            ["create_folder", "New Folder", None, "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"],
            [
                "create_in_another_folder",
                "New Folder 2",
                "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
                "0aWwC6yCVab22oS9iaa2WajYdR9o",
            ],
        ]
    )
    def test_create_folder(self, name, folder_name, parent_folder_id, expected):
        actual = self.action.run({Input.FOLDER_NAME: folder_name, Input.PARENT_FOLDER_ID: parent_folder_id})
        expected = {Output.FOLDER_ID: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_folder_id",
                "Folder Not Found",
                "11111",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                '<HttpError 404 when requesting http://example.com returned "Folder not found".'
                ' Details: "Folder not found">',
            ]
        ]
    )
    def test_create_folder_bad(self, name, folder_name, parent_folder_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.FOLDER_NAME: folder_name, Input.PARENT_FOLDER_ID: parent_folder_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
