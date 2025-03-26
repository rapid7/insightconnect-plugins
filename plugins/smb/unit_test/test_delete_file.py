import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.delete_file import DeleteFile
from jsonschema import validate
from unittest.mock import MagicMock, patch, Mock

CREATE_CLIENT_MOCK = MagicMock()


class TestDeleteFile(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(DeleteFile())

    @patch("smb.SMBConnection.SMBConnection.deleteFiles", return_value=CREATE_CLIENT_MOCK)
    def test_delete_file(self, delete_file):
        input_param = Util.load_json("inputs/delete_file_input.json.exp")
        expect = Util.load_json("expected/delete_file_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
