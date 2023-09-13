import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from util import Util
from icon_microsoft_teams.actions.get_reply_list import GetReplyList
from icon_microsoft_teams.actions.get_reply_list.schema import Input
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class TestGetReplyList(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetReplyList())
        self.payload = {
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "Example Channel",
            Input.MESSAGE_ID: "1234567890",
        }

    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    def test_get_reply_list(self, mock: Mock):
        response = self.action.run(self.payload)

        expected_response = remove_null_and_clean(Util.load_data("get_reply_list"))
        self.assertEqual(response["messages"], expected_response.get("value"))
