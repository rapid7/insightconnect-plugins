import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate

from komand_otrs.actions.retrieve import Retrieve
from komand_otrs.actions.retrieve.schema import Input
from komand_otrs.util.constants import SESSION_CAUSE
from util import Util


@patch("requests.request")
class TestRetrieve(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Retrieve())

    def test_retrieve(self, request_mock: MagicMock) -> None:
        # Login, then fetch the ticket with its articles and dynamic fields
        request_mock.side_effect = [Util.response("access_token"), Util.response("ticket_get")]
        result = self.action.run({Input.TICKET_ID: 52})
        validate(result, self.action.output.schema)

        ticket = result.get("Ticket")
        self.assertEqual(52, ticket.get("TicketID"))
        self.assertEqual(0, ticket.get("EscalationTime"))
        self.assertNotIn("SLAID", ticket)  # fixture sends an empty string, which the helper strips
        self.assertEqual(
            [{"Name": "ITSMImpact", "Value": ["3 normal"]}, {"Name": "ITSMReviewRequired", "Value": ["No", "Yes"]}],
            ticket.get("DynamicField"),
        )
        article = ticket.get("Article")[0]
        self.assertEqual((52, 0), (article.get("TicketID"), article.get("IsVisibleForCustomer")))
        self.assertEqual(15, article.get("Attachment")[0].get("FilesizeRaw"))

    def test_retrieve_missing_escalation_time(self, request_mock: MagicMock) -> None:
        # OTRS sends an empty EscalationTime when none is set, so the key should be dropped
        response = Util.response("ticket_get")
        body = json.loads(response.content)
        body["Ticket"][0]["EscalationTime"] = ""
        response._content = json.dumps(body).encode()
        request_mock.side_effect = [Util.response("access_token"), response]
        result = self.action.run({Input.TICKET_ID: 52})
        validate(result, self.action.output.schema)
        self.assertNotIn("EscalationTime", result.get("Ticket"))

    def test_retrieve_real_otrs_types(self, request_mock: MagicMock) -> None:
        # Real OTRS sends TypeID and numeric field values as ints, the fixture uses strings
        response = Util.response("ticket_get")
        body = json.loads(response.content)
        ticket = body["Ticket"][0]
        ticket["TypeID"] = 1
        ticket["DynamicField"].append({"Name": "ITSMScore", "Value": 5})
        response._content = json.dumps(body).encode()
        request_mock.side_effect = [Util.response("access_token"), response]

        result = self.action.run({Input.TICKET_ID: 52})
        validate(result, self.action.output.schema)
        result_ticket = result.get("Ticket")
        self.assertEqual("1", result_ticket.get("TypeID"))
        self.assertEqual({"Name": "ITSMScore", "Value": ["5"]}, result_ticket.get("DynamicField")[-1])

    def test_retrieve_without_articles(self, request_mock: MagicMock) -> None:
        # Ticket with no articles at all, so the Article key should not appear in output
        response = Util.response("ticket_get")
        body = json.loads(response.content)
        body["Ticket"][0].pop("Article", None)
        response._content = json.dumps(body).encode()
        request_mock.side_effect = [Util.response("access_token"), response]
        result = self.action.run({Input.TICKET_ID: 52})
        validate(result, self.action.output.schema)
        self.assertNotIn("Article", result.get("Ticket"))

    def test_retrieve_api_error(self, request_mock: MagicMock) -> None:
        # Setup mock to return different responses for each call
        request_mock.side_effect = [Util.response("access_token"), Util.response("session_error")]

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TICKET_ID: 52})

        # Verify the exception data
        self.assertEqual(PluginException.causes[PluginException.Preset.BAD_REQUEST], context.exception.cause)

    def test_retrieve_session_failure(self, request_mock: MagicMock) -> None:
        # Wrong credentials, login fails before the lookup
        request_mock.return_value = Util.response("session_error")
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TICKET_ID: 52})
        self.assertEqual(SESSION_CAUSE, context.exception.cause)
