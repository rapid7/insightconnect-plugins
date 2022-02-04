import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_opsgenie.actions.close_alert import CloseAlert
from icon_opsgenie.actions.close_alert.schema import Output
from icon_opsgenie.connection.connection import Connection
from icon_opsgenie.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    STUB_ALERT_ID,
    mock_request_202,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestCloseAlert(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.API_KEY: {"secretKey": "1234567e-123c-123c-123c-1234567e9xAd"}})

        self.action = CloseAlert()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            "identifier": STUB_ALERT_ID,
            "user": "ExampleUser",
            "source": "ExampleSource",
            "note": "ExampleNote",
        }

    @mock.patch("requests.request", side_effect=mock_request_202)
    def test_close_alert_when_status_ok(self, mock_post):
        response = self.action.run(self.params)
        expected_response = {
            Output.RESULT: "Request will be processed",
            Output.REQUESTID: "43a29c5c-3dbf-4fa4-9c26-f4f71023e120",
            Output.ELAPSED_TIME: 0.107,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.NOT_FOUND),
            (mock_request_500, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_close_alert_when_status_error(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )

    def test_close_alert_user_over_100_characters(self):
        mocked_request(mock_request_500)
        payload = {**self.params, "user": "LongUsername" * 101}

        with self.assertRaises(PluginException) as context:
            self.action.run(payload)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.UNKNOWN],
        )
        self.assertEqual(
            context.exception.data,
            'Limit of maximum input characters for parameter "user" has been exceeded (maximum characters 100)',
        )
