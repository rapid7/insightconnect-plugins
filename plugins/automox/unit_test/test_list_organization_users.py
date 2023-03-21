import os
import sys

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from unit_test.util import (
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
                    "uuid": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                    "firstname": "ExampleName",
                    "lastname": "ExampleLastName",
                    "email": "user@example.com",
                    "prefs": [{"user_id": 12345, "pref_name": "notify.weeklydigest", "value": "true"}],
                    "orgs": [
                        {
                            "id": 12345,
                            "zone_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                            "name": "ExampleTestOrg",
                            "trial_end_time": "2023-03-01T12:00:00+0000",
                            "trial_expired": True,
                            "create_time": "2023-03-01T12:00:00+0000",
                            "plan": "manage",
                            "parent_id": "None",
                            "access_key": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                        }
                    ],
                    "rbac_roles": [
                        {
                            "id": 1,
                            "name": "Administrator",
                            "description": "Provides full administrative rights to a specific zone.",
                            "organization_id": 12345,
                        }
                    ],
                    "account_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                    "account_name": "ExampleTestOrg",
                    "account_rbac_role": "global-admin",
                    "account_completed_qsg": True,
                    "account_created_at": "2023-03-01T12:00:00+0000",
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
