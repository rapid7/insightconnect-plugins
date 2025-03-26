import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.get_attributes import GetAttributes
from jsonschema import validate
from unittest.mock import patch, Mock
from util import MockSMBSession


class TestGetAttributes(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(GetAttributes())

    @patch("smb.SMBConnection.SMBConnection.getAttributes", side_effect=MockSMBSession.getAttributes)
    def test_get_attributes(self, mock_smb: Mock) -> None:
        input_param = Util.load_json("inputs/get_attributes_input.json.exp")
        expect = Util.load_json("expected/get_attributes_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
