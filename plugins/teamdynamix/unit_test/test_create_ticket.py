"""Unit tests for the Create Ticket action."""

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock
from icon_teamdynamix.actions.create_ticket import CreateTicket
from icon_teamdynamix.actions.create_ticket.schema import Input, Output
from icon_teamdynamix.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
import logging


class TestCreateTicket(TestCase):
    def setUp(self):
        self.action = CreateTicket()
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test")

        self.mock_client = MagicMock()
        self.mock_client.app_id = 42
        self.mock_client.base_url = "https://example.teamdynamix.com"
        self.connection.client = self.mock_client
        self.action.connection = self.connection

    def test_create_ticket_success(self):
        self.mock_client.create_ticket.return_value = {
            "ID": 12345,
            "Title": "Test Ticket",
            "StatusName": "New",
        }

        params = {
            Input.TITLE: "Test Ticket",
            Input.TYPE_ID: 123,
            Input.ACCOUNT_ID: 789,
            Input.STATUS_ID: 602,
            Input.PRIORITY_ID: 20,
            Input.REQUESTOR_EMAIL: "user@example.com",
            Input.DESCRIPTION: "Test description",
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        self.assertEqual(result[Output.TICKET_ID], 12345)
        self.assertIn("12345", result[Output.TICKET_URL])

        call_payload = self.mock_client.create_ticket.call_args[0][0]
        self.assertEqual(call_payload["TypeID"], 123)
        self.assertEqual(call_payload["Title"], "Test Ticket")
        self.assertEqual(call_payload["AccountID"], 789)
        self.assertEqual(call_payload["StatusID"], 602)
        self.assertEqual(call_payload["PriorityID"], 20)
        self.assertEqual(call_payload["RequestorEmail"], "user@example.com")
        self.assertEqual(call_payload["Description"], "Test description")

    def test_create_ticket_with_all_optional_fields(self):
        self.mock_client.create_ticket.return_value = {"ID": 99999}

        params = {
            Input.TITLE: "Full Ticket",
            Input.TYPE_ID: 100,
            Input.ACCOUNT_ID: 789,
            Input.STATUS_ID: 602,
            Input.PRIORITY_ID: 20,
            Input.REQUESTOR_EMAIL: "user@example.com",
            Input.DESCRIPTION: "Full description",
            Input.FORM_ID: 456,
            Input.RESPONSIBLE_GROUP_ID: 50,
            Input.ADDITIONAL_FIELDS: {"CustomField": "value"},
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        self.assertEqual(result[Output.TICKET_ID], 99999)

        call_payload = self.mock_client.create_ticket.call_args[0][0]
        self.assertEqual(call_payload["FormID"], 456)
        self.assertEqual(call_payload["ResponsibleGroupID"], 50)
        self.assertEqual(call_payload["CustomField"], "value")

    def test_create_ticket_no_id_returned(self):
        self.mock_client.create_ticket.return_value = {"Title": "Oops"}

        params = {
            Input.TITLE: "Bad Ticket",
            Input.TYPE_ID: 123,
            Input.ACCOUNT_ID: 789,
            Input.STATUS_ID: 602,
            Input.PRIORITY_ID: 20,
            Input.REQUESTOR_EMAIL: "user@example.com",
        }

        with self.assertRaises(PluginException):
            self.action.run(params)

    def test_create_ticket_minimal_required_fields(self):
        self.mock_client.create_ticket.return_value = {"ID": 1}

        params = {
            Input.TITLE: "Minimal",
            Input.TYPE_ID: 1,
            Input.ACCOUNT_ID: 100,
            Input.STATUS_ID: 500,
            Input.PRIORITY_ID: 10,
            Input.REQUESTOR_EMAIL: "min@example.com",
        }

        result = self.action.run(params)

        self.assertTrue(result[Output.SUCCESS])
        self.assertEqual(result[Output.TICKET_ID], 1)

        call_payload = self.mock_client.create_ticket.call_args[0][0]
        self.assertNotIn("FormID", call_payload)
        self.assertNotIn("ResponsibleGroupID", call_payload)

    def test_create_ticket_url_format(self):
        self.mock_client.create_ticket.return_value = {"ID": 555}

        params = {
            Input.TITLE: "URL Test",
            Input.TYPE_ID: 1,
            Input.ACCOUNT_ID: 100,
            Input.STATUS_ID: 500,
            Input.PRIORITY_ID: 10,
            Input.REQUESTOR_EMAIL: "test@example.com",
        }

        result = self.action.run(params)

        expected_url = "https://example.teamdynamix.com/TDClient/42/Requests/TicketDet?TicketID=555"
        self.assertEqual(result[Output.TICKET_URL], expected_url)
