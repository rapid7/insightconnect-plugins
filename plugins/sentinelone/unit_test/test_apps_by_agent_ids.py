import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.apps_by_agent_ids import AppsByAgentIds
from komand_sentinelone.actions.apps_by_agent_ids.schema import Input
from unit_test.util import Util
from unittest import TestCase

expected = {
    "data": [
        {
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
        },
        {
            "accountName": "account",
            "agentVersion": "1.1.2",
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
            "groupIp": "1.0.0.1",
            "groupUpdatedAt": "2021-11-11",
            "id": "ffff-fffe",
            "inRemoteShellSession": True,
            "infected": False,
            "isActive": True,
            "isDecommissioned": False,
            "isPendingUninstall": True,
            "isUninstalled": False,
            "isUpToDate": "2021-11-11",
            "lastActiveDate": "2021-11-11",
            "lastIpToMgmt": "1.1.1.2",
            "lastLoggedInUserName": "username",
            "licenseKey": "ffff-ffff-ffffffff-fffe",
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
            "uuid": "ffff-ffff-ffffffff-fffe",
        },
    ]
}


class TestAppsByAgentIds(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AppsByAgentIds())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_inputs_ids(self, mock_request):
        actual = self.action.run({Input.IDS: ["1000000000000000000"]})
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_no_inputs(self, mock_request):
        actual = self.action.run({Input.IDS: []})
        self.assertEqual(expected, actual)
