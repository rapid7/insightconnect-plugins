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
                "name": "FQDN falls back to the short name when no FQDN matches",
                "hostname": FQDN,
                "candidates": [Util.endpoint("id-7", "WORKSTATION-01", None)],
                "found": True,
                "match_count": 1,
                "endpoint_id": "id-7",
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

        payload = Util.sent_payload(mock_send)
        self.assertEqual(NETWORK_URL, Util.sent_request(mock_send).url)
        self.assertEqual("getEndpointsList", payload["method"])
        self.assertEqual(
            {
                "page": 1,
                "perPage": 100,
                "isManaged": True,
                "filters": {"details": {"name": "workstation-01"}, "depth": {"allItemsRecursively": True}},
            },
            payload["params"],
        )

    def test_reads_every_page(self, mock_send):
        mock_send.side_effect = [
            Util.endpoints_page([Util.endpoint("id-2", "WORKSTATION-010")], page=1, pages_count=2),
            Util.endpoints_page([Util.endpoint("id-1", "WORKSTATION-01", FQDN)], page=2, pages_count=2),
        ]

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertTrue(result[Output.FOUND])
        self.assertEqual("id-1", result[Output.ENDPOINT]["id"])
        self.assertEqual([1, 2], [Util.sent_payload(mock_send, index)["params"]["page"] for index in range(2)])

    def test_duplicate_on_a_later_page_makes_the_hostname_ambiguous(self, mock_send):
        mock_send.side_effect = [
            Util.endpoints_page([Util.endpoint("id-1", "WORKSTATION-01", FQDN)], page=1, pages_count=2),
            Util.endpoints_page([Util.endpoint("id-4", "workstation-01")], page=2, pages_count=2),
        ]

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertEqual({Output.FOUND: False, Output.MATCH_COUNT: 2, Output.ENDPOINT: {}}, result)

    def test_pages_without_pages_count_stop_at_a_short_page(self, mock_send):
        full_page = [Util.endpoint(f"prefix-only-{index}", f"WORKSTATION-01{index}") for index in range(100)]
        mock_send.side_effect = [
            Util.endpoints_page(full_page, page=1, pages_count=None),
            Util.endpoints_page([Util.endpoint("id-1", "WORKSTATION-01", FQDN)], page=2, pages_count=None),
        ]

        result = self.action.run({Input.HOSTNAME: "workstation-01"})

        self.assertEqual(2, mock_send.call_count)
        self.assertTrue(result[Output.FOUND])

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
