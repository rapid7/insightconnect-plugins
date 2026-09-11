import logging
from unittest import TestCase

from icon_relayshield.actions.check_breach import CheckBreach

from util import MockConnection


class TestCheckBreach(TestCase):
    def test_check_breach_found(self):
        test_action = CheckBreach()
        test_action.connection = MockConnection(
            {
                "/v1/metered/breach": {
                    "email": "user@example.com",
                    "record_type": "credential_exposure",
                    "breach_count": 1,
                    "breaches": [
                        {
                            "name": "Adobe",
                            "domain": "adobe.com",
                            "breach_date": "2013-10-04",
                            "data_classes": ["Email addresses", "Passwords"],
                            "is_verified": True,
                        }
                    ],
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"email": "user@example.com"})

        self.assertEqual("user@example.com", results["email"])
        self.assertEqual(1, results["breach_count"])
        self.assertEqual("Adobe", results["breaches"][0]["name"])

    def test_check_breach_clean(self):
        test_action = CheckBreach()
        test_action.connection = MockConnection(
            {
                "/v1/metered/breach": {
                    "email": "clean@example.com",
                    "record_type": "credential_exposure",
                    "breach_count": 0,
                    "breaches": [],
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"email": "clean@example.com"})

        self.assertEqual(0, results["breach_count"])
        self.assertEqual([], results["breaches"])
