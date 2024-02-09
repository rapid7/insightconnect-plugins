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
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "ip": "198.51.100.100",
                "isEnable": True,
                "isImportant": False,
                "isOnline": False,
                "isolateStatus": 1,
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "userName": "TREND-MICRO-TES\\vagrant",
            },
            Output.AGENTQUERYSTATUS: {"hasFullAgents": True, "hasFullRbac": True},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
