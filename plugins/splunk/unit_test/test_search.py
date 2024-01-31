import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.search import Search
from icon_splunk.actions.search.schema import Input, Output
from jsonschema import validate

from mock import connect
from utils import default_connector

STUB_PAYLOAD = {Input.QUERY: "search *", Input.COUNT: 1}


class TestSearch(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(Search())

    def test_search(self) -> None:
        response = self.action.run(STUB_PAYLOAD)
        expected = {
            Output.RESULT: {
                "results": [
                    {"_time": "2024-01-30T12:46:00", "event": "example event 1"},
                    {"_time": "2024-01-30T12:47:00", "event": "example event 2"},
                    {"_time": "2024-01-30T12:48:00", "event": "example event 3"},
                ],
                "preview": False,
            },
            Output.COUNT: 3,
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
