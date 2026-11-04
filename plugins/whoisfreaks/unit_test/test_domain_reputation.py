import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.domain_reputation import DomainReputation
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestDomainReputation(ActionTestCase):
    action_class = DomainReputation

    def test_assessment(self):
        body = {
            "risk_category": {"verdict": "clean", "severity": "low", "confidence": 0.92},
            "trust_signals": {"trust_score": 85},
            "dga_score": {"is_dga": False},
        }
        output, session = self.run_action({"domain": "example.com"}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v1/domain/security", {"domainName": "example.com"})
        self.assertEqual(
            ("clean", "low", 0.92, 85, False),
            tuple(output[key] for key in ("verdict", "severity", "confidence", "trust_score", "is_dga")),
        )

    def test_unexpected_types_are_dropped(self):
        body = {
            "risk_category": {"verdict": {"nested": True}, "confidence": "high"},
            "trust_signals": {"trust_score": "n/a"},
        }
        output, _ = self.run_action({"domain": "example.com"}, MockResponse(200, body))
        for key in ("verdict", "confidence", "trust_score"):
            self.assertNotIn(key, output)
