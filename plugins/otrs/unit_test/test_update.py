import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate
from parameterized import parameterized

from komand_otrs.actions.update import Update
from komand_otrs.actions.update.schema import Input
from komand_otrs.util.constants import SESSION_CAUSE
from util import Util

PARAMETERS = {
    Input.TICKETID: 7,
    Input.PRIORITY: "4 high",
    Input.TITLE: "",
    Input.PENDINGTIME: "0001-01-01T00:00:00Z",
    Input.ARTICLE: {"Subject": "Update", "Body": "Ticket updated", "ExcludeNotificationToUserID": []},
    Input.DYNAMICFIELDS: [{"name": "ITSMImpact", "value": "4 high"}],
    Input.ATTACHMENTS: [],
}


class TestUpdate(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Update())

    # Same update either way, the flag only decides whether an Article block is sent
    @parameterized.expand([("with_article", False, True), ("no_article", True, False)])
    @patch("requests.request")
    def test_update(self, _name: str, no_article: bool, has_article: bool, request_mock: MagicMock) -> None:
        # Login, then the PATCH to the ticket
        request_mock.side_effect = [Util.response("access_token"), Util.response("ticket_update")]
        result = self.action.run({**PARAMETERS, Input.NOARTICLE: no_article})
        validate(result, self.action.output.schema)
        self.assertEqual({"ticket_id": 7, "ticket_number": 2018032601000027}, result)

        method, url = request_mock.call_args.args
        self.assertEqual("PATCH", method)
        self.assertTrue(url.endswith("/GenericTicketConnectorREST/Ticket/7"))
        payload = json.loads(request_mock.call_args.kwargs.get("data"))
        self.assertEqual({"Priority": "4 high"}, payload.get("Ticket"))
        self.assertEqual(has_article, "Article" in payload)

        # Empty notification list is dropped so OTRS doesn't get an empty field
        self.assertNotIn("ExcludeNotificationToUserID", payload.get("Article", {}))

    @patch("requests.request")
    def test_update_session_failure(self, request_mock: MagicMock) -> None:
        # Setup mock to return the same response for each call
        request_mock.return_value = Util.response("session_error")

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run({**PARAMETERS, Input.NOARTICLE: False})

        # Verify the exception data
        self.assertEqual(SESSION_CAUSE, context.exception.cause)

    @patch("requests.request")
    def test_update_with_pending_time(self, request_mock: MagicMock) -> None:
        # Pending time goes in its own update first, then the main update. Both reuse one login
        request_mock.side_effect = [
            Util.response("access_token"),
            Util.response("ticket_update"),  # pending time
            Util.response("ticket_update"),
        ]
        result = self.action.run({**PARAMETERS, Input.PENDINGTIME: "2099-11-01T12:30:00+02:00", Input.NOARTICLE: False})
        validate(result, self.action.output.schema)
        self.assertEqual(3, request_mock.call_count)

        # Only one login, so the session is reused between the two updates
        self.assertEqual(1, len([call for call in request_mock.call_args_list if call.args[1].endswith("/Session")]))

        # The offset is converted to UTC and the minutes are kept
        pending_payload = json.loads(request_mock.call_args_list[1].kwargs.get("data"))
        self.assertEqual(
            {"Year": 2099, "Month": 11, "Day": 1, "Hour": 10, "Minute": 30},
            pending_payload.get("Ticket", {}).get("PendingTime"),
        )
