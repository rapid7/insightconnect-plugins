import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.registrant_monitor import RegistrantMonitor
from komand_domaintools.actions.registrant_monitor.schema import Input
from util import mock_responder, Util


class TestRegistrantMonitor(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(RegistrantMonitor())
        self.params = {
            Input.QUERY: "registrant_monitor.com",
            Input.DAYS_BACK: 1,
            Input.EXCLUDE: "test.com"
        }

    @mock.patch("domaintools.API.registrant_monitor", side_effect=mock_responder)
    def test_registrant_monitor(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_registrant_monitor")
        self.assertEqual(response, expected)
