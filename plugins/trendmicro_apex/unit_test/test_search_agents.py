import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.search_agents import SearchAgents
from icon_trendmicro_apex.actions.search_agents.schema import Input, Output
from jsonschema import validate
from unit_test.mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestSearchAgents(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SearchAgents())
        self.params = {Input.AGENT_IDS: "08-00-27-96-86-8E"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_search_agents(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected = {
            Output.SEARCH_AGENT_RESPONSE: [
                {
                    "capabilities": [
                        "cmd_restore_isolated_agent",
                        "cmd_isolate_agent",
                        "cmd_relocate_agent",
                        "cmd_uninstall_agent",
                    ],
                    "entity_id": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                    "folder_path": "Workgroup",
                    "host_name": "TREND-MICRO-TES",
                    "ip_address_list": "198.51.100.100",
                    "isolation_status": "normal",
                    "mac_address_list": "08-00-27-96-86-8E",
                    "managing_server_id": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                    "product": "SLF_PRODUCT_OFFICESCAN_CE",
                }
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
