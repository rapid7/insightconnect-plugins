import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitdefender_gravityzone.actions.find_endpoint import FindEndpoint
from icon_bitdefender_gravityzone.actions.find_endpoint.schema import Input, Output
from util import NETWORK_URL, Util

FQDN = "workstation-01.example.com"
OTHER_FQDN = "workstation-01.other.example.com"


@patch("requests.Session.send")
class TestFindEndpoint(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(FindEndpoint())

    def test_matching(self, mock_send):
        # Every candidate is returned by the prefix search; only exact, case-insensitive matches count
        cases = [
            {
                "name": "short name, one exact match among prefix matches",
                "hostname": "workstation-01",
                "candidates": [
                    Util.endpoint("id-1", "WORKSTATION-01", FQDN),
                    Util.endpoint("id-2", "WORKSTATION-010"),
                    Util.endpoint("id-3", "workstation-01-old"),
                ],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-1",
            },
            {
                "name": "short name, only prefix matches",
                "hostname": "workstation-01",
                "candidates": [Util.endpoint("id-2", "WORKSTATION-010"), Util.endpoint("id-3", "WORKSTATION-01-OLD")],
                "found": False,
                "match_count": 0,
            },
            {
                "name": "short name, no candidates",
                "hostname": "workstation-01",
                "candidates": [],
                "found": False,
                "match_count": 0,
            },
            {
                "name": "short name, ambiguous",
                "hostname": "WORKSTATION-01",
                "candidates": [Util.endpoint("id-1", "WORKSTATION-01", FQDN), Util.endpoint("id-4", "workstation-01")],
                "found": False,
                "match_count": 2,
            },
            {
                "name": "short name does not match on FQDN",
                "hostname": "workstation-01",
                "candidates": [Util.endpoint("id-5", "LAPTOP-7", "workstation-01")],
                "found": False,
                "match_count": 0,
            },
            {
                "name": "FQDN picks the endpoint with that FQDN among endpoints sharing the short name",
                "hostname": FQDN,
                "candidates": [
                    Util.endpoint("id-1", "WORKSTATION-01", FQDN),
                    Util.endpoint("id-6", "WORKSTATION-01", OTHER_FQDN),
                ],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-1",
            },
            {
                "name": "FQDN is matched ignoring case, spaces and a trailing dot",
                "hostname": "  WORKSTATION-01.Example.COM.  ",
                "candidates": [Util.endpoint("id-1", "WORKSTATION-01", FQDN)],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-1",
            },
            {
                "name": "FQDN given, one same-name candidate with no FQDN",
                "hostname": FQDN,
                "candidates": [Util.endpoint("id-7", "WORKSTATION-01", None)],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-7",
            },
            {
                "name": "FQDN given, one same-name candidate with an empty FQDN",
                "hostname": FQDN,
                "candidates": [Util.endpoint("id-7", "WORKSTATION-01", "")],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-7",
            },
            {
                "name": "FQDN given, the only same-name candidate has another FQDN",
                "hostname": FQDN,
                "candidates": [Util.endpoint("id-6", "WORKSTATION-01", OTHER_FQDN)],
                "found": False,
                "match_count": 0,
            },
            {
                "name": "short name given, the only candidate has an FQDN",
                "hostname": "workstation-01",
                "candidates": [Util.endpoint("id-6", "WORKSTATION-01", OTHER_FQDN)],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-6",
            },
            {
                "name": "FQDN fallback to the short name is ambiguous",
                "hostname": FQDN,
                "candidates": [
                    Util.endpoint("id-7", "WORKSTATION-01", None),
                    Util.endpoint("id-6", "WORKSTATION-01", OTHER_FQDN),
                ],
                "found": False,
                "match_count": 2,
            },
            {
                "name": "FQDN matching two endpoints is ambiguous",
                "hostname": FQDN,
                "candidates": [Util.endpoint("id-1", "WORKSTATION-01", FQDN), Util.endpoint("id-8", "WS-01", FQDN)],
                "found": False,
                "match_count": 2,
            },
            {
                "name": "the same endpoint listed twice is one match",
                "hostname": "workstation-01",
                "candidates": [
                    Util.endpoint("id-1", "WORKSTATION-01", FQDN),
                    Util.endpoint("id-1", "WORKSTATION-01", FQDN),
                ],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-1",
            },
        ]
        for case in cases:
            with self.subTest(case["name"]):
                mock_send.reset_mock()
                mock_send.return_value = Util.endpoints_page(case["candidates"])

                result = self.action.run({Input.HOSTNAME: case["hostname"]})

                self.action.output.validate(result)
                self.assertEqual(case["found"], result[Output.FOUND])
                self.assertEqual(case["match_count"], result[Output.MATCH_COUNT])
                if case["found"]:
                    self.assertEqual(case["endpoint_id"], result[Output.ENDPOINT]["id"])
                else:
                    self.assertEqual({}, result[Output.ENDPOINT])

    def test_found_endpoint_fields(self, mock_send):
        mock_send.return_value = Util.endpoints_page([Util.endpoint("id-1", "WORKSTATION-01", FQDN, is_isolated=True)])

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertEqual(
            {
                "id": "id-1",
                "name": "WORKSTATION-01",
                "fqdn": FQDN,
                "ip": "10.0.0.15",
                "macs": ["00:1a:2b:3c:4d:5e"],
                "is_managed": True,
                "is_isolated": True,
            },
            result[Output.ENDPOINT],
        )

    def test_search_request(self, mock_send):
        mock_send.return_value = Util.endpoints_page([])

        self.action.run({Input.HOSTNAME: "Workstation-01.Example.com"})

        self.assertEqual(3, mock_send.call_count)
        for index, name_filter in enumerate(["Workstation-01", "workstation-01", "WORKSTATION-01"]):
            with self.subTest(name_filter):
                payload = Util.sent_payload(mock_send, index)
                self.assertEqual(NETWORK_URL, Util.sent_request(mock_send, index).url)
                self.assertEqual("getEndpointsList", payload["method"])
                self.assertEqual(
                    {
                        "page": 1,
                        "perPage": 100,
                        "isManaged": True,
                        "filters": {"details": {"name": name_filter}, "depth": {"allItemsRecursively": True}},
                    },
                    payload["params"],
                )

    def test_name_filter_variants(self, mock_send):
        cases = [
            ("mixed case FQDN", "Workstation-01.Example.com", ["Workstation-01", "workstation-01", "WORKSTATION-01"]),
            ("lower case", "workstation-01", ["workstation-01", "WORKSTATION-01"]),
            ("upper case", "WORKSTATION-01", ["WORKSTATION-01", "workstation-01"]),
            ("no letters", "123456", ["123456"]),
            ("spaces and a trailing dot", "  Ws-001.example.com.  ", ["Ws-001", "ws-001", "WS-001"]),
        ]
        for name, hostname, expected_name_filters in cases:
            with self.subTest(name):
                mock_send.reset_mock()
                mock_send.return_value = Util.endpoints_page([])

                self.action.run({Input.HOSTNAME: hostname})

                self.assertEqual(
                    [(name_filter, 1) for name_filter in expected_name_filters], Util.sent_name_filters(mock_send)
                )

    def test_upper_case_name_is_found_when_the_filter_is_case_sensitive(self, mock_send):
        # Only the upper-case search returns the endpoint, as a case-sensitive name filter would
        mock_send.side_effect = Util.endpoints_by_name_filter(
            {"WORKSTATION-01": [[Util.endpoint("id-1", "WORKSTATION-01", FQDN)]]}
        )

        result = self.action.run({Input.HOSTNAME: "workstation-01.example.com"})

        self.assertTrue(result[Output.FOUND])
        self.assertEqual("id-1", result[Output.ENDPOINT]["id"])

    def test_results_of_the_variants_are_merged_by_id(self, mock_send):
        same_endpoint = Util.endpoint("id-1", "WORKSTATION-01", FQDN)
        cases = [
            {
                "name": "the same endpoint returned by every variant is one match",
                "pages": {
                    "Workstation-01": [[same_endpoint]],
                    "workstation-01": [[same_endpoint]],
                    "WORKSTATION-01": [[same_endpoint]],
                },
                "found": True,
                "match_count": 1,
            },
            {
                "name": "different endpoints returned by different variants are all counted",
                "pages": {
                    "workstation-01": [[Util.endpoint("id-1", "workstation-01")]],
                    "WORKSTATION-01": [[Util.endpoint("id-9", "WORKSTATION-01")]],
                },
                "found": False,
                "match_count": 2,
            },
        ]
        for case in cases:
            with self.subTest(case["name"]):
                mock_send.reset_mock(side_effect=True)
                mock_send.side_effect = Util.endpoints_by_name_filter(case["pages"])

                result = self.action.run({Input.HOSTNAME: "Workstation-01"})

                self.assertEqual(case["found"], result[Output.FOUND])
                self.assertEqual(case["match_count"], result[Output.MATCH_COUNT])

    def test_reads_every_page(self, mock_send):
        mock_send.side_effect = Util.endpoints_by_name_filter(
            {
                "workstation-01": [
                    [Util.endpoint("id-2", "WORKSTATION-010")],
                    [Util.endpoint("id-1", "WORKSTATION-01", FQDN)],
                ]
            }
        )

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertTrue(result[Output.FOUND])
        self.assertEqual("id-1", result[Output.ENDPOINT]["id"])
        self.assertEqual(
            [("workstation-01", 1), ("workstation-01", 2), ("WORKSTATION-01", 1)], Util.sent_name_filters(mock_send)
        )

    def test_duplicate_on_a_later_page_makes_the_hostname_ambiguous(self, mock_send):
        mock_send.side_effect = Util.endpoints_by_name_filter(
            {
                "workstation-01": [
                    [Util.endpoint("id-1", "WORKSTATION-01", FQDN)],
                    [Util.endpoint("id-4", "workstation-01")],
                ]
            }
        )

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertEqual({Output.FOUND: False, Output.MATCH_COUNT: 2, Output.ENDPOINT: {}}, result)

    def test_pages_without_pages_count_stop_at_a_short_page(self, mock_send):
        full_page = [Util.endpoint(f"prefix-only-{index}", f"WORKSTATION-01{index}") for index in range(100)]
        mock_send.side_effect = Util.endpoints_by_name_filter(
            {"workstation-01": [full_page, [Util.endpoint("id-1", "WORKSTATION-01", FQDN)]]}, with_pages_count=False
        )

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertTrue(result[Output.FOUND])
        self.assertEqual(
            [("workstation-01", 1), ("workstation-01", 2), ("WORKSTATION-01", 1)], Util.sent_name_filters(mock_send)
        )

    def test_hostname_that_cannot_be_searched(self, mock_send):
        for hostname in ["", "   ", "ws", "ab.example.com", ".example.com"]:
            with self.subTest(hostname=hostname):
                with self.assertRaises(PluginException) as context:
                    self.action.run({Input.HOSTNAME: hostname})

                self.assertIn("too short to search for", context.exception.cause)
                self.assertIn("at least 3 characters", context.exception.assistance)
        mock_send.assert_not_called()

    def test_api_error_is_raised(self, mock_send):
        mock_send.return_value = Util.rpc_error(-32001, "Authorization error", "API Key is not allowed")

        with self.assertRaises(PluginException) as context:
            self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertEqual("GravityZone API error -32001: Authorization error.", context.exception.cause)
