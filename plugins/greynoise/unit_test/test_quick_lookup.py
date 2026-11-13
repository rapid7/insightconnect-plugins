import logging
from unittest import TestCase, mock

from icon_greynoise.actions.quick_lookup import QuickLookup

from util import MockConnection, mocked_requests_get


class TestQuickLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.quick", side_effect=mocked_requests_get)
    def test_quick_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_quick = QuickLookup()
        test_quick.connection = MockConnection()
        test_quick.logger = log

        working_params = {"ip_address": "quick_lookup"}
        results = test_quick.run(working_params)
        expected = {
            "ip": "1.2.3.4",
            "internet_scanner_intelligence": {"found": True, "classification": "malicious"},
            "business_service_intelligence": {"found": False, "trust_level": "1"},
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
