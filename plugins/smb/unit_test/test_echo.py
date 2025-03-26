import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.echo import Echo
from jsonschema import validate
from unittest.mock import MagicMock, patch

CREATE_CLIENT_MOCK = MagicMock()


class TestEcho(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect", return_value=CREATE_CLIENT_MOCK)
    def setUp(self, mocked_smb: MagicMock) -> None:
        self.action = Util.default_connector(Echo())

    @patch("smb.SMBConnection.SMBConnection.echo", return_value=b"Hello world")
    def test_echo(self, mock_echo):
        input_param = Util.load_json("inputs/echo_input.json.exp")
        expect = Util.load_json("expected/echo_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
