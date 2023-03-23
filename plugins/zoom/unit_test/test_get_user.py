import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from unittest import TestCase, mock
from icon_zoom.connection.connection import Connection
from icon_zoom.actions.get_user import GetUser
from icon_zoom.actions.get_user.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
import logging

from unit_test.mock import (
    STUB_CONNECTION,
    STUB_USER_ID,
    mock_request_201,
    mock_request_204,
    mock_request_400,
    mock_request_404,
    mock_request_409,
    mock_request_429,
    mocked_request,

)


class TestDGet(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetUser()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {Input.USER_ID: STUB_USER_ID}

    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_get_user_success(self, mock_get):
        response = self.action.run(self.params)
        expected_response = {}

        self.assertEqual(response, expected_response)
