import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.domain_tags.action import DomainTags
from komand_cisco_umbrella_investigate.actions.domain_tags.schema import Input, Output
from parameterized import parameterized

from unit_test.util import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mock_request_429,
    mock_request_500,
    mocked_request,
)

STUB_PARAMS = {Input.DOMAIN: "example.com"}
STUB_RESPONSE = Util.read_file_to_dict("expected/test_domain_tags.json.exp")


class TestDomainTags(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(DomainTags())

    @parameterized.expand(
        [
            ("example.com", STUB_RESPONSE),
            ("example", []),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_domain_tags_ok(self, domain: str, expected_response: Dict[str, Any], mock_get: Mock) -> None:
        response = self.action.run({Input.DOMAIN: domain})
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_domain_tags_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(STUB_PARAMS)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
