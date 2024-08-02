import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.search_events.action import SearchEvents


class TestSearchEvents(unittest.TestCase):
    def setUp(self):
        self.action = SearchEvents()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "threat_level": "Medium",
            "published": "True",
            "analysis": "Ongoing",
            "tag": "test-tag",
            "date_from": "2020-01-01",
            "date_until": "2020-12-31",
            "organization": "Test Org",
            "event": "1",
            "values": "",
            "type_attribute": "",
            "category": "",
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_search_events_success(self, mock_connection):
        mock_search_index_response = [{"id": "1"}]
        mock_search_response = {"response": [{"Event": {"id": "1"}}]}
        mock_connection.client = self.mock_client
        self.mock_client.search_index.return_value = mock_search_index_response
        self.mock_client.search.return_value = mock_search_response

        result = self.action.run(self.params)
        self.assertEqual(result, {"event_list": ["1"]})

    @patch("komand_misp.connection.connection.Connection")
    def test_search_events_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.search_index.side_effect = PluginException(cause="Test exception for search index")

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue("Test exception for search index" in str(context.exception))
