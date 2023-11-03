import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from komand_whois.connection.connection import Connection
from komand_whois.actions.domain import Domain
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import logging


@patch("whois.query", side_effect=Util.mock_whois)
class TestDomain(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Domain())

    @parameterized.expand(
        [
            [
                "domain",
                Util.read_file_to_dict("inputs/domain.json.inp"),
                Util.read_file_to_dict("expected/domain.json.exp")
            ]
        ]
    )
    def test_domain(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "domain_error",
                Util.read_file_to_dict("inputs/domain_error.json.inp"),
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
            ]
        ]
    )
    def test_invalid(self, _mock_request: MagicMock, _test_name: str, input_params: dict, cause: str, assistance: str):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)


