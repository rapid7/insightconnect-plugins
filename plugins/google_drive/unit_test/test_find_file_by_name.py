import sys
import os
from unittest import TestCase
from komand_google_drive.actions.find_file_by_name import FindFileByName
from komand_google_drive.actions.find_file_by_name.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestFindFileByName(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(FindFileByName())

    @parameterized.expand(
        [
            ["find_file", "File to find", "=", "12345", [{"file_name": "File to find", "file_id": "98765"}]],
            ["find_file2", "File to find", "!=", "12345", [{"file_name": "Another file", "file_id": "87654"}]],
            ["find_file3", "File", "contains", "12345", [{"file_name": "File to find", "file_id": "98765"}]],
            ["without_parent_id", "File to find", "=", None, [{"file_name": "File to find", "file_id": "98765"}]],
            ["file_not_found", "Not Found", "=", None, []],
        ]
    )
    def test_find_file_by_name(self, name, filename, operator, parent_id, expected):
        actual = self.action.run(
            {Input.FILENAME: filename, Input.FILENAME_OPERATOR: operator, Input.PARENT_ID: parent_id}
        )
        expected = {Output.FILES_FOUND: expected}
        self.assertEqual(actual, expected)
