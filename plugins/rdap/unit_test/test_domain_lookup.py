import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_rdap.actions.domainLookup import DomainLookup


@patch("requests.request", side_effect=Util.mock_request)
class TestDomainLookup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = DomainLookup()

    @parameterized.expand(
        [
            [
                "invalid_domain",
                Util.read_file_to_dict("inputs/domain_lookup_invalid_domain.json.inp"),
                "Resource not found.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, "
                "please contact support.",
            ],
            [
                "not_found_domain",
                Util.read_file_to_dict("inputs/domain_lookup_not_found_domain.json.inp"),
                "Resource not found.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, "
                "please contact support.",
            ],
        ]
    )
    def test_domain_lockup_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "domain_found",
                Util.read_file_to_dict("inputs/domain_lookup_found_domain.json.inp"),
                Util.read_file_to_dict("expected/domain_lookup_found_domain.json.exp"),
            ]
        ]
    )
    def test_domain_lookup(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
