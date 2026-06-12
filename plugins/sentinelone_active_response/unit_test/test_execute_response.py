import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from komand_sentinelone_active_response.actions.execute_response.action import ExecuteResponse
from komand_sentinelone_active_response.actions.execute_response.schema import Input, Output
from unit_test.util import default_connector

AGENT_CONNECTED = {
    "id": "1234567890123456789",
    "computerName": "WORKSTATION-01",
    "networkStatus": "connected",
    "osName": "Windows 10 Pro",
    "siteName": "Default Site",
    "groupName": "Default Group",
    "activeThreats": 0,
    "agentVersion": "23.1.2.400",
    "networkInterfaces": [{"inet": ["192.168.1.100"], "physical": "00:1A:2B:3C:4D:5E"}],
}

AGENT_DISCONNECTED = {
    "id": "1234567890123456789",
    "computerName": "WORKSTATION-01",
    "networkStatus": "disconnected",
    "osName": "Windows 10 Pro",
    "siteName": "Default Site",
    "groupName": "Default Group",
    "activeThreats": 0,
    "agentVersion": "23.1.2.400",
    "networkInterfaces": [{"inet": ["192.168.1.100"], "physical": "00:1A:2B:3C:4D:5E"}],
}


class TestExecuteResponse(TestCase):
    def setUp(self):
        self.action = default_connector(ExecuteResponse())

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_contain_success(self, mock_sleep):
        """Test contain intent successfully disconnects an agent."""
        client = self.action.connection.client
        client.search_agents.return_value = [AGENT_CONNECTED]
        client.disconnect_agents.return_value = {"data": {"affected": 1}}
        client.get_agent_by_id.return_value = AGENT_DISCONNECTED

        result = self.action.run(
            {
                Input.ENDPOINT_IDENTIFIER: "WORKSTATION-01",
                Input.INTENT: "contain",
                Input.TIMEOUT: 120,
                Input.POLLING_INTERVAL: 10,
            }
        )

        report = result[Output.REPORT]
        self.assertEqual(report["result_status"], "success")
        self.assertEqual(report["action_performed"], "contain")
        self.assertEqual(report["agent"]["agent_id"], "1234567890123456789")
        self.assertEqual(report["agent"]["hostname"], "WORKSTATION-01")
        client.disconnect_agents.assert_called_once_with(["1234567890123456789"])

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_uncontain_success(self, mock_sleep):
        """Test uncontain intent successfully reconnects an agent."""
        client = self.action.connection.client
        client.search_agents.return_value = [AGENT_DISCONNECTED]
        client.connect_agents.return_value = {"data": {"affected": 1}}
        client.get_agent_by_id.return_value = AGENT_CONNECTED

        result = self.action.run(
            {
                Input.ENDPOINT_IDENTIFIER: "WORKSTATION-01",
                Input.INTENT: "uncontain",
                Input.TIMEOUT: 120,
                Input.POLLING_INTERVAL: 10,
            }
        )

        report = result[Output.REPORT]
        self.assertEqual(report["result_status"], "success")
        self.assertEqual(report["action_performed"], "uncontain")
        self.assertEqual(report["agent"]["network_status"], "connected")
        client.connect_agents.assert_called_once_with(["1234567890123456789"])

    def test_status_intent(self):
        """Test status intent returns agent status without calling disconnect/connect."""
        client = self.action.connection.client
        client.search_agents.return_value = [AGENT_CONNECTED]

        result = self.action.run(
            {
                Input.ENDPOINT_IDENTIFIER: "WORKSTATION-01",
                Input.INTENT: "status",
                Input.TIMEOUT: 120,
                Input.POLLING_INTERVAL: 10,
            }
        )

        report = result[Output.REPORT]
        self.assertEqual(report["result_status"], "success")
        self.assertEqual(report["action_performed"], "status")
        self.assertIn("connected", report["summary"])
        client.disconnect_agents.assert_not_called()
        client.connect_agents.assert_not_called()

    def test_info_intent(self):
        """Test info intent returns agent details without state change."""
        client = self.action.connection.client
        client.search_agents.return_value = [AGENT_CONNECTED]

        result = self.action.run(
            {
                Input.ENDPOINT_IDENTIFIER: "192.168.1.100",
                Input.INTENT: "info",
                Input.TIMEOUT: 120,
                Input.POLLING_INTERVAL: 10,
            }
        )

        report = result[Output.REPORT]
        self.assertEqual(report["result_status"], "success")
        self.assertEqual(report["action_performed"], "info")
        self.assertEqual(report["agent"]["hostname"], "WORKSTATION-01")
        self.assertEqual(report["agent"]["ip_address"], "192.168.1.100")
        self.assertEqual(report["agent"]["mac_address"], "00:1A:2B:3C:4D:5E")
        self.assertEqual(report["agent"]["operating_system"], "Windows 10 Pro")
        self.assertEqual(report["agent"]["site_name"], "Default Site")
        self.assertEqual(report["agent"]["group_name"], "Default Group")
        self.assertEqual(report["agent"]["active_threats"], 0)
        self.assertEqual(report["agent"]["agent_version"], "23.1.2.400")
        client.disconnect_agents.assert_not_called()
        client.connect_agents.assert_not_called()

    def test_validation_failure_empty_identifier(self):
        """Test that empty identifier raises PluginException before orchestrator runs."""
        client = self.action.connection.client

        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ENDPOINT_IDENTIFIER: "",
                    Input.INTENT: "contain",
                    Input.TIMEOUT: 120,
                    Input.POLLING_INTERVAL: 10,
                }
            )

        self.assertIn("empty", context.exception.cause.lower())
        client.search_agents.assert_not_called()

    def test_output_clean_strips_empty(self):
        """Test that clean() strips empty string fields from the output report."""
        client = self.action.connection.client
        client.search_agents.return_value = [AGENT_CONNECTED]

        result = self.action.run(
            {
                Input.ENDPOINT_IDENTIFIER: "WORKSTATION-01",
                Input.INTENT: "status",
                Input.TIMEOUT: 120,
                Input.POLLING_INTERVAL: 10,
            }
        )

        report = result[Output.REPORT]
        # clean() should remove fields with empty string values
        # error_cause and error_remediation are empty for a success case
        self.assertNotIn("error_cause", report)
        self.assertNotIn("error_remediation", report)
