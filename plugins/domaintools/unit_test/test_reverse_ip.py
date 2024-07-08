import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_domaintools.actions.reverse_ip import ReverseIp
from komand_domaintools.actions.reverse_ip.schema import Input
from unit_test.util import mock_responder, Util


class TestReverseIp(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(ReverseIp())
        self.params = {Input.DOMAIN: "reverse_ip.com", Input.LIMIT: 1}

    @mock.patch("domaintools.API.reverse_ip", side_effect=mock_responder)
    def test_reverse_ip(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_reverse_ip")
        self.assertEqual(response, expected)
