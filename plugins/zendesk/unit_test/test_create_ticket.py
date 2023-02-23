import sys

sys.path.append("../")

from unittest import TestCase
from unittest.mock import Mock, patch

from icon_zendesk.actions.create_ticket import CreateTicket
from icon_zendesk.actions.create_ticket.schema import Input, Output
from icon_zendesk.util.messages import Messages

from util import Util

from insightconnect_plugin_runtime.exceptions import PluginException


class TestCreate(TestCase):
    @classmethod
    @patch("zenpy.TicketApi.create", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(CreateTicket())

    @patch("zenpy.TicketApi.create", side_effect=Util.mocked_requests)
    def test_create(self, mock_request: Mock) -> None:
        # happy path test
        response = self.action.run({Input.DESCRIPTION: "CreateTicket"})
        expected_ticket_id = 5
        self.assertEqual(response.get(Output.TICKET, {}).get("id"), expected_ticket_id)

    @patch("zenpy.TicketApi.create", side_effect=Util.mocked_requests)
    def test_exceptions(self, mock_request: Mock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.DESCRIPTION: "Exception"})
        self.assertEqual(context.exception.cause, Messages.EXCEPTION_RATE_LIMIT_BUDGED_EXCEEDED_CAUSE)
        self.assertEqual(context.exception.assistance, "")
