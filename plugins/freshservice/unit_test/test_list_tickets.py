import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.list_tickets import ListTickets
from icon_freshservice.actions.list_tickets.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListTickets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListTickets())

    @parameterized.expand(Util.load_parameters("list_tickets").get("parameters"))
    def test_list_tickets(
        self,
        mock_request,
        name,
        ticket_filter,
        requester_id,
        email,
        updated_since,
        ticket_type,
        order_type,
        page,
        per_page,
        expected,
    ):
        actual = self.action.run(
            {
                Input.FILTER: ticket_filter,
                Input.REQUESTERID: requester_id,
                Input.EMAIL: email,
                Input.UPDATEDSINCE: updated_since,
                Input.TYPE: ticket_type,
                Input.ORDERTYPE: order_type,
                Input.PAGE: page,
                Input.PERPAGE: per_page,
            }
        )
        self.assertEqual(actual, expected)
