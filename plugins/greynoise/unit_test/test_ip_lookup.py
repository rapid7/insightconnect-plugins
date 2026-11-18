import json
import logging
import os
from unittest import TestCase, mock

from icon_greynoise.actions.ip_lookup import IpLookup

from util import MockConnection, read_file_to_string


def ip_response(*_args, **_kwargs):
    return json.loads(read_file_to_string(os.path.join(os.path.dirname(__file__), "payloads/ip_lookup.json")))


class TestIpLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.ip", side_effect=ip_response)
    def test_ip_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_ip = IpLookup()
        test_ip.connection = MockConnection()
        test_ip.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_ip.run(working_params)
        payload = ip_response()
        expected = {
            "ip": "1.2.3.4",
            "viz_url": "https://viz.greynoise.io/ip/1.2.3.4",
            "internet_scanner_intelligence": payload["internet_scanner_intelligence"],
            "business_service_intelligence": payload["business_service_intelligence"],
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
        self.assertEqual(mock_get.call_args.args[0], "1.2.3.4")
