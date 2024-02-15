import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.ip_monitor import IpMonitor
from komand_domaintools.actions.ip_monitor.schema import Input
from util import mock_responder, Util


class TestIpMonitor(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(IpMonitor())
        self.params = {
            Input.PAGE: 1,
            Input.DAYS_BACK: 1,
            Input.QUERY: "ip_monitor.com"
        }

    @mock.patch("domaintools.API.ip_monitor", side_effect=mock_responder)
    def test_ip_monitor(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_ip_monitor")
        self.assertEqual(response, expected)
