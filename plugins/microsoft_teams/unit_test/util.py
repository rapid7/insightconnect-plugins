import json
import logging
import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))


class MockGraphApiClient:
    """Mock Graph API client for unit tests."""

    def __init__(self):
        self.get_teams = MagicMock()
        self.get_channels = MagicMock()
        self.create_channel = MagicMock()
        self.delete_channel = MagicMock()
        self.get_channel_messages = MagicMock()
        self.get_channel_message = MagicMock()
        self.get_chat_message = MagicMock()
        self.list_chat_messages = MagicMock()
        self.get_message_replies = MagicMock()
        self.get_user_info = MagicMock()
        self.add_member_to_group = MagicMock()
        self.remove_member_from_group = MagicMock()
        self.add_group_owner = MagicMock()
        self.add_member_to_channel = MagicMock()
        self.create_group = MagicMock()
        self.delete_group = MagicMock()
        self.get_group_id_from_name = MagicMock()
        self.enable_teams_for_group = MagicMock()
        self.create_chat = MagicMock()
        self.install_app_in_chat = MagicMock()


class MockBotService:
    """Mock Bot Framework service for unit tests."""

    def __init__(self):
        self.send_channel_message = MagicMock()
        self.send_chat_message = MagicMock()


class MockConnection:
    def __init__(self):
        self.tenant_id = "1"
        self.resource_endpoint = "https://graph.microsoft.com"
        self.app_catalog_id = ""
        self.client = MockGraphApiClient()
        self.bot = MockBotService()

    def get_headers(self, force_refresh=False):
        return {"Authorization": "Bearer mock_token", "Content-Type": "application/json"}


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = MockConnection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_data(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        )
