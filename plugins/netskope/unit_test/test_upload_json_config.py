import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_netskope.actions.upload_json_config import UploadJsonConfig
from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    mock_request_201_api_v2,
    mock_request_400_api_v2,
    mock_request_401_api_v2,
    mock_request_403_api_v2,
    mock_request_500_api_v2,
    mocked_request,
)


class TestUploadJsonConfig(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = UploadJsonConfig()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            "urllist": {
                "filename": "test.json",
                "content": "eyAiaXRlbXMiOiBbIHsgIm5hbWUiOiAidGVzdF9zdHJpbmdfMyIsICJkYXRhIjogeyAidXJscyI6IFsid3d3LmV4YW1wbGUuY29tIl0sICJ0eXBlIjogImV4YWN0IiB9IH0gXSB9",
            }
        }

    @patch("requests.request", side_effect=mock_request_201_api_v2)
    def test_upload_json_config_ok(self, mock_request: MagicMock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            "uploaded_urllist": [
                {
                    "id": 1,
                    "name": "ExampleName",
                    "data": {"urls": ["https://example.com", "https://example.com"], "type": "exact"},
                    "modify_by": "Netskope REST API",
                    "modify_time": "1997-01-01 00:00:00",
                    "modify_type": "Created",
                    "pending": 0,
                }
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected_response)
        mock_request.assert_called()

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_upload_json_config_bad(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
