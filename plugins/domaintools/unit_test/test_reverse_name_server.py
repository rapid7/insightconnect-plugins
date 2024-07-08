import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from komand_domaintools.actions.reverse_name_server import ReverseNameServer
from komand_domaintools.actions.reverse_name_server.schema import Input
from unit_test.util import mock_responder, Util


class TestReverseNameServer(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(ReverseNameServer())
        self.params = {Input.DOMAIN: "reverse_name_server.com", Input.LIMIT: 1}

    @mock.patch("domaintools.API.reverse_name_server", side_effect=mock_responder)
    def test_reverse_name_server(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_reverse_name_server")
        self.assertEqual(response, expected)
