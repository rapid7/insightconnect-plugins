import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from komand_rapid7_intelhub.actions.search_cves.action import SearchCves
from komand_rapid7_intelhub.actions.get_cve.action import GetCve
from komand_rapid7_intelhub.connection.connection import Connection
import json


class MockConnection:
    def __init__(self):
        self.api_key = "test-api-key"
        self.base_url = "https://us.api.insight.rapid7.com/intelligencehub/intelligence-hub/v1"

    def get_headers(self):
        return {
            "X-Api-Key": self.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }


class TestSearchCves(TestCase):
    @patch("komand_rapid7_intelhub.util.api.requests.request")
    def test_search_cves(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "cve_id": "CVE-2025-12345",
                    "title": "Test Vulnerability",
                    "description": "A test vulnerability",
                    "severity": "High",
                    "cvss_score": 8.5,
                    "published_date": "2025-01-15",
                }
            ],
            "page": 1,
            "page_size": 10,
            "total_count": 1,
            "total_pages": 1,
        }
        mock_request.return_value = mock_response

        action = SearchCves()
        action.connection = MockConnection()
        action.logger = MagicMock()

        result = action.run({"search": "test", "page": 1, "page_size": 10})

        self.assertEqual(len(result["cves"]), 1)
        self.assertEqual(result["cves"][0]["cve_id"], "CVE-2025-12345")
        self.assertEqual(result["pagination"]["total_count"], 1)


class TestGetCve(TestCase):
    @patch("komand_rapid7_intelhub.util.api.requests.request")
    def test_get_cve_found(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "cve_id": "CVE-2025-12345",
                    "title": "Test Vulnerability",
                    "description": "A test vulnerability",
                    "severity": "High",
                    "cvss_score": 8.5,
                    "published_date": "2025-01-15",
                    "modified_date": "2025-01-20",
                    "references": ["https://example.com"],
                    "affected_products": ["Test Product"],
                }
            ]
        }
        mock_request.return_value = mock_response

        action = GetCve()
        action.connection = MockConnection()
        action.logger = MagicMock()

        result = action.run({"cve_id": "CVE-2025-12345"})

        self.assertTrue(result["found"])
        self.assertEqual(result["cve"]["cve_id"], "CVE-2025-12345")

    @patch("komand_rapid7_intelhub.util.api.requests.request")
    def test_get_cve_not_found(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": []}
        mock_request.return_value = mock_response

        action = GetCve()
        action.connection = MockConnection()
        action.logger = MagicMock()

        result = action.run({"cve_id": "CVE-9999-99999"})

        self.assertFalse(result["found"])
