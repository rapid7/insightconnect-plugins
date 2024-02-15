import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.reverse_ip_whois import ReverseIpWhois
from komand_domaintools.actions.reverse_ip_whois.schema import Input
from util import mock_responder, Util


class TestReverseIpWhois(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(ReverseIpWhois())
        self.params = {
            Input.PAGE: 1,
            Input.IP: "10.10.10.10",
            Input.SERVER: "whois.arin.net",
            Input.COUNTRY: "CA",
            Input.INCLUDE_TOTAL_COUNT: True
        }

    @mock.patch("domaintools.API.reverse_ip_whois", side_effect=mock_responder)
    def test_reverse_whois(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_reverse_ip_whois")
        self.assertEqual(response, expected)