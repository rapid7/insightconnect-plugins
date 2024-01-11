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
from icon_automox.actions.list_organization_users import ListOrganizationUsers
from icon_automox.actions.list_organization_users.schema import Input, Output


class TestListOrganizationUsers(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListOrganizationUsers())
        self.params = {Input.ORG_ID: ORG_ID}

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_list_organization_users_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.USERS: [
                {
                    "id": 1234,
                    "uuid": "00000000-0000-0000-0000-000000000000",
                    "firstname": "User",
                    "lastname": "Example",
                    "email": "user@example.com",
                    "prefs": [
                        {"user_id": 1234, "pref_name": "notify.system.add", "value": "false"},
                        {"user_id": 1234, "pref_name": "notify.weeklydigest", "value": "true"},
                        {"user_id": 1234, "pref_name": "user.tfa", "value": "email"},
                    ],
                    "orgs": [
                        {
                            "id": 1234,
                            "zone_id": "00000000-0000-0000-0000-000000000000",
                            "name": "Global Zone",
                            "trial_end_time": "2024-02-03T00:00:00+00:00",
                            "create_time": "2021-10-20T04:03:25+0000",
                            "plan": "manage",
                            "access_key": "00000000-0000-0000-0000-000000000000",
                        },
                        {
                            "id": 1235,
                            "zone_id": "00000000-0000-0000-0000-000000000000",
                            "name": "Local Zone",
                            "trial_end_time": "2021-11-03T00:00:00+00:00",
                            "trial_expired": True,
                            "create_time": "2021-10-26T08:14:25+0000",
                            "plan": "manage",
                            "parent_id": 1234,
                            "access_key": "00000000-0000-0000-0000-000000000000",
                        },
                    ],
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
    def test_list_organization_users_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
