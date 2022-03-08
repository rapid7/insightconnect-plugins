import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_netskope.actions.get_all_url_list import GetAllUrlList
from icon_netskope.actions.get_all_url_list.schema import Output
from icon_netskope.connection.connection import Connection
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200_api_v2,
    mock_request_400_api_v2,
    mock_request_401_api_v2,
    mock_request_403_api_v2,
    mock_request_500_api_v2,
    mocked_request,
)

STUB_EXPECTED_RESPONSE_APPLIED = {
    "urllists": [
        {
            "id": 1,
            "name": "ExampleName",
            "data": {
                "urls": ["https://example.com", "https://example.com"],
                "type": "exact",
                "json_version": 2,
            },
            "modify_by": "Netskope REST API",
            "modify_time": "2022-01-03T00:00:00.000Z",
            "modify_type": "Created",
            "pending": 0,
        }
    ]
}

STUB_EXPECTED_RESPONSE_APPLIED_MANY = {
    "urllists": [
        {
            "id": 1,
            "name": "ExampleName",
            "data": {
                "urls": ["https://example.com", "https://example.com"],
                "type": "exact",
                "json_version": 2,
            },
            "modify_by": "Netskope REST API",
            "modify_time": "2022-01-03T00:00:00.000Z",
            "modify_type": "Created",
            "pending": 0,
        },
        {
            "id": 2,
            "name": "ExampleName2",
            "data": {
                "urls": ["https://example.com", "https://example.com"],
                "type": "exact",
                "json_version": 2,
            },
            "modify_by": "Netskope REST API",
            "modify_time": "2022-01-03T00:00:00.000Z",
            "modify_type": "Created",
            "pending": 0,
        },
        {
            "id": 3,
            "name": "ExampleName3",
            "data": {
                "urls": ["https://example.com", "https://example.com"],
                "type": "exact",
                "json_version": 2,
            },
            "modify_by": "Netskope REST API",
            "modify_time": "2022-01-03T00:00:00.000Z",
            "modify_type": "Created",
            "pending": 0,
        },
    ]
}

STUB_EXPECTED_RESPONSE_PENDING = {
    "urllists": [
        {
            "id": 1,
            "name": "ExampleName",
            "data": {
                "urls": ["https://example.com", "https://example.com"],
                "type": "exact",
                "json_version": 2,
            },
            "modify_by": "Netskope REST API",
            "modify_time": "2022-01-03T00:00:00.000Z",
            "modify_type": "Created",
            "pending": 1,
        }
    ]
}


class TestGetAllUrlList(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetAllUrlList()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

    @parameterized.expand(
        [
            ("", STUB_EXPECTED_RESPONSE_APPLIED),
            ("applied", STUB_EXPECTED_RESPONSE_APPLIED),
            ("pending", STUB_EXPECTED_RESPONSE_PENDING),
        ],
    )
    def test_get_all_url_list_input_params_ok(self, input_pending, expected_response):
        mocked_request(mock_request_200_api_v2)
        response = self.action.run({"status": input_pending})
        self.assertEqual(response, expected_response)

    @mock.patch("icon_netskope.util.api.ApiClient.get_all_url_list", return_value=[])
    def test_get_all_url_list_input_params_ok_no_output(self, mock_api_function):
        response = self.action.run()
        expected_response = {Output.URLLISTS: []}
        self.assertEqual(response, expected_response)

    @mock.patch(
        "icon_netskope.util.api.ApiClient.get_all_url_list",
        return_value=STUB_EXPECTED_RESPONSE_APPLIED_MANY.get("urllists", []),
    )
    def test_get_all_url_list_input_params_ok_many_items(self, mock_api_function):
        response = self.action.run()
        expected_response = STUB_EXPECTED_RESPONSE_APPLIED_MANY
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_get_all_url_list_bad(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
