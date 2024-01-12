import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.update_agent_threat.action import UpdateAgentThreat
from icon_cylance_protect.actions.update_agent_threat.schema import UpdateAgentThreatInput, UpdateAgentThreatOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateAgentThreat(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateAgentThreat())

    @parameterized.expand(
        [
            [
                "valid_threat_update_hostname_md5",
                {
                    "agent": "hostname",
                    "quarantine_state": True,
                    "threat_identifier": "938c2cc0dcc05f2b68c4287040cfcf71",
                },
                {"success": True},
            ],
            [
                "valid_threat_update_ip_md5",
                {
                    "agent": "1.1.1.1",
                    "quarantine_state": True,
                    "threat_identifier": "938c2cc0dcc05f2b68c4287040cfcf71",
                },
                {"success": True},
            ],
            [
                "valid_threat_update_ip_sha",
                {
                    "agent": "1.1.1.1",
                    "quarantine_state": True,
                    "threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d80",
                },
                {"success": True},
            ],
            [
                "valid_threat_update_hostname_sha",
                {
                    "agent": "hostname",
                    "quarantine_state": False,
                    "threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d80",
                },
                {"success": True},
            ],
        ]
    )
    def test_integration_search_threats_valid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, UpdateAgentThreatInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, UpdateAgentThreatOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_threat_update_invalid_sha",
                {
                    "agent": "not_valid_hostname",
                    "quarantine_state": False,
                    "threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d8f",
                },
                "Threat not found.",
                "Unable to find any threats using identifier provided: ['5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d8f'].",
            ],
            [
                "invalid_threat_update_invalid_hostname",
                {
                    "agent": "invalid_hostname",
                    "quarantine_state": False,
                    "threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d80",
                },
                "Not found.",
                "The request was made for a resource that doesn't exist.",
            ],
        ]
    )
    def test_integration_search_threats_invalid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
    ):
        validate(input_params, UpdateAgentThreatInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
