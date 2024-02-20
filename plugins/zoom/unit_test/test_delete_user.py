import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import MagicMock

from icon_zoom.actions.delete_user import DeleteUser
from icon_zoom.actions.delete_user.schema import Input, DeleteUserInput, DeleteUserOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from mock import Util, mock_request_204, mock_request_400, mock_request_404, mocked_request

STUB_DELETE_USER_QUERY_PARAMS = {
    Input.ID: "12345",
    Input.ACTION: "delete",
    Input.TRANSFER_EMAIL: "user@example.com",
    Input.TRANSFER_WEBINARS: False,
    Input.TRANSFER_RECORDINGS: False,
    Input.TRANSFER_MEETINGS: False,
}


class TestDeleteUser(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_204)
    def setUp(self, mock_delete: MagicMock) -> None:
        self.action = Util.default_connector(DeleteUser())
        self.params = STUB_DELETE_USER_QUERY_PARAMS

    @mock.patch("requests.request", side_effect=mock_request_204)
    def delete_user_success(self, mock_delete: MagicMock) -> None:
        # mocked_request(mock_request_204)
        validate(self.params, DeleteUserInput.schema)
        response = self.action.run(self.params)
        expected_response = None
        self.assertEqual(response, expected_response)
        validate(response, DeleteUserOutput.schema)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ]
    )
    @mock.patch("icon_zoom.util.api.ZoomAPI._refresh_oauth_token", return_value=None)
    def test_not_ok(self, mock_request: MagicMock, exception: str, mock_refresh: MagicMock) -> None:
        validate(self.params, DeleteUserInput.schema)
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
