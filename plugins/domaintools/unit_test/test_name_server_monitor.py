import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_domaintools.actions.name_server_monitor import NameServerMonitor
from komand_domaintools.actions.name_server_monitor.schema import Input
from util import mock_responder, Util


class TestNameServerMonitor(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(NameServerMonitor())
        self.params = {
            Input.QUERY: "name_server_monitor.com",
            Input.PAGE: 1,
            Input.DAYS_BACK: 0
        }

    @mock.patch("domaintools.API.name_server_monitor", side_effect=mock_responder)
    def test_name_server_monitor(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_name_server_monitor")
        self.assertEqual(response, expected)
