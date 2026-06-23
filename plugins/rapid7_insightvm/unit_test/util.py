import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from pathlib import Path
from typing import Any
from unittest import TestCase

from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.connection.schema import Input

BASE_DIR = Path(__file__).resolve().parent


class Util:
    _response_cache = {}

    @staticmethod
    def preload_responses(filenames):
        for filename in filenames:
            filepath = os.path.join(str(BASE_DIR), f"payloads/{filename}.json.resp")
            Util._response_cache[filename] = Util.read_file_to_string(filepath)

    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://example.com",
            Input.CREDENTIALS: {"password": "password", "username": "user"},
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(os.path.join(str(BASE_DIR), filename)))

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code, is_csv=False) -> None:
                self.filename = filename
                self.status_code = status_code
                self.is_csv = is_csv
                if filename in Util._response_cache:
                    self.text = Util._response_cache[filename]
                else:
                    self.text = self.load_data()

            def load_data(self):
                return Util.read_file_to_string(os.path.join(str(BASE_DIR), f"payloads/{self.filename}.json.resp"))

            def json(self):
                if self.is_csv:
                    return {"raw": self.text}
                return json.loads(self.text)

            def raise_for_status(self):
                if 200 <= self.status_code <= 300:
                    pass
                else:
                    raise Exception("Error")

        if kwargs.get("url") == "https://example.com/api/3/sites/100/scans":
            return MockResponse("scan_invalid_site_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/sites/1/scans":
            if kwargs.get("json") == {"hosts": ["198.51.100.1"]}:
                return MockResponse("scan1", 200)
            if kwargs.get("params") == [("overrideBlackout", False)]:
                return MockResponse("scan1", 200)
            if kwargs.get("params") == [("overrideBlackout", True)]:
                return MockResponse("scan2", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports?page=0&size=10&sort=ASC":
            return MockResponse("list_reports", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports?page=1&size=10&sort=ASC":
            return MockResponse("list_reports_2", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/1":
            return MockResponse("get_asset", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/2":
            return MockResponse("get_asset_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/assets/3":
            return MockResponse("delete_asset", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/4":
            return MockResponse("delete_asset_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/assets/5/software":
            return MockResponse("get_asset_software", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/6/software":
            return MockResponse("get_asset_software_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/assets/7/vulnerabilities":
            return MockResponse("get_asset_vulnerabilities", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/8/vulnerabilities":
            return MockResponse("get_asset_vulnerabilities_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/sites/1/excluded_targets":
            return MockResponse("get_site_excluded_targets", 200)
        if kwargs.get("url") == "https://example.com/api/3/sites/2/excluded_targets":
            return MockResponse("get_site_excluded_targets_no_addresses", 200)
        if kwargs.get("url") == "https://example.com/api/3/sites/1/included_targets":
            return MockResponse("get_site_included_targets", 200)
        if kwargs.get("url") == "https://example.com/api/3/sites/2/included_targets":
            return MockResponse("get_site_included_targets_no_addresses", 200)
        if kwargs.get("url") == "https://example.com/api/2.0/tags/1":
            if kwargs.get("json") == {
                "attributes": [{"tag_attribute_name": "SOURCE", "tag_attribute_value": "CUSTOM"}],
                "tag_name": "Example Tag",
                "tag_config": {"tag_associated_asset_ids": [1, 2, 3]},
                "tag_type": "Criticality",
            }:
                return MockResponse("tag_assets_bad_type", 405)
            if kwargs.get("json") == {
                "attributes": [{"tag_attribute_name": "SOURCE", "tag_attribute_value": "VM"}],
                "tag_name": "Example Tag",
                "tag_config": {"tag_associated_asset_ids": [1, 2, 3]},
                "tag_type": "Custom",
            }:
                return MockResponse("tag_assets_bad_source", 409)
            if kwargs.get("json") == {
                "attributes": [{"tag_attribute_name": "SOURCE", "tag_attribute_value": "CUSTOM"}],
                "tag_name": "Example Tag",
                "tag_config": {"tag_associated_asset_ids": [4, 5, 6]},
                "tag_type": "Custom",
            }:
                return MockResponse("tag_assets_bad_asset_ids", 500)
            return MockResponse("tag_assets", 200)
        if kwargs.get("url") == "https://example.com/api/2.0/tags/2":
            return MockResponse("tag_assets_bad_id", 404)
        if kwargs.get("url") == "https://example.com/api/getscandetails":
            return MockResponse("test_get_scan_details_endpoint", 200)
        if kwargs.get("json") == {
            "filters": [{"field": "last-scan-date", "operator": "is-earlier-than", "value": 30}],
            "match": "all",
        }:
            return MockResponse("list_inactive_assets", 200)
        if kwargs.get("json") == {
            "filters": [{"field": "last-scan-date", "operator": "is-earlier-than", "value": 10}],
            "match": "all",
        }:
            return MockResponse("list_inactive_assets_not_found", 200)
        if kwargs.get("json") == "2022-01-01T00:00:00.000000Z":
            return MockResponse("update_vulnerability_exception_expiration_date", 200)
        if kwargs.get("json") == "2022-01-10T00:00:00.000000Z":
            return MockResponse("update_vulnerability_exception_expiration_date_invalid_id", 404)
        if kwargs.get("json", {}).get("scope", {}).get("vulnerability") == "test_vulnerability":
            return MockResponse("create_exception", 200)
        if kwargs.get("params") == [("sort", "expires,ASC")]:
            return MockResponse("get_expiring_vulnerability_exceptions", 200)
        if kwargs.get("url") == "https://example.com/api/3/shared_credentials/1":
            return MockResponse("update_shared_credential_valid", 200)
        if kwargs.get("url") == "https://example.com/api/3/shared_credentials/2":
            return MockResponse("update_shared_credential_error", 400)
        if kwargs.get("url") == "https://example.com/api/3/reports":
            json_payload = kwargs.get("json", {})
            if isinstance(json_payload, dict) and json_payload.get("format") == "sql-query":
                # Scan completion uses scope.scan, generate_adhoc_sql_report uses scope.site or no scope
                if json_payload.get("scope", {}).get("scan"):
                    return MockResponse("scan_completion_create_report", 200)
            return MockResponse("generate_adhoc_sql_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/1/generate":
            return MockResponse("create_adhoc_sql_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/1/history/1":
            return MockResponse("status_adhoc_sql_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/1/history/1/output":
            return MockResponse("download_adhoc_sql_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/1":
            return MockResponse("delete_adhoc_sql_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/100/generate":
            return MockResponse("scan_completion_generate_report", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/100/history/1":
            return MockResponse("scan_completion_report_status", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/100/history/1/output":
            return MockResponse("scan_completion_report_output", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports/100":
            return MockResponse("delete_adhoc_sql_report", 200)

        url = kwargs.get("url", "")

        # Scan completion test scenarios
        if kwargs.get("url") == "https://example.com/api/3/sites/2/scans":
            return MockResponse("scan_completion_scans_with_missing_ids", 200)
        if kwargs.get("url") == "https://example.com/api/3/sites/3/scans":
            return MockResponse("scan_completion_mixed_scan_types", 200)

        # Only agent scans (no reportable baseline)
        if kwargs.get("url") == "https://example.com/api/3/sites/4/scans":
            return MockResponse("scan_completion_only_agent_scans", 200)

        # Multiple new scans scenario (IDs: 127, 126, 125, 124)
        if kwargs.get("url") == "https://example.com/api/3/sites/5/scans":
            return MockResponse("scan_completion_multiple_new_scans", 200)

        # Pagination boundary scenario (IDs: 128, 127, 126, 125, 124, 123)
        if kwargs.get("url") == "https://example.com/api/3/sites/6/scans":
            return MockResponse("scan_completion_pagination_boundary", 200)

        # No new scans scenario (IDs: 124, 123, 122 - all <= last_seen_scan_id)
        if kwargs.get("url") == "https://example.com/api/3/sites/7/scans":
            return MockResponse("scan_completion_no_new_scans", 200)

        # Failure mock for exception testing: site_id=999 triggers 500 error
        if kwargs.get("url") == "https://example.com/api/3/sites/999/scans":
            return MockResponse("error_response", 500)

        if "/api/3/sites/" in url and "/scans" in url:
            if not hasattr(Util, "_scan_call_count"):
                Util._scan_call_count = 0
            Util._scan_call_count += 1
            if Util._scan_call_count <= 1:
                return MockResponse("scan_completion_list_scans", 200)
            return MockResponse("scan_completion_new_scans", 200)
        if "/api/3/scans" in url and "/history/" not in url and "/output" not in url and "/generate" not in url:
            if not hasattr(Util, "_scan_call_count"):
                Util._scan_call_count = 0
            Util._scan_call_count += 1
            if Util._scan_call_count <= 1:
                return MockResponse("scan_completion_list_scans", 200)
            return MockResponse("scan_completion_new_scans", 200)

        # Failure mock for exception testing: site_id=999 triggers 500 error
        if kwargs.get("url") == "https://example.com/api/3/sites/999/scans":
            return MockResponse("error_response", 500)

        raise Exception(f"Not implemented: {url} with method {kwargs.get('method', 'GET')}")

    @staticmethod
    async def mocked_async_requests(*args, **kwargs):
        class MockAsyncResponse:
            def __init__(self, filename, status_code) -> None:
                self.filename = filename
                self.status = status_code
                self.response_text = ""

            async def text(self):
                self.response_text = self.load_data()
                return self.response_text

            def load_data(self):
                return Util.read_file_to_string(os.path.join(str(BASE_DIR), f"payloads/{self.filename}.json.resp"))

            async def json(self):
                return json.loads(self.response_text)

        if kwargs.get("url") == "https://example.com/api/3/assets/9/vulnerabilities/ssl-cve-2011-3389-beast/solution":
            return MockAsyncResponse("asset_vulnerability_solution", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/10/vulnerabilities/sl-ve-211-339-beast/solution":
            return MockAsyncResponse("asset_vulnerability_solution_invalid_vulnerability_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/assets/11/vulnerabilities/ssl-cve-2011-3389-beast/solution":
            return MockAsyncResponse("asset_vulnerability_solution_invalid_asset_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/vulnerabilities/certificate-common-name-mismatch":
            return MockAsyncResponse("get_asset_vulnerabilities_with_risk_score", 200)


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


class ErrorChecker:
    expected = {}

    @staticmethod
    def set_expected(expected):
        ErrorChecker.expected = expected

    @staticmethod
    def check_error():
        if MockTrigger.actual == ErrorChecker.expected:
            return True
        TestCase.assertDictEqual(TestCase(), MockTrigger.actual, ErrorChecker.expected)


class TriggerSentException(Exception):
    pass


class TriggerCapture:
    actual: dict[str, Any] = {}

    @staticmethod
    def reset() -> None:
        TriggerCapture.actual = {}

    @staticmethod
    def send(parameters: dict[str, Any]) -> None:
        TriggerCapture.actual.update(parameters)
        raise TriggerSentException()
