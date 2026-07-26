import logging
from unittest import TestCase

from icon_relayshield.actions.check_sim_swap import CheckSimSwap

from util import MockConnection


class TestCheckSimSwap(TestCase):
    def test_check_sim_swap_detected(self):
        test_action = CheckSimSwap()
        test_action.connection = MockConnection(
            {
                "/v1/metered/sim-swap": {
                    "phone": "+14155551234",
                    "swapped": True,
                    "swap_timestamp": "2026-07-20T00:00:00Z",
                    "carrier": "Verizon",
                    "checked_at": "2026-07-26T00:00:00Z",
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"phone": "+14155551234"})

        self.assertTrue(results["swapped"])
        self.assertEqual("Verizon", results["carrier"])

    def test_check_sim_swap_clean(self):
        test_action = CheckSimSwap()
        test_action.connection = MockConnection(
            {
                "/v1/metered/sim-swap": {
                    "phone": "+14155559999",
                    "swapped": False,
                    "swap_timestamp": "",
                    "carrier": "T-Mobile",
                    "checked_at": "2026-07-26T00:00:00Z",
                }
            }
        )
        test_action.logger = logging.getLogger("Test")

        results = test_action.run({"phone": "+14155559999"})

        self.assertFalse(results["swapped"])
