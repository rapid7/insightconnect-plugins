import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_sightings.action import AddSightings


class TestAddSightings(unittest.TestCase):
    def setUp(self):
        self.action = AddSightings()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"sightings": ["sighting1", "sighting2"]}

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sightings_success(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.set_sightings.return_value = {"message": "2 sightings successfully added."}
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sightings_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.set_sightings.return_value = {"message": "Failed to add sightings."}
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})

    @patch("komand_misp.connection.connection.Connection")
    def test_add_sightings_exception(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.set_sightings.side_effect = Exception("Test exception")
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})
        self.action.logger.error.assert_called()
