import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.delete_saved_search import DeleteSavedSearch
from jsonschema import validate
from parameterized import parameterized

from mock import connect
from utils import default_connector

STUB_SAVED_SEARCH_NAME = "ExampleSavedSearchName"


class TestDeleteSavedSearch(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(DeleteSavedSearch())

    @parameterized.expand(
        [
            ({"saved_search_name": STUB_SAVED_SEARCH_NAME}, {"success": True}),
            ({"saved_search_name": ""}, {"success": False}),
        ]
    )
    def test_delete_saved_search(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
