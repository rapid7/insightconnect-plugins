import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_dig.connection.connection import Connection
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from komand_dig.actions.reverse import Reverse
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_dig)
class TestReverse(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Reverse())

    @parameterized.expand(
        [
            [
                "reverse",
                Util.read_file_to_dict("inputs/reverse.json.inp"),
                Util.read_file_to_dict("expected/reverse.json.exp"),
            ],
            [
                "reverse_no_resolver",
                Util.read_file_to_dict("inputs/reverse_no_resolver.json.inp"),
                Util.read_file_to_dict("expected/reverse_no_resolver.json.exp"),
            ],
        ]
    )
    def test_reverse(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        print(f"{input_params}")
        print(f"{expected}")
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "reverse_raise_error",
                Util.read_file_to_dict("inputs/reverse_raise_error.json.inp"),
                Util.read_file_to_dict("expected/reverse_raise_error.json.exp"),
            ]
        ]
    )
    def test_error(self, _mock_request: MagicMock, _test_name: str, input_params: dict, exp: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, exp)
