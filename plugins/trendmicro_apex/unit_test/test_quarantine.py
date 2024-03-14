import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.quarantine import Quarantine
from icon_trendmicro_apex.actions.quarantine.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestQuarantine(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(Quarantine())
        self.params = {Input.AGENT: "198.51.100.100", Input.QUARANTINE_STATE: True, Input.WHITELIST: "198.51.100.101"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_quarantine(self, mock_post, mock_token):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected = {
            Output.RESULT_CODE: 1,
            Output.RESULT_CONTENT: [
                {
                    "capabilities": [
                        "cmd_restore_isolated_agent",
                        "cmd_isolate_agent",
                        "cmd_relocate_agent",
                        "cmd_uninstall_agent",
                    ],
                    "entity_id": "test",
                    "folder_path": "Workgroup",
                    "host_name": "TREND-MICRO-TES",
                    "ip_address_list": "198.51.100.100",
                    "isolation_status": "normal",
                    "mac_address_list": "08-00-27-96-86-8E",
                    "managing_server_id": "test",
                    "product": "SLF_PRODUCT_OFFICESCAN_CE",
                }
            ],
            Output.RESULT_DESCRIPTION: "Operation successful",
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
