import logging
from unittest import TestCase

from icon_relayshield.actions.check_crypto_intel import CheckCryptoIntel

from util import MockConnection


class TestCheckCryptoIntel(TestCase):
    def test_check_crypto_intel_critical(self):
        test_action = CheckCryptoIntel()
        test_action.connection = MockConnection(
            {
                "/v1/metered/crypto-intel": {
                    "address": "0x1234567890123456789012345678901234567890",
                    "chain_id": "1",
                    "composite_risk": "CRITICAL",
                    "address_flags": ["phishing_activities"],
                    "token_risk": None,
                    "correlation_advisories": [
                        "CRITICAL: This address appears in phishing/sanctions/cybercrime databases."
                    ],
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"address": "0x1234567890123456789012345678901234567890"})

        self.assertEqual("CRITICAL", results["composite_risk"])
        self.assertIn("phishing_activities", results["address_flags"])

    def test_check_crypto_intel_clean(self):
        test_action = CheckCryptoIntel()
        test_action.connection = MockConnection(
            {
                "/v1/metered/crypto-intel": {
                    "address": "0x0000000000000000000000000000000000dead",
                    "chain_id": "1",
                    "composite_risk": "LOW",
                    "address_flags": [],
                    "token_risk": None,
                    "correlation_advisories": ["No risk signals detected on this address."],
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"address": "0x0000000000000000000000000000000000dead"})

        self.assertEqual("LOW", results["composite_risk"])
        self.assertEqual([], results["address_flags"])
