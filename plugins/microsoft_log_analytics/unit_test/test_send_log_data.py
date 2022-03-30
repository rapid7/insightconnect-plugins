import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.actions.send_log_data import SendLogData
from icon_microsoft_log_analytics.actions.send_log_data.schema import Input, Output

from icon_microsoft_log_analytics.util.tools import Message
from unit_test.mock import (
    mock_request_200,
    mock_request_404,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mocked_request,
    STUB_WORKSPACE_ID,
    STUB_SHARED_KEY,
    STUB_CONNECTION,
    mock_request_400,
)

STUB_RFC1123_DATE = "Thu, 01 Dec 1994 16:00:00 GMT"

STUB_JSON_BODY = [{"key1": "key1"}]


class TestSendLogData(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = SendLogData()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.LOG_TYPE: "Test",
            Input.LOG_DATA: [{"key1": "test"}],
            Input.RESOURCE_GROUP_NAME: "exampleresourcegroupname",
            Input.SUBSCRIPTION_ID: "1234",
            Input.WORKSPACE_NAME: "ExampleWorkspace",
        }

    def test_send_log_data_ok(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {
            Output.MESSAGE: "Log data has been added",
            Output.LOG_DATA: self.payload.get(Input.LOG_DATA),
        }
        self.assertEqual(expected_response, response)

    def test_send_log_data_generate_signature(self):
        response = self.connection.client._generate_signature(
            STUB_WORKSPACE_ID, STUB_SHARED_KEY, STUB_RFC1123_DATE, STUB_JSON_BODY, "POST", "application/json"
        )
        expected_response = "SharedKey 12345:MnKflSkz0C1VUMYJtenLGX7Ila2gHVRxLTubiK058bI="
        self.assertEqual(expected_response, response)

    def test_send_log_data_generate_signature_wrong_json_input(self):
        with self.assertRaises(PluginException) as context:
            self.connection.client._generate_signature(
                STUB_WORKSPACE_ID, STUB_SHARED_KEY, STUB_RFC1123_DATE, {"WRONG JSON BODY"}, "POST", "application/json"
            )
        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.INVALID_JSON])

    @parameterized.expand(
        [
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
        ],
    )
    @mock.patch("icon_microsoft_log_analytics.util.tools.backoff_function", return_value=0)
    def test_send_log_data_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
