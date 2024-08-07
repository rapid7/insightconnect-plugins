import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_attribute.action import AddAttribute
from komand_misp.actions.add_attribute.schema import AddAttributeInput, AddAttributeOutput
from jsonschema import validate


class TestAddAttribute(unittest.TestCase):
    def setUp(self):
        self.action = AddAttribute()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "event": "1",
            "type_value": "ip-dst",
            "category": "Network activity",
            "value": "8.8.8.8",
            "comment": "Test comment",
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_add_attribute_success(self, mock_connection):
        mock_response = {"Attribute": {"type_value": "ip-dst", "value": "8.8.8.8"}}
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"id": "1", "org_id": "1"}}
        self.mock_client.add_attribute.return_value = mock_response

        validate(self.params, AddAttributeInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"attribute": mock_response.get("Attribute")})
        validate(result, AddAttributeOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_add_attribute_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"id": "1"}}
        self.mock_client.add_attribute.return_value = {}

        validate(self.params, AddAttributeInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(self.params)
