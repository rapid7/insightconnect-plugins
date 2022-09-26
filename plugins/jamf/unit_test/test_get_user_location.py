import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from icon_jamf.actions.get_user_location import GetUserLocation
from icon_jamf.actions.get_user_location.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    STUB_DEVICE_ID,
    mock_request_200,
    mock_request_400,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mock_request_505,
    mocked_request,
)
from util import Util


class TestGetUserLocation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_action_connector(STUB_CONNECTION, GetUserLocation())

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_user_location_ok(self, mocked_get):
        response = self.action.run({Input.ID: STUB_DEVICE_ID})
        expected_response = {
            Output.USER_LOCATION_DETAIL: {
                "username": "Example Name",
                "real_name": "Example Name",
                "email_address": "user@example.com",
                "position": "Example Position",
                "phone": "111222333",
                "department": "Example Department",
                "building": "Example Building",
                "room": "Example Room",
            }
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_user_location_exception(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ID: STUB_DEVICE_ID})
        self.assertEqual(context.exception.cause, exception)
