import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from icon_microsoft_teams.actions.get_message_in_channel import GetMessageInChannel
from icon_microsoft_teams.actions.get_message_in_channel.schema import Input
from util import Util
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class TestGetMessageInChannel(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetMessageInChannel())
        self.payload = {
            Input.TEAM_ID: "example-team-id",
            Input.CHANNEL_ID: "11:examplechannel.name",
            Input.MESSAGE_ID: "1234567890",
            Input.REPLY_ID: "1234567891",
        }

    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    def test_get_message_in_channel(self, mock: Mock):
        response = self.action.run(self.payload)

        expected_response = remove_null_and_clean(Util.load_data("get_message_in_channel"))
        self.assertEqual(response["message"], expected_response)
