import logging
from unittest import TestCase

from icon_relayshield.actions.check_domain import CheckDomain

from util import MockConnection


class TestCheckDomain(TestCase):
    def test_check_domain_lookalikes_found(self):
        test_action = CheckDomain()
        test_action.connection = MockConnection(
            {
                "/v1/metered/domain": {
                    "domain": "example.com",
                    "lookalikes_found": 1,
                    "lookalikes": [
                        {
                            "domain": "exarnple.com",
                            "gsb_flagged": False,
                            "registration_age_days": 4,
                            "cert_count": 1,
                            "cert_recent": True,
                            "latest_cert_issued": "2026-07-20T00:00:00Z",
                        }
                    ],
                    "candidates_checked": 12,
                    "checked_at": "2026-07-26T00:00:00Z",
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"domain": "example.com"})

        self.assertEqual(1, results["lookalikes_found"])
        self.assertEqual("exarnple.com", results["lookalikes"][0]["domain"])

    def test_check_domain_clean(self):
        test_action = CheckDomain()
        test_action.connection = MockConnection(
            {
                "/v1/metered/domain": {
                    "domain": "clean-example.com",
                    "lookalikes_found": 0,
                    "lookalikes": [],
                    "candidates_checked": 10,
                    "checked_at": "2026-07-26T00:00:00Z",
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"domain": "clean-example.com"})

        self.assertEqual(0, results["lookalikes_found"])
