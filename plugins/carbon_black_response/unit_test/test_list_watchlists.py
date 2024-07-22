import sys
import os

from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
from unittest import mock
from unittest import TestCase
from carbon_black_response.icon_carbon_black_response.actions.list_watchlists.schema import Input, ListWatchlistsOutput
from carbon_black_response.icon_carbon_black_response.actions.list_watchlists import ListWatchlists
from jsonschema import validate


class TestListWatchlists(TestCase):
    def setUp(self):
        self.action = ListWatchlists()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.carbon_black = self.mock_client

    @mock.patch("icon_carbon_black_response.connection.connection.Connection")
    def test_list_sensors_success(self, mock_connection):
        mock_connection.carbon_black = self.mock_client
        self.mock_client.get_object.return_value = [
            {
                "date_added": "2018-01-16 09:15:14.015605-08:00",
                "enabled": True,
                "group_id": -1,
                "id": "6",
                "index_type": "modules",
                "last_hit_count": 0,
                "name": "Cb Threat Reputation >= 50",
                "readonly": False,
                "search_query": "cb.urlver=1&q=alliance_score_srsthreat%3A%5B50%20TO%20%2A%5D",
                "search_timestamp": "1970-01-01T00:00:00.000Z",
                "total_hits": "0",
                "total_tags": "0",
            }
        ]
        response = self.action.run()
        expected_response = {
            "watchlists": [
                {
                    "date_added": "2018-01-16 09:15:14.015605-08:00",
                    "enabled": True,
                    "group_id": -1,
                    "id": "6",
                    "index_type": "modules",
                    "last_hit_count": 0,
                    "name": "Cb Threat Reputation >= 50",
                    "readonly": False,
                    "search_query": "cb.urlver=1&q=alliance_score_srsthreat%3A%5B50%20TO%20%2A%5D",
                    "search_timestamp": "1970-01-01T00:00:00.000Z",
                    "total_hits": "0",
                    "total_tags": "0",
                }
            ]
        }
        self.assertEqual(expected_response, response)
        validate(response, ListWatchlistsOutput.schema)
