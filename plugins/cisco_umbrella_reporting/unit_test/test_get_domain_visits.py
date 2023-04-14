import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase, mock
from unittest.mock import Mock

from icon_cisco_umbrella_reporting.actions.get_domain_visits import GetDomainVisits
from icon_cisco_umbrella_reporting.actions.get_domain_visits.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from unit_test.mock import (
    Util,
    mock_request_200,
    mock_request_204,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mock_request_invalid_json,
    mocked_request,
)


class TestGetDomainVisits(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(GetDomainVisits())

    @parameterized.expand(
        [
            (
                mock_request_200,
                {
                    Output.DOMAIN_VISITS: [
                        {
                            "externalIp": "255.255.255.255",
                            "internalIp": "255.255.255.255",
                            "categories": ["Malware"],
                            "verdict": "allowed",
                            "domain": "example.com",
                            "datetime": "2019-01-24T06:31:46",
                            "timestamp": 1548311506,
                            "identities": [
                                {
                                    "id": 1,
                                    "label": "ExampleName",
                                    "deleted": True,
                                }
                            ],
                            "threats": [{"label": "Wannacry", "type": "Ransomware"}],
                            "allApplications": ["ExampleApp"],
                            "allowedApplications": ["ExampleApp"],
                            "queryType": "MX",
                        }
                    ]
                },
            ),
            (mock_request_204, {Output.DOMAIN_VISITS: []}),
        ]
    )
    def test_get_domain_visits_ok(self, mock_request: Mock, expected_response: Dict[str, Any]) -> None:
        mocked_request(mock_request)
        response = self.action.run({Input.ADDRESS: "example.com", Input.FROM: "-1days", Input.LIMIT: 1})
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_domain_visits_exceptions(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
