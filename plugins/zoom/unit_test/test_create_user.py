import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_zoom.actions.create_user import CreateUser
from insightconnect_plugin_runtime.exceptions import PluginException

from mock import (
    Util,
    STUB_CREATE_USER,
    mock_request_201,
    mock_request_400,
    mock_request_404,
    mock_request_409,
    mock_request_429,
    mocked_request,
)


class TestCreateUser(TestCase):
    @mock.patch("requests.request", side_effect=mock_request_201)
    def setUp(self, mock_request) -> None:
        mocked_request(mock_request)
        self.action = Util.default_connector(CreateUser())
        self.params = STUB_CREATE_USER

    @mock.patch("icon_zoom.util.api.ZoomAPI.authenticate")
    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_create_user_success(self, mock_post, mock_auth):
        mock_auth.return_value = 200
        response = self.action.run(self.params)
        expected_response = {
            "email": "jchill@example.com",
            "first_name": "Jill",
            "id": "KDcuGIm1QgePTO8WbOqwIQ",
            "last_name": "Chill",
            "type": 1,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    @mock.patch("icon_zoom.util.api.ZoomAPI._refresh_oauth_token", return_value=None)
    def test_not_ok(self, mock_request, exception, mock_refresh):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
