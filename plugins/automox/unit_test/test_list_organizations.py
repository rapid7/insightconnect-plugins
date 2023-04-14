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
                    "name": "ExampleTestOrg",
                    "create_time": "2023-03-01T12:00:00+0000",
                    "access_key": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                    "trial_end_time": "2023-03-01T12:00:00+0000",
                    "trial_expired": True,
                    "sub_plan": "FULL",
                    "rate_id": 1,
                    "bill_overages": True,
                    "metadata": {"patchServersDone": True},
                    "billing_name": "ExampleTestOrg",
                    "billing_email": "user@example.com",
                    "device_count": 1,
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
    def test_list_organizations_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
