import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.add_member_to_channel.action import AddMemberToChannel
from icon_microsoft_teams.actions.add_member_to_channel.schema import Input

from util import Util


class TestAddMemberToChannel(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddMemberToChannel())
        self.action.connection.client.get_group_id_from_name.return_value = "group-123"
        self.action.connection.client.get_channels.return_value = [{"id": "channel-456", "displayName": "Example Channel"}]
        self.action.connection.client.get_user_info.return_value = {"id": "user-789", "displayName": "Test User"}
        self.action.connection.client.add_member_to_channel.return_value = True

    def test_add_member_to_channel(self) -> None:
        test_input = {
            Input.GROUP_NAME: "test",
            Input.MEMBER_LOGIN: "test@example.com",
            Input.CHANNEL_NAME: "Example Channel",
            Input.ROLE: "Owner",
        }
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        self.action.connection.client.get_group_id_from_name.assert_called_with("test")
        self.action.connection.client.get_channels.assert_called_with("group-123", "Example Channel")
        self.action.connection.client.get_user_info.assert_called_with("test@example.com")
        self.action.connection.client.add_member_to_channel.assert_called_with("group-123", "channel-456", "user-789", "owner")
