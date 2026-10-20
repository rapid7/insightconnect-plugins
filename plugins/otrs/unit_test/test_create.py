import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from datetime import datetime, timedelta, timezone
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate

from komand_otrs.actions.create import Create
from komand_otrs.actions.create.schema import Input
from komand_otrs.util.constants import SESSION_CAUSE
from util import Util

PARAMETERS = {
    Input.TITLE: "Suspicious login detected",
    Input.QUEUE: "Raw",
    Input.TYPE: "Incident",
    Input.STATE: "new",
    Input.PRIORITY: "3 normal",
    Input.CUSTOMERUSER: "test_customer",
    Input.PENDINGTIME: "0001-01-01T00:00:00Z",
    Input.ARTICLE: {
        "Subject": "Suspicious login",
        "Body": "Suspicious login detected for user jdoe",
        "Charset": "UTF-8",
        "ForceNotificationToUserID": [],
    },
    Input.DYNAMIC_FIELDS: [{"name": "ITSMImpact", "value": "3 normal"}],
    Input.ATTACHMENTS: [{"filename": "notes.txt", "content": "VGhpcyBpcyBhIHRlc3QK"}],
}


@patch("requests.request")
class TestCreate(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Create())

    def test_create(self, request_mock: MagicMock) -> None:
        request_mock.side_effect = [Util.response("access_token"), Util.response("ticket_create")]
        result = self.action.run(PARAMETERS)
        validate(result, self.action.output.schema)
        self.assertEqual({"ticket_id": 7, "ticket_number": 2018032601000027}, result)

        # Empty PendingTime and ForceNotificationToUserID are stripped before the request goes out
        payload = json.loads(request_mock.call_args.kwargs.get("data"))
        self.assertEqual("Suspicious login detected", payload.get("Ticket", {}).get("Title"))
        self.assertNotIn("PendingTime", payload.get("Ticket", {}))
        self.assertNotIn("ForceNotificationToUserID", payload.get("Article"))
        self.assertEqual([{"Name": "ITSMImpact", "Value": "3 normal"}], payload.get("DynamicField"))
        self.assertEqual("text/plain", payload.get("Attachment")[0].get("ContentType"))

    def test_create_missing_title(self, request_mock: MagicMock) -> None:
        # Setup mock to return the same response for each call
        request_mock.return_value = Util.response("access_token")

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run({**PARAMETERS, Input.TITLE: ""})

        # Verify the exception data
        self.assertEqual(PluginException.causes[PluginException.Preset.BAD_REQUEST], context.exception.cause)
        self.assertIn("Title is required", str(context.exception.data))

    def test_create_session_failure(self, request_mock: MagicMock) -> None:
        # Setup mock to return the same response for each call
        request_mock.return_value = Util.response("session_error")

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run(PARAMETERS)

        # Verify the exception data
        self.assertEqual(SESSION_CAUSE, context.exception.cause)

    def test_create_with_sla_and_pending_time_uses_one_session(self, request_mock: MagicMock) -> None:
        ticket = json.loads(Util.response("ticket_get").content)
        ticket["Ticket"][0]["SLAID"] = "3"
        ticket_get = Util.response("ticket_get")
        ticket_get._content = json.dumps(ticket).encode()
        pending = (datetime.now(timezone.utc) + timedelta(days=2, hours=3)).isoformat()

        # Replies come back in call order, login first then create, pending time, SLA and get
        request_mock.side_effect = [
            Util.response("access_token"),
            Util.response("ticket_create"),
            Util.response("ticket_update"),  # pending time
            Util.response("ticket_update"),  # SLA
            ticket_get,
        ]
        result = self.action.run({**PARAMETERS, Input.PENDINGTIME: pending, Input.SLA: "Gold", Input.SERVICE: "Email"})
        validate(result, self.action.output.schema)
        self.assertEqual({"ticket_id": 7, "ticket_number": 2018032601000027}, result)
        sessions = [call for call in request_mock.call_args_list if call.args[1].endswith("/Session")]
        self.assertEqual(1, len(sessions))

        # OTRS won't take a plain string on create, so pending time goes in a follow up update
        create_payload = json.loads(request_mock.call_args_list[1].kwargs.get("data"))
        self.assertNotIn("PendingTime", create_payload.get("Ticket", {}))
        update_payload = json.loads(request_mock.call_args_list[2].kwargs.get("data"))
        self.assertEqual(
            {"Year", "Month", "Day", "Hour", "Minute"}, set(update_payload.get("Ticket", {}).get("PendingTime"))
        )

    def test_create_sla_not_set(self, request_mock: MagicMock) -> None:
        # Setup mock to return different responses for each call
        request_mock.side_effect = [
            Util.response("access_token"),
            Util.response("ticket_create"),
            Util.response("ticket_update"),
            Util.response("ticket_get"),  # fixture has an empty SLAID
        ]

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run({**PARAMETERS, Input.SLA: "Gold", Input.SERVICE: "Email"})

        # Verify the exception data
        self.assertEqual("SLA and Service was not set.", context.exception.cause)
