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
)
from icon_automox.actions.list_policies import ListPolicies
from icon_automox.actions.list_policies.schema import Input, Output


class TestListPolicies(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListPolicies())
        self.params = {Input.ORG_ID: ORG_ID}

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_list_policies_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.POLICIES: [
                {
                    "id": 1234,
                    "uuid": "00000000-0000-0000-0000-000000000000",
                    "name": "Test notification",
                    "policy_type_name": "custom",
                    "organization_id": 103871,
                    "configuration": {
                        "os_family": "Windows",
                        "notify_reboot_user": True,
                        "notify_deferred_reboot_user": True,
                        "pending_reboot_deferral_enabled": True,
                        "custom_pending_reboot_notification_message": "Updates require restart: Please save your work.",
                        "notify_deferred_reboot_user_message_timeout": 15,
                        "custom_pending_reboot_notification_max_delays": 3,
                        "custom_pending_reboot_notification_message_mac": "Updates require restart: Please save your work.",
                        "custom_pending_reboot_notification_deferment_periods": [1, 4, 8],
                    },
                    "schedule_time": "00:00",
                    "create_time": "2023-10-25T21:56:48+0000",
                    "server_groups": [1234],
                    "server_count": 5,
                    "status": "inactive",
                }
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
    def test_list_policies_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
