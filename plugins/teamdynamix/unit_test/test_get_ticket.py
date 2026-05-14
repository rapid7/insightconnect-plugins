"""Unit tests for the Get Ticket action."""

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock
from icon_teamdynamix.actions.get_ticket import GetTicket
from icon_teamdynamix.actions.get_ticket.schema import Input, Output
from icon_teamdynamix.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
import logging


class TestGetTicket(TestCase):
    def setUp(self):
        self.action = GetTicket()
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test")

        self.mock_client = MagicMock()
        self.mock_client.app_id = 42
        self.mock_client.base_url = "https://example.teamdynamix.com"
        self.connection.client = self.mock_client
        self.action.connection = self.connection

    def test_get_ticket_success(self):
        self.mock_client.get_ticket.return_value = {
            "ID": 12345,
            "Title": "Test Ticket",
            "StatusName": "In Progress",
            "Description": "Some description",
        }

        params = {Input.TICKET_ID: 12345}
        result = self.action.run(params)

        self.assertEqual(result[Output.TICKET_ID], 12345)
        self.assertEqual(result[Output.TITLE], "Test Ticket")
        self.assertEqual(result[Output.STATUS], "In Progress")
        self.assertIsInstance(result[Output.TICKET], dict)
        self.mock_client.get_ticket.assert_called_once_with(12345)

    def test_get_ticket_not_found(self):
        self.mock_client.get_ticket.return_value = {}

        params = {Input.TICKET_ID: 99999}

        with self.assertRaises(PluginException):
            self.action.run(params)

    def test_get_ticket_missing_optional_fields(self):
        self.mock_client.get_ticket.return_value = {
            "ID": 100,
        }

        params = {Input.TICKET_ID: 100}
        result = self.action.run(params)

        self.assertEqual(result[Output.TICKET_ID], 100)
        # clean() removes empty strings, so title and status won't be in output
        self.assertNotIn(Output.TITLE, result)
        self.assertNotIn(Output.STATUS, result)

    def test_get_ticket_cleans_none_values(self):
        self.mock_client.get_ticket.return_value = {
            "ID": 200,
            "Title": "Test",
            "StatusName": "Open",
            "Description": None,
            "RequestorUid": None,
            "Tags": None,
        }

        params = {Input.TICKET_ID: 200}
        result = self.action.run(params)

        ticket = result[Output.TICKET]
        self.assertNotIn("Description", ticket)
        self.assertNotIn("RequestorUid", ticket)
        self.assertNotIn("Tags", ticket)
        self.assertEqual(ticket["Title"], "Test")
