import sys
import os

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from typing import Any, Dict
from unittest import TestCase, mock
from unittest.mock import Mock

from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dAdd import DAdd
from icon_cisco_umbrella_destinations.actions.dAdd.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    STUB_DESTINATION_LIST_ID,
    mocked_request,
)


class TestDAdd(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DAdd())

        self.params = {
            Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID,
            Input.DESTINATION: "dummyDestination",
            Input.COMMENT: "dummyComment",
        }

        self.params_no_comment = {
            Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID,
            Input.DESTINATION: "dummyDestination",
        }

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_if_ok(self, mock_post):
        mocked_request(mock_post)
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

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_if_comment_is_none(self, mock_post):
        response = self.action.run(self.params_no_comment)
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
