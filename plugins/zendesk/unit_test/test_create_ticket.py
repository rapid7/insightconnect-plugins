from unittest import TestCase
from komand_zendesk.actions.create_ticket import CreateTicket
from komand_zendesk.actions.create_ticket.schema import Input, Output
from unittest.mock import patch

from util import Util


class TestCreate(TestCase):
    @classmethod
    @patch("zenpy.TicketApi.create", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(CreateTicket())

    @patch("zenpy.TicketApi.create", side_effect=Util.mocked_requests)
    def test_create(self, mock_request):
        # happy path test
        actual = self.action.run({Input.DESCRIPTION: "CreateTicket"})
        expected_ticket_id = 5
        self.assertEqual(actual.get("id"), expected_ticket_id)
