import sys
import os

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlCreate import DlCreate
from icon_cisco_umbrella_destinations.actions.dlCreate.schema import Input
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


class TestDlCreate(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlCreate()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.data = {
            "access": "allow",
            "isGlobal": False,
            "name": "DELETEME2",
        }

        self.params = {Input.ACCESS: "allow", Input.ISGLOBAL: False, Input.LABEL: "DELETEME2"}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_successful(self, mock_post):
        response = self.action.run({Input.ACCESS: "allow", Input.ISGLOBAL: False, Input.LABEL: "DELETEME2"})
        expected_response = {
            "success": {
                "id": 15786904,
                "organizationId": 2372338,
                "access": "allow",
                "isGlobal": False,
                "name": "DELETEME2",
                "createdAt": "2022-02-10T11:01:20+0000",
                "modifiedAt": "2022-02-10T11:01:20+0000",
                "isMspDefault": False,
                "markedForDeletion": False,
                "bundleTypeId": 1,
                "meta": {"destinationCount": 0},
            }
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_401, PluginException.Preset.USERNAME_PASSWORD),
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.UNAUTHORIZED),
            (mock_request_500, PluginException.Preset.SERVER_ERROR),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, PluginException.causes[exception])
