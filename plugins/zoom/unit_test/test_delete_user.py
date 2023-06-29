import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_zoom.actions.delete_user import DeleteUser
from icon_zoom.actions.delete_user.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from mock import (
    Util,
    mock_request_204,
    mock_request_400,
    mock_request_404,
    mocked_request,
)

STUB_DELETE_USER_QUERY_PARAMS = {
    Input.ID: "12345",
    Input.ACTION: "delete",
    Input.TRANSFER_EMAIL: "user@example.com",
    Input.TRANSFER_WEBINARS: "",
    Input.TRANSFER_RECORDINGS: "",
    Input.TRANSFER_MEETINGS: "",
}


class TestDeleteUser(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_204)
    def setUp(self, mock_delete) -> None:
        self.action = Util.default_connector(DeleteUser())
        self.params = STUB_DELETE_USER_QUERY_PARAMS

    @mock.patch("requests.request", side_effect=mock_request_204)
    def delete_user_success(self, mock_delete):
        # mocked_request(mock_request_204)
        response = self.action.run(self.params)
        expected_response = None

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ]
    )
    @mock.patch("icon_zoom.util.api.ZoomAPI._refresh_oauth_token", return_value=None)
    def test_not_ok(self, mock_request, exception, mock_refresh):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
