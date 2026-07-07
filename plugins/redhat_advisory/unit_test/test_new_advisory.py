import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import timeout_decorator

from komand_redhat_advisory.triggers.new_advisory import NewAdvisory
from komand_redhat_advisory.triggers.new_advisory.schema import Input
from util import Util


class TestNewAdvisory(TestCase):
    @patch("requests.Session.send", side_effect=Util.mocked_session_send)
    def test_new_advisory_happy_path(self, _mock_send):
        trigger = Util.default_connector(NewAdvisory())

        sent_events = []
        trigger.send = sent_events.append
        trigger.state = {}
        trigger.state_file = ""
        trigger.load_state = lambda: None
        try:
            trigger.run_trigger = True
        except AttributeError:
            # Newer SDK exposes run_trigger as a read-only @property; it returns True by default.
            pass

        try:
            timeout_decorator.timeout(1)(trigger.run)(
                {
                    Input.AFTER: "2026-06-30",
                    Input.INCLUDE_SOURCE: False,
                }
            )
        except timeout_decorator.timeout_decorator.TimeoutError:
            pass

        rhsas = [event["rhsa"] for event in sent_events]
        self.assertEqual(rhsas, ["RHSA-2026:30858", "RHSA-2026:30859"])

        first = sent_events[0]
        self.assertEqual(first["severity"], "important")
        self.assertEqual(first["cves"], ["CVE-2026-48962"])
        self.assertEqual(first["bugzillas"], ["2481767"])
        self.assertEqual(first["released_on"], "2026-06-30T02:38:12Z")
        self.assertEqual(first["released_packages"], ["perl-IO-Compress-0:2.081-2.el8_10"])
