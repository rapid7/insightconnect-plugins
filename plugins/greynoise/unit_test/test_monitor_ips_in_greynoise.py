import logging
from unittest import TestCase, mock

from icon_greynoise.triggers.monitor_ips_in_greynoise import MonitorIpsInGreynoise

from util import MockConnection


class TestMonitorIpsInGreynoise(TestCase):
    @mock.patch("greynoise.GreyNoise.query")
    def test_matching_ips_reads_request_metadata_pages(self, mock_query):
        mock_query.side_effect = [
            {
                "data": [
                    {
                        "ip": "1.2.3.4",
                        "internet_scanner_intelligence": {"found": True, "classification": "malicious"},
                    }
                ],
                "request_metadata": {"count": 2, "complete": False, "scroll": "next"},
            },
            {
                "data": [{"ip": "5.6.7.8"}],
                "request_metadata": {"count": 2, "complete": True, "scroll": ""},
            },
        ]
        trigger = MonitorIpsInGreynoise()
        trigger.connection = MockConnection()
        trigger.logger = logging.getLogger("Test")

        self.assertEqual(trigger._matching_ips("(1.2.3.4 OR 5.6.7.8) last_seen:1d"), ["1.2.3.4", "5.6.7.8"])
        self.assertEqual(mock_query.call_args_list[1].kwargs["scroll"], "next")

    @mock.patch("greynoise.GreyNoise.query")
    def test_matching_ips_empty_when_count_is_zero(self, mock_query):
        mock_query.return_value = {"data": [], "request_metadata": {"count": 0, "complete": True}}
        trigger = MonitorIpsInGreynoise()
        trigger.connection = MockConnection()
        trigger.logger = logging.getLogger("Test")

        self.assertEqual(trigger._matching_ips("(1.2.3.4) last_seen:1d"), [])
        mock_query.assert_called_once()
