import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.historical_dns import HistoricalDns
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestHistoricalDns(ActionTestCase):
    action_class = HistoricalDns

    def test_snapshots(self):
        body = {"totalRecords": 3, "totalPages": 1, "currentPage": 1, "historicalDnsRecords": [{"queryTime": "t"}]}
        params = {"domain": "example.com", "record_types": "all", "page": 1}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session, "GET", "/v2.0/dns/historical", {"domainName": "example.com", "type": "all", "page": 1}
        )
        self.assertEqual(3, output["total_records"])

    def test_ptr_is_rejected(self):
        with self.assertRaises(PluginException):
            self.run_action({"domain": "example.com", "record_types": "PTR"})
