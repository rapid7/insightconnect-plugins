"""Unit tests for the Update Ticket action."""

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock
from icon_teamdynamix.actions.update_ticket import UpdateTicket
from icon_teamdynamix.actions.update_ticket.schema import Input, Output
from icon_teamdynamix.connection.connection import Connection
import logging


class TestUpdateTicket(TestCase):
    def setUp(self):
        self.action = UpdateTicket()
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test")

        self.mock_client = MagicMock()
        self.mock_client.app_id = 42
        self.mock_client.base_url = "https://example.teamdynamix.com"
        self.connection.client = self.mock_client
        self.action.connection = self.connection

        self.existing_ticket = {
            "ID": 12345,
            "Title": "Original Title",
            "Description": "Original Description",
            "StatusID": 100,
            "PriorityID": 10,
        }

    def test_update_ticket_title(self):
        self.mock_client.get_ticket.return_value = self.existing_ticket
        self.mock_client.update_ticket.return_value = {"ID": 12345}

        params = {
            Input.TICKET_ID: 12345,
            Input.TITLE: "Updated Title",
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        update_payload = self.mock_client.update_ticket.call_args[0][1]
        self.assertEqual(update_payload["Title"], "Updated Title")
        self.assertEqual(update_payload["Description"], "Original Description")

    def test_update_ticket_status_and_priority(self):
        self.mock_client.get_ticket.return_value = self.existing_ticket
        self.mock_client.update_ticket.return_value = {"ID": 12345}

        params = {
            Input.TICKET_ID: 12345,
            Input.STATUS_ID: 602,
            Input.PRIORITY_ID: 30,
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        update_payload = self.mock_client.update_ticket.call_args[0][1]
        self.assertEqual(update_payload["StatusID"], 602)
        self.assertEqual(update_payload["PriorityID"], 30)

    def test_update_ticket_with_additional_fields(self):
        self.mock_client.get_ticket.return_value = self.existing_ticket
        self.mock_client.update_ticket.return_value = {"ID": 12345}

        params = {
            Input.TICKET_ID: 12345,
            Input.ADDITIONAL_FIELDS: {"CustomField": "CustomValue"},
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        update_payload = self.mock_client.update_ticket.call_args[0][1]
        self.assertEqual(update_payload["CustomField"], "CustomValue")

    def test_update_ticket_fetches_current_first(self):
        self.mock_client.get_ticket.return_value = self.existing_ticket
        self.mock_client.update_ticket.return_value = {"ID": 12345}

        params = {
            Input.TICKET_ID: 12345,
            Input.TITLE: "New Title",
        }

        self.action.run(params)

        self.mock_client.get_ticket.assert_called_once_with(12345)
        self.mock_client.update_ticket.assert_called_once()
        update_call_args = self.mock_client.update_ticket.call_args[0]
        self.assertEqual(update_call_args[0], 12345)
