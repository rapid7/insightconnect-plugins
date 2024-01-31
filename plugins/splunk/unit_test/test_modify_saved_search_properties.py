import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.modify_saved_search_properties import ModifySavedSearchProperties
from icon_splunk.actions.modify_saved_search_properties.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import EXAMPLE_LIST_SAVED_SEARCHES, connect
from utils import default_connector

STUB_PAYLOAD = {Input.SAVED_SEARCH_NAME: "ExampleSavedSearchName", Input.PROPERTIES: {}}


class TestModifySavedSearchProperties(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(ModifySavedSearchProperties())

    @parameterized.expand([(STUB_PAYLOAD, True), ({**STUB_PAYLOAD, Input.SAVED_SEARCH_NAME: "error"}, False)])
    def test_modify_saved_search_properties(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        expected = {Output.SUCCESS: expected}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
