import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.get_ticket import GetTicket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, CLEAN_TICKET, RAW_TICKET, MockResponse, Util, token_response


class TestGetTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, RAW_TICKET))
    def test_get_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run({"ticket_id": 101})

        self.assertEqual({"ticket": CLEAN_TICKET}, result)
        self.assertEqual(("GET", f"{BASE_URL}/api/tickets/101"), mock_request.call_args.args)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(404, text="not found"))
    def test_get_ticket_not_found(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({"ticket_id": 999})

        self.assertEqual("Resource not found.", context.exception.cause)
