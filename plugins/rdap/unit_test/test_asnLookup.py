import os
import sys
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest.mock import Mock

from icon_rdap.actions.asnLookup import AsnLookup
from parameterized import parameterized

from unit_test.util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestAsnLookup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AsnLookup())

    @parameterized.expand(
        [
            [
                "existing_asn",
                Util.read_file_to_dict("inputs/asn_lookup.json.inp"),
                Util.read_file_to_dict("expected/asn_lookup.json.exp"),
            ]
        ]
    )
    def test_asn_lookup(
        self, mock_request: Mock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "asn_not_found",
                Util.read_file_to_dict("inputs/asn_lookup_not_found.json.inp"),
                "Resource not found.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_asn_lookup_raise_exception(
        self, mock_request: Mock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
