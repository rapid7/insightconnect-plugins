import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.add_group_owner.action import AddGroupOwner
from icon_microsoft_teams.actions.add_group_owner.schema import AddGroupOwnerInput, AddGroupOwnerOutput, Input
from jsonschema import validate

from util import Util


class TestAddGroupOwner(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddGroupOwner())
        self.action.connection.client.get_user_info.return_value = {"id": "user-123", "displayName": "Test User"}
        self.action.connection.client.get_group_id_from_name.return_value = "group-456"
        self.action.connection.client.add_group_owner.return_value = True

    def test_add_group_owner(self) -> None:
        test_input = {Input.GROUP_NAME: "test", Input.MEMBER_LOGIN: "test@example.com"}
        validate(test_input, AddGroupOwnerInput.schema)
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        validate(response, AddGroupOwnerOutput.schema)
        self.action.connection.client.get_user_info.assert_called_with("test@example.com")
        self.action.connection.client.get_group_id_from_name.assert_called_with("test")
        self.action.connection.client.add_group_owner.assert_called_with("group-456", "user-123")
