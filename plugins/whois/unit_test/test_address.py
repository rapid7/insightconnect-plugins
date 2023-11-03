import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from komand_whois.connection.connection import Connection
from komand_whois.actions.address import Address
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import logging


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_whois)
class TestAddress(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Address())

    @parameterized.expand(
        [
            [
                "address",
                Util.read_file_to_dict("inputs/address.json.inp"),
                Util.read_file_to_dict("expected/address.json.exp"),
            ]
        ]
    )
    def test_address(self, _test_mock: MagicMock, _test_name: str, input_params: str, expected: str):
        actual = self.action.run(input_params)
        print(f"{actual =}")
        print(f"{expected =}")
        self.assertEqual(actual, expected)


