import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.get_agent_details import GetAgentDetails
from komand_sentinelone.actions.get_agent_details.schema import Input
from unit_test.util import Util
from unittest import TestCase

expected = {
    "agent": {
        "accountName": "account",
        "agentVersion": "1.1.1",
        "allowRemoteShell": False,
        "computerName": "computer",
        "coreCount": "1",
        "cpuCount": "1",
        "cpuId": "11",
        "createdAt": "2021-11-11",
        "domain": "domain",
        "externalId": "10.10.10.10",
        "externalIp": "10.10.10.10",
        "firewallEnabled": True,
        "groupIp": "1.0.0.0",
        "groupUpdatedAt": "2021-11-11",
        "id": "ffff-ffff",
        "inRemoteShellSession": True,
        "infected": False,
        "isActive": True,
        "isDecommissioned": False,
        "isPendingUninstall": True,
        "isUninstalled": False,
        "isUpToDate": "2021-11-11",
        "lastActiveDate": "2021-11-11",
        "lastIpToMgmt": "1.1.1.1",
        "lastLoggedInUserName": "username",
        "licenseKey": "ffff-ffff-ffffffff-ffff",
        "locationEnabled": True,
        "networkQuarantineEnabled": True,
        "networkStatus": "active",
        "operationalState": "active",
        "operationalStateExpiration": "active",
        "osArch": "x64",
        "osName": "windows 7",
        "osType": "win",
        "osUsername": "username",
        "remoteProfilingState": "active",
        "remoteProfilingStateExpiration": "active",
        "scanFinishedAt": "2021-11-11",
        "threatRebootRequired": False,
        "totalMemory": 8000,
        "updatedAt": "2021-11-11",
        "uuid": "ffff-ffff-ffffffff-ffff",
    }
}


class TestGetAgentDetails(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_response_when_any_status(self, mock_request):
        actual = self.action.run(
            {Input.AGENT: "hostname123", Input.CASE_SENSITIVE: True, Input.OPERATIONAL_STATE: "Any"}
        )
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_response_when_na_status(self, mock_request):
        expected["agent"]["operationalState"] = "na"
        actual = self.action.run(
            {Input.AGENT: "hostname_na", Input.CASE_SENSITIVE: True, Input.OPERATIONAL_STATE: "na"}
        )
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_response_when_fully_disabled_status(self, mock_request):
        expected["agent"]["operationalState"] = "fully_disabled"
        actual = self.action.run(
            {
                Input.AGENT: "hostname_fully_disabled",
                Input.CASE_SENSITIVE: True,
                Input.OPERATIONAL_STATE: "fully_disabled",
            }
        )
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_response_when_partially_disabled_status(self, mock_request):
        expected["agent"]["operationalState"] = "partially_disabled"
        actual = self.action.run(
            {
                Input.AGENT: "hostname_partially_disabled",
                Input.CASE_SENSITIVE: True,
                Input.OPERATIONAL_STATE: "partially_disabled",
            }
        )
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_response_when_disabled_error_status(self, mock_request):
        expected["agent"]["operationalState"] = "disabled_error"
        actual = self.action.run(
            {
                Input.AGENT: "hostname_disabled_error",
                Input.CASE_SENSITIVE: True,
                Input.OPERATIONAL_STATE: "disabled_error",
            }
        )
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_return_empty_when_different_status(self, mock_request):
        for test in [
            "na",
            "fully_disabled",
            "partially_disabled",
            "disabled_error",
        ]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run(
                    {Input.AGENT: "hostname123", Input.CASE_SENSITIVE: True, Input.OPERATIONAL_STATE: test}
                )
                self.assertEqual({"agent": {}}, actual)
