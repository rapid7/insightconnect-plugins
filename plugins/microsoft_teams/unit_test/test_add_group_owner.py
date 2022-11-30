import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from icon_microsoft_teams.actions.add_group_owner.action import AddGroupOwner
from icon_microsoft_teams.actions.add_group_owner.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util

STUB_GROUP_NAME = "test"
STUB_MEMBER_LOGIN = "test"

STUB_EXAMPLE_ACTION_RESPONSE = {"success": True}


class TestAddGroupOwner(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddGroupOwner())

        self.payload = {Input.GROUP_NAME: STUB_GROUP_NAME, Input.MEMBER_LOGIN: STUB_MEMBER_LOGIN}

    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    @mock.patch("requests.post", side_effect=Util.mocked_requests)
    def test_add_group_owner(self, mock_requests_get, mock_requests_post) -> None:
        response = self.action.run(self.payload)
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(response, expected_response)
