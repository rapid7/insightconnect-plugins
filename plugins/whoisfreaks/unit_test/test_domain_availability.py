import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.domain_availability import DomainAvailability
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestDomainAvailability(ActionTestCase):
    action_class = DomainAvailability

    def test_unavailable_with_suggestions(self):
        body = {
            "domain": "example.com",
            "availability": "unavailable",
            "message": "Domain is not available",
            "domain_available_response": [{"domain": "example.net", "availability": "AVAILABLE"}],
        }
        params = {"domain": "example.com", "suggestions": True, "suggestion_count": 3}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session, "GET", "/v2.0/domain/availability", {"domain": "example.com", "sug": "true", "count": 3}
        )
        self.assertEqual("UNAVAILABLE", output["availability"])
        self.assertFalse(output["available"])
        self.assertEqual("Domain is not available", output["message"])
        self.assertEqual(1, len(output["suggestions"]))

    def test_available_boolean_form(self):
        output, session = self.run_action(
            {"domain": "free.com", "suggestions": False}, MockResponse(200, {"availability": True})
        )
        self.assertEqual({"domain": "free.com", "sug": "false"}, session.calls[-1]["params"])
        self.assertTrue(output["available"])
        self.assertEqual("AVAILABLE", output["availability"])

    def test_unknown_leaves_available_unset(self):
        output, _ = self.run_action({"domain": "x.com"}, MockResponse(200, {"availability": "UNKNOWN"}))
        self.assertNotIn("available", output)

    def test_invalid_count(self):
        with self.assertRaises(PluginException):
            self.run_action({"domain": "x.com", "suggestions": True, "suggestion_count": 500})
