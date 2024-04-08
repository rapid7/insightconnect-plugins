import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_netskope.actions.get_single_user_confidence_index import GetSingleUserConfidenceIndex
from icon_netskope.actions.get_single_user_confidence_index.schema import Input
from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    mock_request_200_api_v2,
    mock_request_400_api_v2,
    mock_request_401_api_v2,
    mock_request_403_api_v2,
    mock_request_500_api_v2,
    mocked_request,
)


class TestGetSingleUserConfidenceIndex(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetSingleUserConfidenceIndex()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            Input.USERNAME: "ExampleUser",
            Input.FROMTIME: 1,
        }

    @patch("requests.request", side_effect=mock_request_200_api_v2)
    def test_get_single_user_confidence_index_ok(self, mock_request: MagicMock) -> None:
        response = self.action.run(self.params)
        expected_response = {"userId": "ExampleUser", "confidences": [{"start": 0, "confidenceScore": 0}]}
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
    def test_get_single_user_confidence_index_bad(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
