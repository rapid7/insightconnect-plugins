import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_zoom.connection.connection import Connection
from icon_zoom.actions.create_user import CreateUser
from icon_zoom.actions.create_user.schema import Input
import json
import logging
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    STUB_CONNECTION,
    STUB_CREATE_USER,
    mock_request_201,
    mock_request_400,
    mock_request_404,
    mock_request_409,
    mock_request_429,
    mocked_request,
)


class TestCreateUser(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = CreateUser()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = STUB_CREATE_USER

    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_create_user_success(self, mock_get):
        response = self.action.run(self.params)
        expected_response = {}

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (
                mock_request_409,
                "User already exists, try again.",
            ),
            (mock_request_429, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    # TODO - For 409, compare it to the something in the return
    # TODO - For 429, we will have to check headers and see if whatever exists
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
