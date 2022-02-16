import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dGet import DGet
from icon_cisco_umbrella_destinations.actions.dGet.schema import Input
from icon_cisco_umbrella_destinations.util.api import ERROR_MSG
from insightconnect_plugin_runtime.exceptions import PluginException
import logging

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    STUB_DESTINATION_LIST_ID,
    mocked_request,
)


class TestDGet(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DGet()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_destination_get_success(self, mock_get):
        response = self.action.run(self.params)
        expected_response = {
            "success": {
                "status": {"code": 200, "text": "OK"},
                "meta": {"page": 1, "limit": 100, "total": 3},
                "data": [
                    {
                        "id": "6672",
                        "destination": "google.co.uk",
                        "type": "domain",
                        "comment": "comment",
                        "createdAt": "2022-02-02 14:04:29",
                    },
                    {
                        "id": "183128",
                        "destination": "stackoverflow.com",
                        "type": "domain",
                        "comment": "another",
                        "createdAt": "2022-01-31 17:07:15",
                    },
                    {
                        "id": "42882950",
                        "destination": "enteradestination",
                        "type": "domain",
                        "comment": "EnterAComment",
                        "createdAt": "2022-01-31 17:06:28",
                    },
                ],
            }
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, ERROR_MSG),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
