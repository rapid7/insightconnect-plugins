import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_cisco_umbrella_enforcement.connection.connection import Connection
from komand_cisco_umbrella_enforcement.actions.add_event import AddEvent
from parameterized import parameterized
import logging
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_202,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestAddEvent(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = AddEvent()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    @mock.patch("requests.request", side_effect=mock_request_202)
    def test_add_event(self, mock_post):
        response = self.action.run(events)
        expected_response = []

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, "Invalid request."),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(domain_id)
        self.assertEqual(context.exception.cause, exception)
