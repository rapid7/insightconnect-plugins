import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.reputation import Reputation
from komand_domaintools.actions.reputation.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from util import mock_responder, Util

class TestReputation(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(Reputation())
        self.params = {
            Input.DOMAIN: "reputation.com",
            Input.INCLUDE_REASONS: True
        }

    @mock.patch("domaintools.API.reputation", side_effect=mock_responder)
    def test_reputation(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_reputation")
        self.assertEqual(response, expected)
