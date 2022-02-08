import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase

from icon_opsgenie.actions.create_alert import CreateAlert
from icon_opsgenie.actions.create_alert.schema import Output
from icon_opsgenie.connection.connection import Connection
from icon_opsgenie.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import mock_request_202, mock_request_403, mock_request_404, mock_request_500, mocked_request


class TestCreateAlert(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.API_KEY: {"secretKey": "1234567e-123c-123c-123c-1234567e9xAd"}})

        self.action = CreateAlert()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            "message": "An example message",
            "user": "ExampleUser",
            "source": "ExampleSource",
            "note": "ExampleNote",
        }

    def test_create_alert_when_status_ok(self):
        mocked_request(mock_request_202)
        response = self.action.run(self.params)
        expected_response = {
            Output.RESULT: "Request will be processed",
            Output.REQUESTID: "43a29c5c-3dbf-4fa4-9c26-f4f71023e120",
            Output.ELAPSED_TIME: 0.302,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.NOT_FOUND),
            (mock_request_500, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_create_alert_when_status_error(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )

    def test_create_alert_no_message(self):
        mocked_request(mock_request_500)

        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.UNKNOWN],
        )
        self.assertEqual(context.exception.data, "No required parameter has been entered")

    def test_create_alert_message_over_130_characters(self):
        mocked_request(mock_request_500)
        payload = {"message": "LongMessage" * 131}

        with self.assertRaises(PluginException) as context:
            self.action.run(payload)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.UNKNOWN],
        )
        self.assertEqual(
            context.exception.data,
            'Limit of maximum input characters for parameter "message" has been exceeded (maximum characters 130)',
        )

    def test_create_alert_user_over_100_characters(self):
        mocked_request(mock_request_500)
        payload = {"message": "An example message", "user": "LongUsername" * 101}

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

    def test_create_alert_actions_over_10_elements(self):
        mocked_request(mock_request_500)
        payload = {**self.params, "actions": [str(element) for element in range(1, 12)]}

        with self.assertRaises(PluginException) as context:
            self.action.run(payload)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.UNKNOWN],
        )
        self.assertEqual(
            context.exception.data,
            'Limit of maximum input characters for parameter "actions" has been exceeded (maximum elements 10)',
        )

    def test_create_alert_actions_over_50_characters(self):
        mocked_request(mock_request_500)
        payload = {**self.params, "actions": ["First", "LongActionName" * 51]}

        with self.assertRaises(PluginException) as context:
            self.action.run(payload)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.UNKNOWN],
        )
        self.assertEqual(
            context.exception.data,
            'Limit of maximum input characters for parameter "actions" has been exceeded (maximum characters 50)',
        )
