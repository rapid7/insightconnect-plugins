import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase, mock

from icon_netskope.actions.create_new_url_list import CreateNewUrlList
from icon_netskope.actions.create_new_url_list.schema import Input
from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_201_api_v2,
    mock_request_400_api_v2,
    mock_request_401_api_v2,
    mock_request_403_api_v2,
    mock_request_404_api_v2,
    mock_request_429_api_v2,
    mock_request_500_api_v2,
    mock_request_bad_json_response_api_v2,
    mocked_request,
)

STUB_GET_URL_LIST_BY_ID = {
    "id": 0,
    "name": "ExampleName",
    "data": {"urls": ["https://example.com", "https://example.com"], "type": "exact"},
    "modify_type": "Created",
    "modify_by": "Netskope API",
    "modify_time": "1997-01-01 00:00:00",
    "pending": 0,
}


class TestCreateNewUrlList(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = CreateNewUrlList()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            Input.NAME: "ExampleName",
            Input.TYPE: "exact",
            Input.URLS: ["https://example.com", "https://example.com"],
        }

    @mock.patch("icon_netskope.util.api.ApiClient.get_url_list_by_id", return_value=STUB_GET_URL_LIST_BY_ID)
    def test_create_new_url_list_ok(self, mock_post):
        mocked_request(mock_request_201_api_v2)
        response = self.action.run(self.params)
        expected_response = {
            "id": 0,
            "name": "ExampleName",
            "data": {"urls": ["https://example.com", "https://example.com"], "type": "exact"},
            "modify_type": "Created",
            "modify_by": "Netskope API",
            "modify_time": "1997-01-01 00:00:00",
            "pending": 0,
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_429_api_v2, PluginException.Preset.RATE_LIMIT),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
            (mock_request_bad_json_response_api_v2, PluginException.Preset.INVALID_JSON),
        ],
    )
    def test_create_new_url_list_bad(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
