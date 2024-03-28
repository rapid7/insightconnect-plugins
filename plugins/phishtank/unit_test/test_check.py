import sys
import os
from unittest.mock import patch, MagicMock

from parameterized import parameterized
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_phishtank.connection.connection import Connection
from komand_phishtank.actions.check import Check
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
import json
import logging


@patch("requests.post")
class TestCheck(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(Check())

    @parameterized.expand(
     [
         [
            "check",
            Util.read_file_to_dict("inputs/check.json.inp"),
            Util.read_file_to_dict("expected/check.json.exp"),
         ]
     ]
    )
    def test_check(self, _test_mock: MagicMock, _test_name: str, input_params: str, expected: dict):

        actual = self.action.run(input_params)
        print(f"actual = {actual}")
        print(f"expected = {expected}")
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "check_error",

            ]
        ]
    )
    def test_check_error(self):
        pass
