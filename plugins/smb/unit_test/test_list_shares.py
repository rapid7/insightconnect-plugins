import sys
import os
from util import Util, MockSMBSession

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.list_shares import ListShares
from jsonschema import validate
from unittest.mock import patch, Mock


class TestListShares(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(ListShares())

    @patch("smb.SMBConnection.SMBConnection.listShares", side_effect=MockSMBSession.listShares)
    def test_list_shares(self, mock_smb: Mock) -> None:
        input_param = Util.load_json("inputs/list_shares_input.json.exp")
        expect = Util.load_json("expected/list_shares_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
