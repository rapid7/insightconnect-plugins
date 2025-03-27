import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.list_share_files import ListShareFiles
from jsonschema import validate
from unittest.mock import patch, Mock
from util import MockSMBSession


class TestListShareFiles(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(ListShareFiles())

    @patch("smb.SMBConnection.SMBConnection.listPath", side_effect=MockSMBSession.listPath)
    def test_list_share_files(self, mock_smb: Mock) -> None:
        input_param = Util.load_json("inputs/list_share_files_input.json.exp")
        expect = Util.load_json("expected/list_share_files_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
