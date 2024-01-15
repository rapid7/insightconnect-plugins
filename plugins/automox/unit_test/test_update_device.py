import sys
import os

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from util import (
    Util,
    mock_request_200,
    mock_request_204,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
    ORG_ID,
    DEVICE_ID,
    POLICY_ID,
)

from icon_automox.actions.update_device import UpdateDevice
from icon_automox.actions.update_device.schema import Input, Output


class TestUpdateDevice(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(UpdateDevice())
        self.params = {
            Input.ORG_ID: ORG_ID,
            Input.CUSTOM_NAME: "apple",
            Input.DEVICE_ID: DEVICE_ID,
            Input.EXCEPTION: False,
            Input.SERVER_GROUP_ID: 1234,
            Input.TAGS: ["apple", "banana"],
        }

    @patch("requests.Session.request", side_effect=mock_request_200)
    @patch("requests.Session.request", side_effect=mock_request_204)
    def test_update_device_ok(self, mock: Mock, mock2: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.SUCCESS: True,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_200_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
        ],
    )
    def test_update_device_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
