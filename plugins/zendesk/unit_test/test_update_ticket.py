from unittest import TestCase
from komand_zendesk.actions.update_ticket import UpdateTicket
from komand_zendesk.actions.update_ticket.schema import Input, Output
from unittest.mock import patch

from util import Util


class TestUpdateTicket(TestCase):
    @classmethod
    @patch("zenpy.TicketApi.update", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(UpdateTicket())

    @patch("zenpy.TicketApi.update", side_effect=Util.mocked_requests)
    @patch("zenpy.TicketApi.__call__", side_effect=Util.mocked_requests)
    def test_update(self, mock_request, mocked_request2):
        # happy path test - closing a ticket
        actual = self.action.run({Input.TICKET_ID: 1, Input.STATUS: "Closed"})
        expected_ticket_status = "Closed"
        self.assertEqual(actual.get(Output.TICKET).get(Input.STATUS), expected_ticket_status)
