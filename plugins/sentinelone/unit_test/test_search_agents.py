import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.search_agents import SearchAgents
from komand_sentinelone.actions.search_agents.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestSearchAgents(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SearchAgents())

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_success_when_array_fields_set_to_none(self, mock_request):
        actual = self.action.run(
            {
                Input.AGENT: "10.10.10.10",
                Input.AGENT_ACTIVE: True,
                Input.CASE_SENSITIVE: True,
                Input.OPERATIONAL_STATE: "Any",
            }
        )
        expected = {
            "agents": [
                {
                    "accountId": "433241117337583618",
                    "accountName": "SentinelOne",
                    "activeDirectory": {
                        "computerDistinguishedName": "None",
                        "computerMemberOf": [],
                        "lastUserDistinguishedName": "None",
                        "lastUserMemberOf": [],
                    },
                    "activeThreats": 0,
                    "agentVersion": "4.1.4.82",
                    "allowRemoteShell": False,
                    "appsVulnerabilityStatus": "up_to_date",
                    "cloudProviders": {},
                    "computerName": "so-agent-win12",
                    "consoleMigrationStatus": "N/A",
                    "coreCount": 1,
                    "cpuCount": 1,
                    "cpuId": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
                    "createdAt": "2020-05-28T14:53:03.014660Z",
                    "domain": "WORKGROUP",
                    "encryptedApplications": False,
                    "externalIp": "198.51.100.100",
                    "firewallEnabled": True,
                    "groupId": "521580416411822676",
                    "groupIp": "198.51.100.x",
                    "groupName": "Default Group",
                    "id": "901345720792880606",
                    "inRemoteShellSession": False,
                    "infected": False,
                    "installerType": ".exe",
                    "isActive": True,
                    "isDecommissioned": False,
                    "isPendingUninstall": False,
                    "isUninstalled": False,
                    "isUpToDate": True,
                    "lastActiveDate": "2020-06-05T18:32:56.748620Z",
                    "lastIpToMgmt": "10.4.24.55",
                    "locationEnabled": True,
                    "locationType": "fallback",
                    "locations": [],
                    "machineType": "server",
                    "mitigationMode": "protect",
                    "mitigationModeSuspicious": "detect",
                    "modelName": "VMware, Inc. - VMware Virtual Platform",
                    "networkInterfaces": [],
                    "networkQuarantineEnabled": False,
                    "networkStatus": "disconnected",
                    "operationalState": "na",
                    "operationalStateExpiration": "None",
                    "osArch": "64 bit",
                    "osName": "Windows Server 2012 Standard",
                    "osRevision": "9200",
                    "osStartTime": "2020-05-28T14:59:36Z",
                    "osType": "windows",
                    "osUsername": "None",
                    "rangerStatus": "NotApplicable",
                    "rangerVersion": "None",
                    "registeredAt": "2020-05-28T14:53:03.010853Z",
                    "remoteProfilingState": "disabled",
                    "remoteProfilingStateExpiration": "None",
                    "scanAbortedAt": "None",
                    "scanFinishedAt": "2020-05-28T22:24:59.420166Z",
                    "scanStartedAt": "2020-05-28T21:12:58.216807Z",
                    "scanStatus": "finished",
                    "siteId": "521580416395045459",
                    "siteName": "Rapid7",
                    "threatRebootRequired": False,
                    "totalMemory": 1023,
                    "updatedAt": "2020-06-05T15:39:10.754112Z",
                    "userActionsNeeded": [],
                    "uuid": "28db47168fa54f89aeed99769ac8d4dc",
                }
            ]
        }
        self.assertEqual(expected, actual)

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_success_good_response(self, mock_request):
        actual = self.action.run(
            {
                Input.AGENT: "10.10.10.11",
                Input.AGENT_ACTIVE: True,
                Input.CASE_SENSITIVE: True,
                Input.OPERATIONAL_STATE: "Any",
            }
        )

        expected = {
            "agents": [
                {
                    "accountId": "433241117337583618",
                    "accountName": "SentinelOne",
                    "activeDirectory": {
                        "computerDistinguishedName": "None",
                        "computerMemberOf": [],
                        "lastUserDistinguishedName": "None",
                        "lastUserMemberOf": [],
                    },
                    "activeThreats": 0,
                    "agentVersion": "4.1.4.82",
                    "allowRemoteShell": False,
                    "appsVulnerabilityStatus": "up_to_date",
                    "cloudProviders": {},
                    "computerName": "so-agent-win12",
                    "consoleMigrationStatus": "N/A",
                    "coreCount": 1,
                    "cpuCount": 1,
                    "cpuId": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
                    "createdAt": "2020-05-28T14:53:03.014660Z",
                    "domain": "WORKGROUP",
                    "encryptedApplications": False,
                    "externalIp": "198.51.100.100",
                    "firewallEnabled": True,
                    "groupId": "521580416411822676",
                    "groupIp": "198.51.100.x",
                    "groupName": "Default Group",
                    "id": "901345720792880606",
                    "inRemoteShellSession": False,
                    "infected": False,
                    "installerType": ".exe",
                    "isActive": True,
                    "isDecommissioned": False,
                    "isPendingUninstall": False,
                    "isUninstalled": False,
                    "isUpToDate": True,
                    "lastActiveDate": "2020-06-05T18:32:56.748620Z",
                    "lastIpToMgmt": "10.4.24.55",
                    "locationEnabled": True,
                    "locationType": "fallback",
                    "locations": [{"id": "629380164464502476", "name": "Fallback", "scope": "global"}],
                    "machineType": "server",
                    "mitigationMode": "protect",
                    "mitigationModeSuspicious": "detect",
                    "modelName": "VMware, Inc. - VMware Virtual Platform",
                    "networkInterfaces": [
                        {
                            "id": "901345720801269215",
                            "inet": ["198.51.100.100"],
                            "inet6": ["2001:db8:8:4::2"],
                            "name": "Ethernet",
                            "physical": "00:50:56:94:17:08",
                        }
                    ],
                    "networkQuarantineEnabled": False,
                    "networkStatus": "disconnected",
                    "operationalState": "na",
                    "operationalStateExpiration": "None",
                    "osArch": "64 bit",
                    "osName": "Windows Server 2012 Standard",
                    "osRevision": "9200",
                    "osStartTime": "2020-05-28T14:59:36Z",
                    "osType": "windows",
                    "osUsername": "None",
                    "rangerStatus": "NotApplicable",
                    "rangerVersion": "None",
                    "registeredAt": "2020-05-28T14:53:03.010853Z",
                    "remoteProfilingState": "disabled",
                    "remoteProfilingStateExpiration": "None",
                    "scanAbortedAt": "None",
                    "scanFinishedAt": "2020-05-28T22:24:59.420166Z",
                    "scanStartedAt": "2020-05-28T21:12:58.216807Z",
                    "scanStatus": "finished",
                    "siteId": "521580416395045459",
                    "siteName": "Rapid7",
                    "threatRebootRequired": False,
                    "totalMemory": 1023,
                    "updatedAt": "2020-06-05T15:39:10.754112Z",
                    "userActionsNeeded": [],
                    "uuid": "28db47168fa54f89aeed99769ac8d4dc",
                }
            ]
        }
        self.assertEqual(expected, actual)
