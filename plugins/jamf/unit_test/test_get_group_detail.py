import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
from unittest import TestCase, mock

from icon_jamf.actions.get_group_detail import GetGroupDetail
from icon_jamf.actions.get_group_detail.schema import Input, Output
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


class TestGetGroupDetail(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_action_connector(STUB_CONNECTION, GetGroupDetail())

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_group_details_ok(self, mocked_get) -> None:
        response = self.action.run({Input.ID: STUB_DEVICE_ID})
        expected_response = {
            Output.GROUP_DETAIL: {
                "id": 1,
                "name": "iPhones",
                "is_smart": True,
                "criteria": [
                    {
                        "size": 1,
                        "criterion": {
                            "name": "Last Inventory Update",
                            "priority": 0,
                            "and_or": "and",
                            "search_type": "more than x days ago",
                            "value": 7,
                            "opening_paren": False,
                            "closing_paren": False,
                        },
                    }
                ],
                "site": {"id": -1, "name": "None"},
                "mobile_devices": [
                    {
                        "mobile_device": {
                            "id": 1,
                            "name": "Example iPhone",
                            "mac_address": "E0:E0:E0:E0:E0:E0",
                            "udid": "1111111-1111-1111-1111-111111111111",
                            "wifi_mac_address": "E0:AC:CB:97:36:G4",
                            "serial_number": "EXAMPLE_SERIAL",
                        }
                    }
                ],
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
    def test_get_group_details_exception(self, mock_request, exception) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ID: STUB_DEVICE_ID})
        self.assertEqual(context.exception.cause, exception)
