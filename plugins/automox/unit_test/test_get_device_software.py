import os
import sys

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from util import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
    ORG_ID,
    DEVICE_ID,
)
from icon_automox.actions.get_device_software import GetDeviceSoftware
from icon_automox.actions.get_device_software.schema import Input, Output


class TestGetDeviceSoftware(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetDeviceSoftware())
        self.params = {Input.ORG_ID: ORG_ID, Input.DEVICE_ID: DEVICE_ID}

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_get_device_software_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.SOFTWARE: [
                {
                    "id": 1234,
                    "server_id": 1234,
                    "package_id": 1234,
                    "software_id": 1234,
                    "installed": True,
                    "name": "com.apple.appleseed.FeedbackAssistant",
                    "display_name": "Feedback Assistant",
                    "version": "5.1",
                    "repo": "Apple-System",
                    "package_version_id": 1234,
                    "os_name": "OS X",
                    "os_version": "12.2",
                    "os_version_id": 1234,
                    "create_time": "2021-12-20T16:21:21+0000",
                    "organization_id": 1234,
                },
                {
                    "id": 1234,
                    "server_id": 1234,
                    "package_id": 1234,
                    "software_id": 1234,
                    "installed": True,
                    "name": "com.apple.calculator",
                    "display_name": "Calculator",
                    "version": "10.16",
                    "repo": "Apple-System",
                    "package_version_id": 1234,
                    "os_name": "OS X",
                    "os_version": "12.2",
                    "os_version_id": 1234,
                    "create_time": "2021-12-26T17:23:19+0000",
                    "organization_id": 1234,
                },
            ]
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
    def test_get_device_software_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
