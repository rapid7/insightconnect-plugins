import sys
import os

sys.path.append(os.path.abspath("../"))

from unit_test.util import mock_responder, Util
from unittest import TestCase, mock
from komand_domaintools.actions.brand_monitor import BrandMonitor
from komand_domaintools.actions.brand_monitor.schema import Input


class TestBrandMonitor(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_account) -> None:
        self.action = Util.default_connector(BrandMonitor())
        self.params = {
            Input.QUERY: "test.com",
            Input.EXCLUDE: "example.com",
            Input.DOMAIN_STATUS: "new",
            Input.DAYS_BACK: 1,
        }

    @mock.patch("domaintools.API.brand_monitor", side_effect=mock_responder)
    def test_brand_monitor(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_brand_monitor")
        self.assertEqual(response, expected)
