import os
import sys
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_splunk.actions.insert import Insert
from icon_splunk.actions.insert.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import connect
from utils import default_connector

STUB_PAYLOAD = {
    Input.INDEX: "ExampleIndexName",
    Input.EVENT: "ExampleEventName",
    Input.HOST: "ExampleHost",
    Input.SOURCE: "ExampleSource",
    Input.SOURCE_TYPE: "ExampleSourceType",
}


class TestInsert(TestCase):
    @patch("splunklib.client.connect", side_effect=connect)
    def setUp(self, mock_client: MagicMock) -> None:
        self.action = default_connector(Insert())

    @parameterized.expand([({},), ({**STUB_PAYLOAD, Input.HOST: "error"},)])
    def test_insert(self, input_data: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
