import logging
from unittest import TestCase

from icon_carbon_black_cloud.util.utils import Util


class TestWhitelistChecker(TestCase):
    def test_whitelist_checker(self):
        test_whitelist = ["198.162.1.1", "198.100.1.1/24", "win-test", "12345"]
        log = logging.getLogger("Test")

        self.assertTrue(Util.match_whitelist("198.162.1.1", test_whitelist, log))
        self.assertTrue(Util.match_whitelist("198.100.1.1", test_whitelist, log))
        self.assertTrue(Util.match_whitelist("win-test", test_whitelist, log))
        self.assertTrue(Util.match_whitelist("12345", test_whitelist, log))
        self.assertFalse(Util.match_whitelist("5", test_whitelist, log))
        self.assertFalse(Util.match_whitelist("not-win-test", test_whitelist, log))
        self.assertFalse(Util.match_whitelist("192.200.1.1", test_whitelist, log))
