import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_thehive.actions.get_current_user import GetCurrentUser
from insightconnect_plugin_runtime.exceptions import PluginException

from parameterized import parameterized
from unit_test.mock import (
    Util,
    mocked_request,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
)


class TestGetCurrentUser(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(GetCurrentUser())

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_current_user(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()
        expected = {
            "success": {
                "_routing": "admin",
                "hasKey": True,
                "preferences": {},
                "updatedBy": "admin",
                "roles": ["read", "write", "admin"],
                "_type": "user",
                "createdAt": 1544021746094,
                "_parent": None,
                "createdBy": "init",
                "name": "Administrator",
                "_id": "admin",
                "id": "admin",
                "_version": 1,
                "updatedAt": 1544215737382,
                "status": "Ok",
            }
        }
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
