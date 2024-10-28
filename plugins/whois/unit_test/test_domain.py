import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_whois.actions.domain import Domain
from parameterized import parameterized

from util import Util


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
                Util.read_file_to_dict("expected/domain.json.exp"),
            ]
        ]
    )
    def test_domain(
        self, _mock_request: MagicMock, _test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ):
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "domain_error",
                Util.read_file_to_dict("inputs/domain_error.json.inp"),
                "Invalid domain as input.",
                "Ensure the domain is not prefixed with a protocol.",
            ]
        ]
    )
    def test_invalid(
        self, _mock_request: MagicMock, _test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
