import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_netskope.actions.apply_pending_url_list_changes import ApplyPendingUrlListChanges
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


class TestApplyPendingUrlListChanges(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = ApplyPendingUrlListChanges()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

    def test_apply_pending_url_list_changes_ok(self):
        mocked_request(mock_request_200_api_v2)
        response = self.action.run()
        expected_response = {
            "deployed_urllists": [
                {
                    "id": 1,
                    "name": "ExampleName",
                    "data": {
                        "urls": ["https://example.com", "https://example.com"],
                        "type": "exact",
                    },
                    "modify_by": "Netskope REST API",
                    "modify_time": "2022-01-03T00:00:00.000Z",
                    "modify_type": "Created",
                    "pending": 1,
                }
            ]
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400_api_v2, PluginException.Preset.NOT_FOUND),
            (mock_request_401_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_api_v2, PluginException.Preset.UNAUTHORIZED),
            (mock_request_500_api_v2, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_apply_pending_url_list_changes_bad(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
