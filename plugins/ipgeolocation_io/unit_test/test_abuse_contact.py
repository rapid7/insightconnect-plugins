from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.abuse_contact import AbuseContact
from icon_ipgeolocation_io.actions.abuse_contact.schema import Input, Output
from unit_test.mock import DOMAIN, IP_ABUSE, IP_BOGON, make_action, mock_request, sent_params

import os
import sys

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=mock_request)
class TestAbuseContact(TestCase):
    def setUp(self):
        self.action = make_action(AbuseContact)

    def test_returns_the_abuse_contact(self, _):
        actual = self.action.run({Input.IP: IP_ABUSE})

        self.assertEqual(actual[Output.IP], IP_ABUSE)
        abuse = actual[Output.ABUSE]
        self.assertEqual(abuse["emails"], ["helpdesk@apnic.net"])
        self.assertEqual(abuse["phone_numbers"], ["+61 7 3858 3100"])
        self.assertEqual(abuse["kind"], "group")
        self.assertEqual(abuse["route"], "1.0.0.0/24")
        # organization comes back empty for this record and should be dropped.
        self.assertNotIn("organization", abuse)

    def test_missing_ip_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({})

        self.assertIn("No IP address was provided", context.exception.cause)
        mocked.assert_not_called()

    def test_domain_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IP: DOMAIN})
        mocked.assert_not_called()

    def test_private_address_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IP: IP_BOGON})
        mocked.assert_not_called()

    def test_field_filters_are_forwarded(self, mocked):
        self.action.run({Input.IP: IP_ABUSE, Input.FIELDS: ["abuse.emails"]})

        self.assertEqual(sent_params(mocked)["fields"], "abuse.emails")
