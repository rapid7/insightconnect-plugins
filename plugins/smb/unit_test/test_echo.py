import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_smb.actions.echo import Echo
from jsonschema import validate
from unittest.mock import patch


class TestEcho(TestCase):
    @patch("komand_smb.connection.connection.Connection.connect", return_value=None)
    def setUp(self, mock_connect) -> None:
        self.action = Util.default_connector(Echo())

    def test_echo(self):
        input_param = {"message": "Hello world"}
        validate(input_param, self.action.input.schema)

        expect = {"response": "Hello world"}
        actual = self.action.run(input_param)

        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
