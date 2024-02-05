import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.get_saved_search_job_history import GetSavedSearchJobHistory
from icon_splunk.actions.get_saved_search_job_history.schema import Input, Output
from jsonschema import validate

from mock import EXAMPLE_EXCEPTION_MESSAGE, EXAMPLE_JOB_HISTORY, connect
from utils import default_connector

STUB_SAVED_SEARCH_NAME = "ExampleSavedSearchName"


class TestGetSavedSearchJobHistory(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(GetSavedSearchJobHistory())

    def test_get_saved_search_job_history(self) -> None:
        response = self.action.run({Input.SAVED_SEARCH_NAME: STUB_SAVED_SEARCH_NAME})
        expected = {Output.JOB_HISTORY: EXAMPLE_JOB_HISTORY}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    def test_get_saved_search_job_history_error(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.SAVED_SEARCH_NAME: "error"})
        self.assertEqual(context.exception.cause, "The specified saved search was not found.")
        self.assertEqual(context.exception.assistance, "Ensure the saved search 'error' exists.")
        self.assertEqual(context.exception.data, f"'{EXAMPLE_EXCEPTION_MESSAGE}'")
