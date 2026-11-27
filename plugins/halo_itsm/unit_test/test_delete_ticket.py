import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.delete_ticket import DeleteTicket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, MockResponse, Util, token_response


class TestDeleteTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(204))
    def test_delete_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run({"ticket_id": 101})

        self.assertEqual({"success": True}, result)
        self.assertEqual(("DELETE", f"{BASE_URL}/api/tickets/101"), mock_request.call_args.args)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(403, text="forbidden"))
    def test_delete_ticket_permission_denied(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({"ticket_id": 101})

        self.assertEqual("Permission denied.", context.exception.cause)
