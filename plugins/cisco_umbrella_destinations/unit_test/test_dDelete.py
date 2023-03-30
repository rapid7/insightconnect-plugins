import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dDelete import DDelete
from icon_cisco_umbrella_destinations.actions.dDelete.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

import logging

from unit_test.mock import (
    Util,
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


class TestDDelete(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DDelete())
        self.params = {Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID, Input.PAYLOAD: "1234 5678"}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_successful(self, mock_delete):
        mocked_request(mock_delete)
        response = self.action.run(self.params)
        expected_response = {
            "success": {
                "id": 15755711,
                "access": "allow",
                "isGlobal": False,
                "name": "CreateListTest",
                "createdAt": "2022-01-28T16:03:36+0000",
                "modifiedAt": "2022-02-09T11:47:00+0000",
                "isMspDefault": False,
                "markedForDeletion": False,
                "bundleTypeId": 1,
                "meta": {"destinationCount": 5},
            },
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
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
