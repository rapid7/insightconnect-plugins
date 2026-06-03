import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_microsoft_teams.actions.install_app import InstallApp
from icon_microsoft_teams.actions.install_app.schema import InstallAppInput, InstallAppOutput
from icon_microsoft_teams.util.graph_api_client import GraphApiClient
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


class TestInstallApp(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(InstallApp())

    def test_install_app_in_team(self) -> None:
        test_input = {
            "team_id": "ee0f5ae2-8bc6-4ae5-8466-7daeebbfa062",
            "app_id": "05F59CEC-A742-4A50-A62E-202A57E478A4",
        }
        validate(test_input, InstallAppInput.schema)
        actual = self.action.run(test_input)
        self.assertTrue(actual["success"])
        validate(actual, InstallAppOutput.schema)
        self.action.connection.client.install_app_in_team.assert_called_once_with(
            "ee0f5ae2-8bc6-4ae5-8466-7daeebbfa062",
            "05F59CEC-A742-4A50-A62E-202A57E478A4",
        )

    def test_install_app_in_chat(self) -> None:
        test_input = {
            "chat_id": "19:ea28e88c00e94c7786b065394a61f296@thread.v2",
            "app_id": "05F59CEC-A742-4A50-A62E-202A57E478A4",
        }
        validate(test_input, InstallAppInput.schema)
        actual = self.action.run(test_input)
        self.assertTrue(actual["success"])
        validate(actual, InstallAppOutput.schema)
        self.action.connection.client.install_app_in_chat.assert_called_once_with(
            "19:ea28e88c00e94c7786b065394a61f296@thread.v2",
            "05F59CEC-A742-4A50-A62E-202A57E478A4",
        )

    def test_install_app_no_target_raises(self) -> None:
        test_input = {
            "app_id": "05F59CEC-A742-4A50-A62E-202A57E478A4",
        }
        validate(test_input, InstallAppInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)
        self.assertIn("No target specified", context.exception.cause)

    def test_install_app_both_targets_raises(self) -> None:
        test_input = {
            "team_id": "ee0f5ae2-8bc6-4ae5-8466-7daeebbfa062",
            "chat_id": "19:ea28e88c00e94c7786b065394a61f296@thread.v2",
            "app_id": "05F59CEC-A742-4A50-A62E-202A57E478A4",
        }
        validate(test_input, InstallAppInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)
        self.assertIn("Both Team ID and Chat ID", context.exception.cause)


class TestGraphApiClientInstallApp(TestCase):
    """Tests for the GraphApiClient install_app methods."""

    def setUp(self) -> None:
        self.client = GraphApiClient.__new__(GraphApiClient)
        self.client._base_url = "https://graph.microsoft.com"
        self.client._logger = MagicMock()
        self.client._get_auth_headers = MagicMock(return_value={"Authorization": "Bearer token"})
        self.client._call_api = MagicMock()
        self.client._raise_for_status = MagicMock()

    def test_install_app_in_team_success(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        self.client._call_api.return_value = mock_response

        self.client.install_app_in_team("team-123", "app-456")

        self.client._call_api.assert_called_once_with(
            "POST",
            "https://graph.microsoft.com/v1.0/teams/team-123/installedApps",
            headers={"Authorization": "Bearer token"},
            json={"teamsApp@odata.bind": "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/app-456"},
        )
        self.client._raise_for_status.assert_not_called()

    def test_install_app_in_team_201(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 201
        self.client._call_api.return_value = mock_response

        self.client.install_app_in_team("team-123", "app-456")
        self.client._raise_for_status.assert_not_called()

    def test_install_app_in_team_error(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 403
        self.client._call_api.return_value = mock_response

        self.client.install_app_in_team("team-123", "app-456")
        self.client._raise_for_status.assert_called_once_with(mock_response)

    def test_install_app_in_chat_success(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 201
        self.client._call_api.return_value = mock_response

        self.client.install_app_in_chat("19:chat-id@thread.v2", "app-789")

        self.client._call_api.assert_called_once_with(
            "POST",
            "https://graph.microsoft.com/v1.0/chats/19:chat-id@thread.v2/installedApps",
            headers={"Authorization": "Bearer token"},
            json={"teamsApp@odata.bind": "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/app-789"},
        )
        self.client._raise_for_status.assert_not_called()

    def test_install_app_in_chat_error(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 404
        self.client._call_api.return_value = mock_response

        self.client.install_app_in_chat("19:chat-id@thread.v2", "app-789")
        self.client._raise_for_status.assert_called_once_with(mock_response)
