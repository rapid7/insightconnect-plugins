import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightvm.triggers.scan_completion import ScanCompletion
from komand_rapid7_insightvm.triggers.scan_completion.schema import Input, ScanCompletionInput
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from parameterized import parameterized

from util import TriggerCapture, TriggerSentException, Util

EXPECTED_SCAN_OUTPUT = {
    "scan_id": 124,
    "scan_completed_output": [
        {
            "ip_address": "192.168.1.1",
            "hostname": "test-host",
            "os": "Windows 10",
            "member_of_sites": ["site1"],
            "severity": "Critical",
            "riskscore": 850,
            "cvss_score": 9.8,
            "cvss_v3_score": 9.8,
            "exploits": 5,
            "malware_kits": 2,
            "vulnerability_id": 123456,
            "vulnerability_name": "Test Vulnerability",
            "vulnerability_details": "Test vulnerability details",
            "vulnerability_instances": 1,
            "vuln_first_published": "2022-01-01",
            "days_since_vuln_first_published": 500,
            "days_present_on_asset": 30,
            "date_first_seen_on_asset": "2024-01-15",
            "date_most_recently_seen_on_asset": "2024-01-15",
            "solution_id": 999,
            "nexpose_id": "nxp-001",
            "best_solution": "Apply security patch",
            "est_time_to_fix": "2 hours",
            "solution_type": "Vendor patch",
        }
    ],
}


