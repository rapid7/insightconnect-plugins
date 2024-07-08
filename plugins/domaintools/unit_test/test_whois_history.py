import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_domaintools.actions.whois_history import WhoisHistory
from komand_domaintools.actions.whois_history.schema import Input
from util import mock_responder, Util


class TestWhoisHistory(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(WhoisHistory())
        self.params = {Input.DOMAIN: "whois_history.com"}

    @mock.patch("domaintools.API.whois_history", side_effect=mock_responder)
    def test_whois_history(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_whois_history")
        self.assertEqual(response, expected)
