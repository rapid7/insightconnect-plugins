import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.search_threat_agents.action import SearchThreatAgents
from icon_cylance_protect.actions.search_threat_agents.schema import SearchThreatAgentsInput, SearchThreatAgentsOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestSearchThreatAgents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchThreatAgents())

    @parameterized.expand(
        [
            [
                "valid_threat_search_md5",
                {"threat_identifier": "938c2cc0dcc05f2b68c4287040cfcf71"},
                {
                    "agents": [
                        {
                            "agent_version": "2.0.1540",
                            "date_found": "2020-05-29T10:12:45",
                            "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                            "file_status": "Default",
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "ip_addresses": ["1.1.1.1"],
                            "mac_addresses": ["00-60-26-26-D5-19"],
                            "name": "hostname",
                            "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "state": "OffLine",
                        }
                    ]
                },
            ],
            [
                "valid_threat_search_sha",
                {"threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d80"},
                {
                    "agents": [
                        {
                            "agent_version": "2.0.1540",
                            "date_found": "2020-05-29T10:12:45",
                            "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                            "file_status": "Default",
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "ip_addresses": ["1.1.1.1"],
                            "mac_addresses": ["00-60-26-26-D5-19"],
                            "name": "hostname",
                            "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "state": "OffLine",
                        }
                    ]
                },
            ],
            [
                "valid_threat_search_name",
                {"threat_identifier": "honeyhashx86.exe"},
                {
                    "agents": [
                        {
                            "agent_version": "2.0.1540",
                            "date_found": "2020-05-29T10:12:45",
                            "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                            "file_status": "Default",
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "ip_addresses": ["1.1.1.1"],
                            "mac_addresses": ["00-60-26-26-D5-19"],
                            "name": "hostname",
                            "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "state": "OffLine",
                        }
                    ]
                },
            ],
        ]
    )
    def test_integration_search_threat_agents_valid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, SearchThreatAgentsInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, SearchThreatAgentsOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_threat_search_md5",
                {"threat_identifier": "938c2cc0dcc05f2b68c4287040cfcf70"},
                "Threat not found.",
                "Unable to find any threats using identifier provided: 938c2cc0dcc05f2b68c4287040cfcf70.",
            ],
            [
                "invalid_threat_search_sha",
                {"threat_identifier": "5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d81"},
                "Threat not found.",
                "Unable to find any threats using identifier provided: 5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d81.",
            ],
            [
                "invalid_threat_search_name",
                {"threat_identifier": "invalid_name"},
                "Threat not found.",
                "Unable to find any threats using identifier provided: invalid_name.",
            ],
        ]
    )
    @patch("icon_cylance_protect.actions.search_agents.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_search_threat_agent_invalid(
        self,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, SearchThreatAgentsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
