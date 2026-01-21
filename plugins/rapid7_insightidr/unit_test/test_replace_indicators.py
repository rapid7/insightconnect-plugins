import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.replace_indicators import ReplaceIndicators
from komand_rapid7_insightidr.actions.replace_indicators.schema import (
    Input,
    ReplaceIndicatorsInput,
    ReplaceIndicatorsOutput,
)
from parameterized import parameterized

from mock_utils import mock_post_request
from util import Util


@patch("requests.Session.send", side_effect=mock_post_request)
class TestReplaceIndicators(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ReplaceIndicators())

    @parameterized.expand(
        [
            ["dcdba462-fcf5-4021-8707-98b14232239b", ["rapid7.com"], [], [], []],
            ["dcdba462-fcf5-4021-8707-98b14232239b", [], ["a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"], [], []],
            ["dcdba462-fcf5-4021-8707-98b14232239b", [], [], ["192.0.2.0/24"], []],
            ["dcdba462-fcf5-4021-8707-98b14232239b", [], [], [], ["https://example.com"]],
        ]
    )
    def test_replace_indicators(self, mock_request, key, domain_names, hashes, ips, urls) -> None:
        test_input = {
            Input.KEY: key,
            Input.DOMAIN_NAMES: domain_names,
            Input.HASHES: hashes,
            Input.IPS: ips,
            Input.URLS: urls,
        }
        validate(test_input, ReplaceIndicatorsInput.schema)
        actual = self.action.run(test_input)
        expected = {
            "threat": {
                "name": "Threat Command Alert",
                "note": "This threat will be automatically managed by an InsightConnect workflow",
                "published": False,
                "indicator_count": 1,
            },
            "rejected_indicators": [],
        }
        self.assertEqual(actual, expected)
        validate(actual, ReplaceIndicatorsOutput.schema)

    @parameterized.expand(
        [
            [
                "dcdba462",
                "",
                "",
                "",
                "",
                "The response from InsightIDR was not in the correct format.",
                "Contact support for help. See log for more details",
            ],
        ]
    )
    def test_replace_indicators_invalid(
        self, mock_request, key, domain_names, hashes, ips, urls, cause, assistance
    ) -> None:
        test_input = {
            Input.KEY: key,
            Input.DOMAIN_NAMES: domain_names,
            Input.HASHES: hashes,
            Input.IPS: ips,
            Input.URLS: urls,
        }
        with self.assertRaises(PluginException) as error:
            actual = self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
