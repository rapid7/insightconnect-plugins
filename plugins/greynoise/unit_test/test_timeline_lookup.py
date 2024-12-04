import logging
from unittest import TestCase, mock

from icon_greynoise.actions.timeline_lookup import TimelineLookup

from util import MockConnection, mocked_requests_get


class TestTimelineLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.timelinedaily", side_effect=mocked_requests_get)
    def test_timeline_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_timeline = TimelineLookup()
        test_timeline.connection = MockConnection()
        test_timeline.logger = log

        working_params = {"ip_address": "timeline_lookup"}
        results = test_timeline.run(working_params)
        expected = {
            "activity": [
                {
                    "asn": "AS12345",
                    "category": "hosting",
                    "city": "Berlin",
                    "classification": "benign",
                    "country": "Germany",
                    "country_code": "DE",
                    "destinations": [{"country": "South Africa", "country_code": "ZA"}],
                    "hassh_fingerprints": [],
                    "http_paths": ["/favicon.ico"],
                    "http_user_agents": ["Mozilla/5.0"],
                    "ja3_fingerprints": ["04b3f524166caafd433b6864250945be"],
                    "organization": "Alpha Strike Labs GmbH",
                    "protocols": [{"port": 80, "transport_protocol": "TCP"}],
                    "rdns": "",
                    "region": "Berlin",
                    "spoofable": True,
                    "tags": [
                        {
                            "category": "actor",
                            "description": "description.",
                            "intention": "benign",
                            "name": "Acme, Inc.",
                        }
                    ],
                    "timestamp": "2024-11-03T00:00:00Z",
                    "tor": False,
                    "vpn": False,
                    "vpn_service": "",
                }
            ],
            "ip": "1.2.3.4",
            "metadata": {
                "end_time": "2024-11-04T19:13:35.892189739Z",
                "ip": "1.2.3.4",
                "limit": 50,
                "next_cursor": "",
                "start_time": "2024-11-03T00:00:00Z",
            },
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
