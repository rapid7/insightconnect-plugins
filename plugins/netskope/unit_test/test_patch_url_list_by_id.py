import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_netskope.actions.patch_url_list_by_id import PatchUrlListById
from icon_netskope.actions.patch_url_list_by_id.schema import Input
from icon_netskope.connection.connection import Connection
from unit_test.mock import (
    STUB_ACTION,
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


class TestPatchUrlListById(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = PatchUrlListById()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {
            Input.ID: STUB_ID,
            Input.ACTION: STUB_ACTION,
            Input.NAME: "ExampleName",
            Input.TYPE: "exact",
            Input.URLS: ["https://example.com", "https://example.com"],
        }

    def test_patch_url_list_by_id_ok(self):
        mocked_request(mock_request_200_api_v2)
        response = self.action.run(self.params)
        expected_response = {
            "id": 1,
            "name": "ExampleName",
            "data": {"urls": ["https://example.com", "https://example.com"], "type": "exact", "json_version": 2},
            "modify_by": "Netskope REST API",
            "modify_time": "1997-01-01 00:00:00",
            "modify_type": "Created",
            "pending": 0,
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_patch_url_list_by_id(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
