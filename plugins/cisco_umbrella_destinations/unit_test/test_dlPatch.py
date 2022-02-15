import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlPatch import DlPatch
from icon_cisco_umbrella_destinations.actions.dlPatch.schema import Input
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


class TestDlPatch(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlPatch()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID, Input.LABEL: "DUMMYNAME"}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_successful(self, mock_patch):
        response = self.action.run(self.params)
        expected_response = {
            "success": {
                "status": {"code": 200, "text": "OK"},
                "data": {
                    "id": 15755492,
                    "organizationId": 2372338,
                    "access": "allow",
                    "isGlobal": False,
                    "name": "DUMMYNAME",
                    "thirdpartyCategoryId": None,
                    "createdAt": "2022-01-28T14:11:53+0000",
                    "modifiedAt": "2022-02-02T14:15:29+0000",
                    "isMspDefault": False,
                    "markedForDeletion": False,
                    "bundleTypeId": 1,
                    "meta": {"destinationCount": 1},
                },
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
