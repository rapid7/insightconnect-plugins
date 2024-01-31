import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.list_saved_searches import ListSavedSearches
from icon_splunk.actions.list_saved_searches.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import EXAMPLE_LIST_SAVED_SEARCHES, connect
from utils import default_connector

STUB_PAYLOAD = {}


class TestListSavedSearches(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(ListSavedSearches())

    def test_list_saved_searches(self) -> None:
        response = self.action.run({})
        expected = {Output.SAVED_SEARCHES: EXAMPLE_LIST_SAVED_SEARCHES}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
