import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.update_ticket import UpdateTicket

from util import BASE_URL, CLEAN_TICKET, RAW_TICKET, MockResponse, Util, token_response


class TestUpdateTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(UpdateTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, [RAW_TICKET]))
    def test_update_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run({"ticket_id": 101, "summary": "Server is unresponsive", "status_id": 2, "impact": 0})

        self.assertEqual({"ticket": CLEAN_TICKET}, result)
        self.assertEqual(("POST", f"{BASE_URL}/api/tickets"), mock_request.call_args.args)
        # Halo updates the ticket whose id is in the body; empty and zero values are not sent
        self.assertEqual(
            [{"id": 101, "summary": "Server is unresponsive", "status_id": 2}], mock_request.call_args.kwargs["json"]
        )
