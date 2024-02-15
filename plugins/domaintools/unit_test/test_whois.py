import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.whois import Whois
from komand_domaintools.actions.whois.schema import Input
from util import mock_responder, Util



class TestWhois(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(Whois())
        self.params = {
            Input.QUERY: "whois.com",
        }

    @mock.patch("domaintools.API.whois", side_effect=mock_responder)
    def test_whois(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_whois")
        self.assertEqual(response, expected)
