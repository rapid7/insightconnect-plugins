import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.domain_profile import DomainProfile
from komand_domaintools.actions.domain_profile.schema import Input
from util import mock_responder, Util


class TestDomainProfile(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(DomainProfile())
        self.params = {Input.DOMAIN: "example.com"}

    @mock.patch("domaintools.API.domain_profile", side_effect=mock_responder)
    def test_domain_profile(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_domain_profile")
        self.assertEqual(response, expected)
