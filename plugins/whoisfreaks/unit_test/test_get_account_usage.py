import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.get_account_usage import GetAccountUsage
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestGetAccountUsage(ActionTestCase):
    action_class = GetAccountUsage

    def test_usage_hides_api_key(self):
        body = {
            "apiKey": "unit-test-api-key-0123456789abcdef",
            "apiCredits": {"totalCredits": 10000, "servedRequest": 250},
            "apiSubscription": {
                "subscriptionStatus": "active",
                "requestLimit": "100000",
                "servedRequests": 5000,
                "nested": {"api_key": "secret"},
            },
        }
        output, session = self.run_action({}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v1.0/whoisapi/usage")
        self.assertEqual(10000, output["total_credits"])
        self.assertEqual(250, output["used_credits"])
        self.assertEqual("active", output["subscription_status"])
        self.assertEqual(100000, output["subscription_request_limit"])
        self.assertEqual(5000, output["subscription_requests_used"])
        self.assertNotIn("apiKey", output["response"])
        self.assertNotIn("api_key", output["response"]["apiSubscription"]["nested"])

    def test_missing_record(self):
        with self.assertRaises(PluginException):
            self.run_action({}, MockResponse(404, {"message": "The API key does not exist."}))

    def test_invalid_key(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action({}, MockResponse(401, {"message": "Provided API key is invalid."}))
        self.assertEqual("invalid_credentials", context.exception.kind)
