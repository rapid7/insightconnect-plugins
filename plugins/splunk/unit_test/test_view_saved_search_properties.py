import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.view_saved_search_properties import ViewSavedSearchProperties
from icon_splunk.actions.view_saved_search_properties.schema import Input, Output
from jsonschema import validate

from mock import EXAMPLE_EXCEPTION_MESSAGE, EXAMPLE_JOB_ID, connect
from utils import default_connector

STUB_PAYLOAD = {Input.SAVED_SEARCH_NAME: "ExampleSavedSearchName"}


class TestViewSavedSearchProperties(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(ViewSavedSearchProperties())

    def test_view_saved_search_properties(self) -> None:
        response = self.action.run(STUB_PAYLOAD)
        expected = {Output.PROPERTIES: {}}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    def test_view_saved_search_properties_error(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.SAVED_SEARCH_NAME: "error"})
        self.assertEqual(context.exception.cause, "Saved search error was not found!")
        self.assertEqual(context.exception.assistance, "Ensure the saved search exists.")
        self.assertEqual(context.exception.data, f"'{EXAMPLE_EXCEPTION_MESSAGE}'")
