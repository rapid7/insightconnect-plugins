import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_bitdefender_gravityzone.actions.get_endpoints_list import GetEndpointsList
from komand_bitdefender_gravityzone.actions.get_endpoints_list.schema import Input
from util import Util


class TestGetEndpointsList(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetEndpointsList())

    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_get_endpoints_list(self, mock_post):
        """Test successful endpoint listing with default parameters."""
        test_input = {
            Input.PAGE: 1,
            Input.PER_PAGE: 30,
        }
        result = self.action.run(test_input)

        self.assertEqual(result["total"], 2)
        self.assertEqual(result["page"], 1)
        self.assertEqual(result["per_page"], 30)
        self.assertEqual(len(result["endpoints"]), 2)

        # Verify first endpoint fields are mapped correctly
        endpoint = result["endpoints"][0]
        self.assertEqual(endpoint["id"], "5a4f2c3b6e9d1a0012345678")
        self.assertEqual(endpoint["name"], "WORKSTATION-001")
        self.assertEqual(endpoint["label"], "Engineering Lab")
        self.assertEqual(endpoint["fqdn"], "workstation-001.corp.example.com")
        self.assertEqual(endpoint["group_id"], "abcdef1234567890abcdef12")
        self.assertTrue(endpoint["is_managed"])
        self.assertEqual(endpoint["machine_type"], 1)
        self.assertEqual(endpoint["operating_system_version"], "Windows 10 Pro 21H2")
        self.assertEqual(endpoint["ip"], "192.168.1.100")
        self.assertEqual(endpoint["macs"], ["AA:BB:CC:DD:EE:01"])
        self.assertTrue(endpoint["managed_with_best"])

    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_get_endpoints_list_with_filters(self, mock_post):
        """Test endpoint listing with parent_id and is_managed filters."""
        test_input = {
            Input.PARENT_ID: "abcdef1234567890abcdef12",
            Input.IS_MANAGED: True,
            Input.PAGE: 1,
            Input.PER_PAGE: 30,
        }
        result = self.action.run(test_input)

        self.assertIsInstance(result["endpoints"], list)
        self.assertGreater(len(result["endpoints"]), 0)

    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_get_endpoints_list_empty(self, mock_post):
        """Test endpoint listing with no results."""
        test_input = {
            Input.NAME_FILTER: "nonexistent*",
            Input.PAGE: 1,
            Input.PER_PAGE: 30,
        }
        result = self.action.run(test_input)

        self.assertEqual(result["total"], 0)
        self.assertEqual(result["endpoints"], [])
