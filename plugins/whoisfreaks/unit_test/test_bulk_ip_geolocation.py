import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.bulk_ip_geolocation import BulkIpGeolocation
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestBulkIpGeolocation(ActionTestCase):
    action_class = BulkIpGeolocation

    def test_bulk(self):
        params = {"ip_addresses": ["8.8.8.8", "1.1.1.1", "10.0.0.1", "nope", "8.8.8.8"]}
        output, session = self.run_action(params, MockResponse(200, [{"ip": "8.8.8.8"}, {"ip": "1.1.1.1"}]))
        self.assert_request(session, "POST", "/v1.0/geolocation", None, {"ips": ["8.8.8.8", "1.1.1.1"]})
        self.assertEqual(2, len(output["results"]))
        self.assertEqual(
            ["Private, reserved or special-use IP address", "Not a valid IP address", "Duplicate value"],
            [item["reason"] for item in output["skipped"]],
        )

    def test_list_too_large_from_api(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action(
                {"ip_addresses": ["8.8.8.8"]},
                MockResponse(
                    413, {"message": "The requested list size is [101] which exceeds the maximum list size of 100."}
                ),
            )
        self.assertEqual("list_too_large", context.exception.kind)
