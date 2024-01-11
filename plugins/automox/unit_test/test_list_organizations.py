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
)
from icon_automox.actions.list_organizations import ListOrganizations
from icon_automox.actions.list_organizations.schema import Output


class TestListOrganizations(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListOrganizations())

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_list_organizations_ok(self, mock: Mock) -> None:
        response = self.action.run()
        expected_response = {
            Output.ORGANIZATIONS: [
                {
                    "id": 1234,
                    "name": "Global Zone",
                    "create_time": "2021-10-20T04:03:25+0000",
                    "access_key": "00000000-0000-0000-0000-000000000000",
                    "trial_end_time": "2024-02-03T00:00:00+0000",
                    "sub_plan": "FULL",
                    "rate_id": 1,
                    "billing_name": "Test",
                    "billing_email": "example@automox.com",
                    "uuid": "00000000-0000-0000-0000-0000000000000",
                    "device_count": 2,
                },
                {
                    "id": 1235,
                    "name": "Another One",
                    "create_time": "2021-10-26T08:14:25+0000",
                    "access_key": "00000000-0000-0000-0000-000000000000",
                    "trial_end_time": "2021-11-03T00:00:00+0000",
                    "trial_expired": True,
                    "sub_plan": "FULL",
                    "rate_id": 1,
                    "parent_id": 1234,
                    "uuid": "00000000-0000-0000-0000-000000000000",
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
    def test_list_organizations_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