class TestScanCompletion(TestCase):
    @classmethod
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.trigger = Util.default_connector(ScanCompletion())

    def setUp(self) -> None:
        TriggerCapture.reset()
        Util._scan_call_count = 0

    @parameterized.expand(
        [
            ("default_interval", {Input.INTERVAL: 5}, EXPECTED_SCAN_OUTPUT),
            ("with_site_id", {Input.INTERVAL: 5, Input.SITE_ID: "1"}, EXPECTED_SCAN_OUTPUT),
        ]
    )
    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=TriggerCapture.send)
    def test_scan_completion(
        self,
        test_name: str,
        input_params: dict,
        expected: dict,
        mock_send: MagicMock,
        mock_get: MagicMock,
        mock_post: MagicMock,
        mock_delete: MagicMock,
        mock_sleep: MagicMock,
    ) -> None:
        # Validate input parameters against schema
        validate(input_params, ScanCompletionInput.schema)

        # Run trigger and capture output
        try:
            self.trigger.run(input_params)
        except TriggerSentException:
            pass

        # Assert captured output matches expected result
        self.assertDictEqual(TriggerCapture.actual, expected)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    @patch("insightconnect_plugin_runtime.Trigger.send")
    def test_scan_completion_exception(
        self,
        mock_send: MagicMock,
        mock_get: MagicMock,
        mock_post: MagicMock,
        mock_delete: MagicMock,
        mock_sleep: MagicMock,
    ) -> None:
        # Assert that API error raises PluginException during scan list retrieval
        with self.assertRaises(PluginException) as context:
            self.trigger.run({Input.INTERVAL: 5, Input.SITE_ID: "999"})

        # Verify exception contains proper error information from the 500 response
        self.assertIn("Internal Server Error", context.exception.cause)
        self.assertIn("contact support", context.exception.assistance)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_skip_scans_with_missing_id(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # Scans with null ID should be skipped during filtering
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        Util._scan_call_count = 0
        scans = self.trigger.find_new_completed_scans(
            endpoint="https://example.com/api/3/sites/2/scans", last_seen_scan_id=None, resource_helper=resource_helper
        )

        # Should only find reportable scans (skipping null id)
        self.assertIn(125, scans)
        self.assertIn(124, scans)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_skip_agent_and_unfinished_scans(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # Only finished non-agent scans should be included in filtering
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        Util._scan_call_count = 0
        scans = self.trigger.find_new_completed_scans(
            endpoint="https://example.com/api/3/sites/3/scans", last_seen_scan_id=None, resource_helper=resource_helper
        )

        # Should only find finished regular scans (skip 126-running and 125-agent)
        self.assertIn(127, scans)
        self.assertIn(124, scans)
        self.assertNotIn(126, scans)
        self.assertNotIn(125, scans)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_first_poll_baseline_no_reportable_scans(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # When only agent scans exist, find_latest_completed_scan returns None (no baseline)
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        result = self.trigger.find_latest_completed_scan(
            endpoint="https://example.com/api/3/sites/4/scans", resource_helper=resource_helper
        )
        self.assertIsNone(result)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_first_poll_baseline_with_reportable_scan(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # When reportable scans exist, find_latest_completed_scan returns highest finished scan ID
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        result = self.trigger.find_latest_completed_scan(
            endpoint="https://example.com/api/3/sites/1/scans", resource_helper=resource_helper
        )
        self.assertEqual(result, 123)

    @patch("time.sleep")
    @patch(
        "requests.Session.get",
        side_effect=[
            requests.ConnectionError("Connection reset"),
            requests.ConnectionError("Connection reset"),
            MagicMock(
                status_code=200,
                text='{"page": {"number": 0, "size": 500, "totalPages": 1}, "resources": [{"id": 123, "status": "finished", "scanType": "regular"}]}',
                json=lambda: {
                    "page": {"number": 0, "size": 500, "totalPages": 1},
                    "resources": [{"id": 123, "status": "finished", "scanType": "regular"}],
                },
            ),
        ],
    )
    def test_scan_completion_retry_on_transient_connection_error(
        self, mock_get: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # Transient ConnectionError should be retried and succeed on 3rd attempt
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        result = self.trigger.find_latest_completed_scan(
            endpoint="https://example.com/api/3/sites/1/scans", resource_helper=resource_helper
        )

        # Should succeed after retries
        self.assertEqual(result, 123)

        # Verify retries happened (2 failures + 1 success = 3 calls)
        self.assertEqual(mock_get.call_count, 3)

    @patch("time.sleep")
    @patch(
        "requests.Session.get",
        side_effect=[
            requests.ConnectionError("Connection reset"),
            requests.ConnectionError("Connection reset"),
            requests.ConnectionError("Connection reset"),
            requests.ConnectionError("Connection reset"),
        ],
    )
    def test_scan_completion_retry_exhausted_raises_plugin_exception(
        self, mock_get: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # All retries exhausted should raise PluginException
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        with self.assertRaises(PluginException) as context:
            self.trigger.find_latest_completed_scan(
                endpoint="https://example.com/api/3/sites/1/scans", resource_helper=resource_helper
            )
        self.assertIn("Connection reset", context.exception.cause)

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_multiple_scans_ascending_order(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # Multiple new scans between polling intervals should be returned in ascending order
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        Util._scan_call_count = 0
        scans = self.trigger.find_new_completed_scans(
            endpoint="https://example.com/api/3/sites/5/scans", last_seen_scan_id=124, resource_helper=resource_helper
        )

        # Should find all scans > 124 in ascending order: [125, 126, 127]
        self.assertEqual(scans, [125, 126, 127])

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_pagination_boundary(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # Pagination should stop at scan_id <= last_seen_scan_id boundary
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        Util._scan_call_count = 0
        scans = self.trigger.find_new_completed_scans(
            endpoint="https://example.com/api/3/sites/6/scans", last_seen_scan_id=124, resource_helper=resource_helper
        )

        # Should return [125, 126, 127, 128] and NOT continue paginating through [123, 122]
        self.assertEqual(scans, [125, 126, 127, 128])

    @patch("time.sleep")
    @patch("requests.Session.delete", side_effect=Util.mocked_requests)
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_scan_completion_no_new_scans(
        self, mock_get: MagicMock, mock_post: MagicMock, mock_delete: MagicMock, mock_sleep: MagicMock
    ) -> None:
        # When all scans are <= last_seen_scan_id, should return empty list without emitting
        resource_helper = ResourceRequests(self.trigger.connection.session, self.trigger.logger, True)
        Util._scan_call_count = 0
        scans = self.trigger.find_new_completed_scans(
            endpoint="https://example.com/api/3/sites/7/scans", last_seen_scan_id=124, resource_helper=resource_helper
        )

        # All scans (124, 123, 122) are <= 124, so result should be empty
        self.assertEqual(scans, [])
