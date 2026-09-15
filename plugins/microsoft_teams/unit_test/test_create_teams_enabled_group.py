import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.create_teams_enabled_group import CreateTeamsEnabledGroup
from icon_microsoft_teams.actions.create_teams_enabled_group.schema import Input

from util import Util


class TestCreateTeamsEnabledGroup(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateTeamsEnabledGroup())
        self.action.connection.client.create_group.return_value = {
            "id": "new-group-id",
            "displayName": "Test Group",
            "description": "A test group",
            "mailNickname": "TestGroup",
            "mailEnabled": True,
            "securityEnabled": False,
        }
        self.action.connection.client.enable_teams_for_group.return_value = True

    def test_create_teams_enabled_group(self) -> None:
        test_input = {
            Input.GROUP_NAME: "Test Group",
            Input.GROUP_DESCRIPTION: "A test group",
            Input.MAIL_NICKNAME: "TestGroup",
            Input.MAIL_ENABLED: True,
            Input.OWNERS: ["owner@example.com"],
            Input.MEMBERS: ["member@example.com"],
        }
        response = self.action.run(test_input)
        self.assertEqual(response["group"]["displayName"], "Test Group")
        self.action.connection.client.create_group.assert_called_once()
        self.action.connection.client.enable_teams_for_group.assert_called_with("new-group-id")
