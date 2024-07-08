import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_domaintools.actions.hosting_history import HostingHistory
from komand_domaintools.actions.hosting_history.schema import Input
from util import mock_responder, Util


class TestHostingHistory(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(HostingHistory())
        self.params = {Input.DOMAIN: "hosting_history.com"}

    @mock.patch("domaintools.API.hosting_history", side_effect=mock_responder)
    def test_hosting_history(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_hosting_history")
        self.assertEqual(response, expected)
