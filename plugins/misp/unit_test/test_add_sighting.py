import sys
import os

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException


from unittest import TestCase
from unittest.mock import patch, MagicMock
from komand_misp.actions.add_sighting.action import AddSighting
from komand_misp.actions.add_sighting.schema import AddSightingInput, AddSightingOutput
from jsonschema import validate


class TestAddSighting(TestCase):
    def setUp(self):
        self.action = AddSighting()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sighting_min_inputs(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        params = {"attribute": 16, "type": "Sighting"}

        example_response = {
            "Sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "",
                "type": "0",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        excepted = {
            "sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "",
                "type": "0",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        self.mock_client.add_sighting.return_value = example_response

        validate(params, AddSightingInput.schema)
        result = self.action.run(params)
        self.assertEqual(result, excepted)
        validate(result, AddSightingOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sighting_min_inputs_expiration(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        params = {"attribute": 16, "type": "Expiration"}

        example_response = {
            "Sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "",
                "type": "2",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        excepted = {
            "sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "",
                "type": "2",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        self.mock_client.add_sighting.return_value = example_response

        validate(params, AddSightingInput.schema)
        result = self.action.run(params)
        self.assertEqual(result, excepted)
        validate(result, AddSightingOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sighting_all_inputs(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        params = {"attribute": 16, "type": "Sighting", "source": "test", "date": "2024-08-20", "Time": "15:00"}

        example_response = {
            "Sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "test",
                "type": "0",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        excepted = {
            "sighting": {
                "attribute_id": "16",
                "date_sighting": "1724238012",
                "event_id": "10",
                "id": "26",
                "org_id": "1",
                "source": "test",
                "type": "0",
                "uuid": "ee40bd90-9c42-466e-970c-4e9c9f583120",
            }
        }

        self.mock_client.add_sighting.return_value = example_response

        validate(params, AddSightingInput.schema)
        result = self.action.run(params)
        self.assertEqual(result, excepted)
        validate(result, AddSightingOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sighting_failure_not_added(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        params = {"attribute": 16, "type": "Expiration"}

        self.mock_client.add_sighting.return_value = {}
        validate(params, AddSightingInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(params)
        self.action.logger.error.assert_called()

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sighting_failure(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        params = {"attribute": 16, "type": "Expiration"}

        self.mock_client.add_sighting.side_effect = Exception("Test exception")
        validate(params, AddSightingInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(params)
        self.action.logger.error.assert_called()
