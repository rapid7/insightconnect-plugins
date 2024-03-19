import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.get_agent_status import GetAgentStatus
from icon_trendmicro_apex.actions.get_agent_status.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestGetAgentStatus(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetAgentStatus())
        self.params = {Input.AGENT_GUID: ""}

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_agent_status(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.AGENTENTITY: {
                "agentGuid": "123456789-1234-1234-1234-123456789",
                "ip": "198.51.100.100",
                "isEnable": True,
                "isImportant": False,
                "isOnline": False,
                "isolateStatus": 1,
                "machineGuid": "123456789-1234-1234-1234-123456789",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "123456789-1234-1234-1234-123456789",
                "userGuid": "123456789-1234-1234-1234-123456789",
                "userName": "TREND-MICRO-TES\\vagrant",
            },
            Output.AGENTQUERYSTATUS: {"hasFullAgents": True, "hasFullRbac": True},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
