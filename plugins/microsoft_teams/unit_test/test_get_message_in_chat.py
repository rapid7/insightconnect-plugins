import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from icon_microsoft_teams.actions.get_message_in_chat import GetMessageInChat
from icon_microsoft_teams.actions.get_message_in_chat.schema import Input, GetMessageInChatInput, GetMessageInChatOutput
from util import Util
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from jsonschema import validate


class TestGetMessageInChat(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetMessageInChat())
        self.payload = {
            Input.USERNAME: "user@example.com",
            Input.CHAT_ID: "11:examplechat.name",
            Input.MESSAGE_ID: "1234567890",
        }

    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    def test_get_message_in_chat(self, mock: Mock):
        validate(self.payload, GetMessageInChatInput.schema)
        response = self.action.run(self.payload)

        expected_response = remove_null_and_clean(Util.load_data("get_message_in_chat"))
        self.assertEqual(response["message"], expected_response)
        validate(response["message"], GetMessageInChatOutput.schema)
