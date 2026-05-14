"""Unit tests for the Search Tickets action."""

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock
from icon_teamdynamix.actions.search_tickets import SearchTickets
from icon_teamdynamix.actions.search_tickets.schema import Input, Output
from icon_teamdynamix.connection.connection import Connection
from icon_teamdynamix.util.constants import DEFAULT_MAX_RESULTS
import logging


class TestSearchTickets(TestCase):
    def setUp(self):
        self.action = SearchTickets()
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test")

        self.mock_client = MagicMock()
        self.mock_client.app_id = 42
        self.mock_client.base_url = "https://example.teamdynamix.com"
        self.connection.client = self.mock_client
        self.action.connection = self.connection

    def test_search_tickets_with_results(self):
        self.mock_client.search_tickets.return_value = [
            {"ID": 1, "Title": "Ticket One"},
            {"ID": 2, "Title": "Ticket Two"},
        ]

        params = {
            Input.SEARCH_TEXT: "CVE-2024",
            Input.MAX_RESULTS: 10,
        }

        result = self.action.run(params)

        self.assertEqual(result[Output.COUNT], 2)
        self.assertEqual(len(result[Output.TICKETS]), 2)
        self.mock_client.search_tickets.assert_called_once_with(
            {"MaxResults": 10, "SearchText": "CVE-2024"}
        )

    def test_search_tickets_empty_results(self):
        self.mock_client.search_tickets.return_value = []

        params = {Input.MAX_RESULTS: 25}

        result = self.action.run(params)

        self.assertEqual(result[Output.COUNT], 0)

    def test_search_tickets_with_status_filter(self):
        self.mock_client.search_tickets.return_value = [
            {"ID": 5, "Title": "Filtered Ticket"},
        ]

        params = {
            Input.STATUS_ID: 602,
            Input.MAX_RESULTS: 25,
        }

        result = self.action.run(params)

        self.assertEqual(result[Output.COUNT], 1)
        call_payload = self.mock_client.search_tickets.call_args[0][0]
        self.assertEqual(call_payload["StatusIDs"], [602])

    def test_search_tickets_default_max_results(self):
        self.mock_client.search_tickets.return_value = []

        params = {}

        self.action.run(params)

        call_payload = self.mock_client.search_tickets.call_args[0][0]
        self.assertEqual(call_payload["MaxResults"], DEFAULT_MAX_RESULTS)

    def test_search_tickets_cleans_none_values_in_results(self):
        self.mock_client.search_tickets.return_value = [
            {"ID": 1, "Title": "Ticket One", "Description": None, "Tags": None},
            {"ID": 2, "Title": "Ticket Two", "RequestorUid": None},
        ]

        params = {Input.MAX_RESULTS: 25}

        result = self.action.run(params)

        self.assertEqual(result[Output.COUNT], 2)
        self.assertNotIn("Description", result[Output.TICKETS][0])
        self.assertNotIn("Tags", result[Output.TICKETS][0])
        self.assertNotIn("RequestorUid", result[Output.TICKETS][1])
