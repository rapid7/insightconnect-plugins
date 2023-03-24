import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


from unittest import TestCase, mock
from icon_zoom.connection.connection import Connection
from icon_zoom.actions.get_user import GetUser
from icon_zoom.actions.get_user.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
import logging

from unit_test.mock import (
    STUB_CONNECTION,
    STUB_USER_ID,
    mock_request_201,
    mock_request_400,
    mock_request_404,
    mocked_request,
)


class TestGetUser(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetUser()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {Input.USER_ID: STUB_USER_ID}

    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_get_user_success(self, mock_post):
        response = self.action.run(self.params)
        expected_response = {
            "user": {
                "id": "L7h_1I3YTWmId_E89-_Sbg",
                "first_name": "",
                "last_name": "",
                "display_name": "",
                "type": 1,
                "role_name": "",
                "verified": 0,
                "created_at": "2023-03-23T15:33:52Z",
                "group_ids": [],
                "im_group_ids": [],
                "account_id": "",
                "language": "",
                "phone_country": "",
                "phone_number": "",
                "status": "pending",
                "login_types": [],
                "user_created_at": "2021-10-11T14:02:35Z",
            },
            "version": "v1",
            "type": "action_event",
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
