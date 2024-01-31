import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.display_search_results import DisplaySearchResults
from icon_splunk.actions.display_search_results.schema import Input, Output
from jsonschema import validate

from mock import connect
from utils import default_connector

STUB_SAVED_SEARCH_NAME = "ExampleSavedSearchName"
STUB_READER_RESPONSE = [
    {
        "_raw": "2023-10-15 12:00:00, INFO - Application started",
        "host": "server-1",
        "source": "/var/log/application.log",
        "sourcetype": "test",
        "index": "main",
        "_time": "2023-10-15T12:00:00",
        "event": {"level": "INFO", "message": "Application started"},
    }
]


class TestDisplaySearchResults(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(DisplaySearchResults())

    @patch("splunklib.results.ResultsReader", return_value=STUB_READER_RESPONSE)
    def test_display_search_results(self, mock_reader: MagicMock) -> None:
        response = self.action.run({Input.JOB_ID: "12345", Input.TIMEOUT: 0})
        expected = {Output.SEARCH_RESULTS: STUB_READER_RESPONSE}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
        mock_reader.assert_called_once()

    def test_display_search_results_error(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.JOB_ID: "error"})
        self.assertEqual(context.exception.cause, "Unable to find job.")
        self.assertEqual(context.exception.assistance, "Ensure the provided job ID input is valid.")
        self.assertEqual(context.exception.data, "Job ID: error")
