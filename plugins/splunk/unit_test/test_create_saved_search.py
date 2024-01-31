import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.create_saved_search import CreateSavedSearch
from icon_splunk.actions.create_saved_search.schema import Input, Output
from jsonschema import validate

from mock import EXAMPLE_EXCEPTION_MESSAGE, connect
from utils import default_connector

STUB_SAVED_SEARCH_NAME = "ExampleSavedSearchName"
STUB_QUERY = "search *"


class TestCreateSavedSearch(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(CreateSavedSearch())

    def test_create_saved_search(self) -> None:
        response = self.action.run(
            {Input.SAVED_SEARCH_NAME: STUB_SAVED_SEARCH_NAME, Input.QUERY: STUB_QUERY, Input.PROPERTIES: {}}
        )
        expected = {Output.SAVED_SEARCH: {"content": {}, "name": STUB_SAVED_SEARCH_NAME}}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    def test_create_saved_search_error(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.PROPERTIES: {}})
        self.assertEqual(context.exception.cause, "Unable to create saved search!")
        self.assertEqual(context.exception.assistance, "Ensure your properties and query are valid.")
        self.assertEqual(context.exception.data, EXAMPLE_EXCEPTION_MESSAGE)
