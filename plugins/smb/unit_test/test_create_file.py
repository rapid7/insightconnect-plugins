import sys
import os
from util import Util


sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_smb.actions.create_file import CreateFile
from jsonschema import validate
from unittest.mock import MagicMock, patch, Mock

CREATE_CLIENT_MOCK = MagicMock()


class TestCreateFile(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(CreateFile())

    @patch("smb.SMBConnection.SMBConnection.storeFile", return_value=CREATE_CLIENT_MOCK)
    def test_create_file(self, mock_store_file):
        input_param = Util.load_json("inputs/create_file_input.json.exp")
        expect = Util.load_json("expected/create_file_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
