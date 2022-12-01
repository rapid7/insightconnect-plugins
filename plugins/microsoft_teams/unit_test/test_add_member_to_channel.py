import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_microsoft_teams.actions.add_member_to_channel.action import AddMemberToChannel
from icon_microsoft_teams.actions.add_member_to_channel.schema import Input

from util import Util
from unittest import TestCase, mock

STUB_GROUP_NAME = "test"
STUB_MEMBER_LOGIN = "test"
STUB_CHANNEL_NAME = "Example Channel"
STUB_MEMBER_ROLE = "Owner"

STUB_EXAMPLE_ACTION_RESPONSE = {"success": True}


class TestAddMemberToChannel(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddMemberToChannel())

        self.payload = {
            Input.GROUP_NAME: STUB_GROUP_NAME,
            Input.MEMBER_LOGIN: STUB_MEMBER_LOGIN,
            Input.CHANNEL_NAME: STUB_CHANNEL_NAME,
            Input.ROLE: STUB_MEMBER_ROLE,
        }

    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    @mock.patch("requests.post", side_effect=Util.mocked_requests)
    def test_add_member_to_channel(self) -> None:
        response = self.action.run(self.payload)
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(response, expected_response)
