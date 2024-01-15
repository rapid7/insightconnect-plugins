import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.search_agents.action import SearchAgents
from icon_cylance_protect.actions.search_agents.schema import SearchAgentsInput, SearchAgentsOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestSearchAgents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchAgents())

    @parameterized.expand(
        [
            [
                "valid_search_ip",
                {"agent": "1.1.1.1"},
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
                "valid_search_hostname",
                {"agent": "hostname"},
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
                "valid_search_mac",
                {"agent": "00-60-26-26-D5-19"},
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
    @patch("icon_cylance_protect.actions.search_agents.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_quarantine_valid(
        self,
        _test_name: str,
        input_params: dict,
        expected: dict,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, SearchAgentsInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, SearchAgentsOutput.schema)

    @parameterized.expand(
        [
            [
                "valid_search_mac",
                {"agent": "1.1.1.2"},
                "Agent not found.",
                "Unable to find any agents using identifier provided: 1.1.1.2.",
            ]
        ]
    )
    @patch("icon_cylance_protect.actions.search_agents.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_quarantine_invalid(
        self,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, SearchAgentsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
