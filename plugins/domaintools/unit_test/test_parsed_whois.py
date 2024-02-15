import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.parsed_whois import ParsedWhois
from komand_domaintools.actions.parsed_whois.schema import Input
from util import mock_responder, Util


class TestParsedWhois(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(ParsedWhois())
        self.params = {Input.DOMAIN: "parsed_whois.com"}

    @mock.patch("domaintools.API.parsed_whois", side_effect=mock_responder)
    def test_parsed_whois_monitor(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_parsed_whois.py")
        self.assertEqual(response, expected)
