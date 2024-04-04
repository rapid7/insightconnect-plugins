import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Callable
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_netskope.actions.update_file_hash_list import UpdateFileHashList
from icon_netskope.actions.update_file_hash_list.schema import Output
from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    mock_request_200_api_v1,
    mock_request_201_api_v1,
    mock_request_400_api_v1,
    mock_request_403_api_v1,
    mock_request_404_api_v1,
    mock_request_429_api_v1,
    mock_request_500_api_v1,
    mock_request_bad_json_response_api_v1,
    mocked_request,
)


class TestUpdateFileHashList(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = UpdateFileHashList()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

    @parameterized.expand(
        [
            (mock_request_200_api_v1,),
            (mock_request_201_api_v1,),
        ]
    )
    def test_update_file_hash_list_ok(self, mock_request: Callable) -> None:
        mocked_request(mock_request)
        data = {
            "name": "test",
            "list": [
                "e28eb9739b6e84d0f796e3acc0f5b71e",
                "e28eb9739b6e84d0f697e3acc0f5b71a",
                "e28eb9839b6e74d0f696e3acc0f6b710",
            ],
        }
        response = self.action.run(data)
        expected_response = {Output.STATUS: "success", Output.MESSAGE: "File Filter Profile updated successfully"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400_api_v1, PluginException.Preset.UNKNOWN),
            (mock_request_403_api_v1, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404_api_v1, PluginException.Preset.NOT_FOUND),
            (mock_request_429_api_v1, PluginException.Preset.RATE_LIMIT),
            (mock_request_500_api_v1, PluginException.Preset.UNKNOWN),
            (mock_request_bad_json_response_api_v1, PluginException.Preset.INVALID_JSON),
        ]
    )
    @patch("icon_netskope.util.utils.backoff_function", return_value=0)
    def test_update_file_hash_list_bad(
        self, mock_request: Callable, exception: str, mock_backoff_function: MagicMock
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run({"name": "test", "list": []})
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
        mock_backoff_function.assert_called()
