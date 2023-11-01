import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_dig.connection.connection import Connection
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from komand_dig.actions.forward import Forward
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_dig)
class TestForward(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Forward())

    @parameterized.expand(
        [
            [
                "forward",
                Util.read_file_to_dict("inputs/forward.json.inp"),
                Util.read_file_to_dict("expected/forward.json.exp"),
            ],
            [
                "forward_no_resolver",
                Util.read_file_to_dict("inputs/forward_no_resolver.json.inp"),
                Util.read_file_to_dict("expected/forward_no_resolver.json.exp"),
            ],
        ]
    )
    def test_forward(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "forward_raise_error",
                Util.read_file_to_dict("inputs/forward_raise_error.json.inp"),
                Util.read_file_to_dict("expected/forward_raise_error.json.exp"),
            ]
        ]
    )
    def test_error(self, _mock_request: MagicMock, _test_name: str, input_params: dict, exp: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, exp)
