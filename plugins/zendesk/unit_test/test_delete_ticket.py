import sys

sys.path.append("../")

from unittest import TestCase
from icon_zendesk.actions.delete_ticket import DeleteTicket
from icon_zendesk.actions.delete_ticket.schema import Input, Output
from unittest.mock import patch, Mock

from util import Util


class TestDeleteTicket(TestCase):
    @classmethod
    @patch("zenpy.TicketApi.delete", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(DeleteTicket())

    @patch("zenpy.TicketApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.TicketApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_ticket(self, mock_request: Mock, mock_second: Mock) -> None:
        # happy path test- Note as of now- API just returns 204 and no actual response on success
        actual = self.action.run({Input.TICKET_ID: 0})
        self.assertEqual(actual.get(Output.STATUS), True)

    @patch("zenpy.TicketApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.TicketApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_ticket_fail(self, mock_request: Mock, mock_second: Mock) -> None:
        # Here -1 is showing a ticket id that doesn't exist. We don't expect an exception just a fail
        actual = self.action.run({Input.TICKET_ID: -1})
        self.assertEqual(actual.get(Output.STATUS), False)
