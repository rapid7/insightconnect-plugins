import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dAdd import DAdd
from icon_cisco_umbrella_destinations.actions.dAdd.schema import Input
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
    STUB_RESPONSE,
)


class TestDAdd(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DAdd()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {
            Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID,
            Input.DESTINATION: "dummyDestination",
            Input.COMMENT: "dummyComment",
        }

        self.params_no_comment = {
            Input.DESTINATIONLISTID: STUB_DESTINATION_LIST_ID,
            Input.DESTINATION: "dummyDestination",
        }

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_if_ok(self, mock_post):
        response = self.action.run(self.params)
        expected_response = STUB_RESPONSE
        self.assertEqual(response, expected_response)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_if_comment_is_none(self, mock_post):
        response = self.action.run(self.params_no_comment)
        expected_response = STUB_RESPONSE
        self.assertEqual(response, expected_response)

    # @mock.patch("requests.request", side_effect=mock_request_200_invalid_json)
    # def test_if_invalid_json(self, mock_post):
    #     # Need to send across call which returns 200
    #     response = self.action.run()
    #     # Need to map a JSON Decode error here
    #     expected_response =
    #     self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, "Invalid input data, ensure the information you are inputting is correct"),
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
