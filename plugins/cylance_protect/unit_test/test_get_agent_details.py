import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.get_agent_details.action import GetAgentDetails
from icon_cylance_protect.actions.get_agent_details.schema import GetAgentDetailsInput, GetAgentDetailsOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestGetAgentDetails(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    @parameterized.expand(
        [
            [
                "valid_get_agent_details_ip",
                {"agent": "1.1.1.1"},
                {
                    "agent": {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "ip_addresses": ["1.1.1.1"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                },
            ],
            [
                "valid_get_agent_details_hostname",
                {"agent": "hostname"},
                {
                    "agent": {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f6",
                        "ip_addresses": ["1.1.1.2"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                },
            ],
            [
                "valid_get_agent_details_mac",
                {"agent": "00-60-26-26-D5-19"},
                {
                    "agent": {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "ip_addresses": ["1.1.1.1"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                },
            ],
        ]
    )
    @patch(
        "icon_cylance_protect.actions.get_agent_details.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip
    )
    def test_integration_get_agent_details_valid(
        self,
        _test_name: str,
        input_params: dict,
        expected: dict,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, GetAgentDetailsInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, GetAgentDetailsOutput.schema)
