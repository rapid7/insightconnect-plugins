import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_netskope.actions.delete_url_list_by_id import DeleteUrlListById
from icon_netskope.actions.delete_url_list_by_id.schema import Input
from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    STUB_ID,
    mock_request_200_api_v2,
    mock_request_400_api_v2,
    mock_request_401_api_v2,
    mock_request_403_api_v2,
    mock_request_404_api_v2,
    mock_request_500_api_v2,
    mocked_request,
)


class TestDeleteUrlListById(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DeleteUrlListById()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {Input.ID: STUB_ID}

    @patch("requests.request", side_effect=mock_request_200_api_v2)
    def test_delete_url_list_by_id_ok(self, mock_requests: MagicMock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            "id": 1,
            "name": "ExampleName",
            "data": {"urls": ["https://example.com", "https://example.com"], "type": "exact"},
            "modify_by": "Netskope REST API",
            "modify_time": "1997-01-01 00:00:00",
            "modify_type": "Created",
            "pending": 0,
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected_response)
        mock_requests.assert_called()

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
        ],
    )
    @patch("icon_netskope.util.utils.backoff_function", return_value=0)
    def test_delete_url_list_by_id_bad(
        self, mock_request: Callable, exception: str, mock_backoff_function: MagicMock
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
        mock_backoff_function.assert_called()
