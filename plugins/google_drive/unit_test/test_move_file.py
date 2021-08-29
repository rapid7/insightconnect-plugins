import sys
import os
from unittest import TestCase
from komand_google_drive.actions.move_file import MoveFile
from komand_google_drive.actions.move_file.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestMoveFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MoveFile())

    def test_move_file(self):
        actual = self.action.run(
            {Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E", Input.FILE_ID: "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR"}
        )
        expected = {
            Output.RESULT: {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]}
        }
        self.assertEqual(actual, expected)

    def test_move_file_not_found(self):
        with self.assertRaises(Exception):
            self.action.run({Input.FOLDER_ID: "0BwwA4oUTeiV1TGRPeTVjaWRDY1E", Input.FILE_ID: "File Not Found"})
