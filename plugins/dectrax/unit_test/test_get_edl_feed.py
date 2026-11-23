import sys
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("./"))

from icon_dectrax.connection.connection import Connection
from icon_dectrax.actions.get_edl_feed import GetEdlFeed
from icon_dectrax.actions.get_edl_feed.schema import Output


class TestGetEdlFeed(TestCase):

    def setUp(self):
        self.connection = Connection()
        self.connection.logger = MagicMock()
        self.connection.connect({
            "url": "https://dectrax.internal",
            "api_key": {"secretKey": "test-key"},
            "ssl_verify": False,
        })
        self.action = GetEdlFeed()
        self.action.connection = self.connection
        self.action.logger = MagicMock()

    @patch("requests.get")
    def test_get_edl_feed(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "# DECTRAX Threat Intelligence Feed\n198.51.100.24\n203.0.113.88\n"
        mock_get.return_value = mock_response

        response = self.action.run({})
        self.assertTrue(response[Output.SUCCESS])
        self.assertIn("198.51.100.24", response[Output.FEED_CONTENT])
