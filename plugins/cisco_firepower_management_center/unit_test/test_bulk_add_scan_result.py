import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_firepower_management_center.actions.bulk_add_scan_result import BulkAddScanResult
from icon_cisco_firepower_management_center.actions.bulk_add_scan_result.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestBulkAddScanResult(TestCase):
    def test_bulk_add_scan_result(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
    ) -> None:
        action = Util.default_connector(BulkAddScanResult())
        actual = action.run(
            {
                Input.SCAN_RESULTS: [
                    {
                        "host": {
                            "ip_address": "0.0.0.164",
                            "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"},
                        },
                        "scan_result_details": {
                            "description": "Example description",
                            "protocol_id": "6",
                            "scanner_id": "ProductZImport",
                            "source_id": "ProductZ",
                            "vulnerability_id": "943387",
                            "vulnerability_title": "Virus Wire 0",
                        },
                    }
                ],
                Input.OPERATION: "ScanUpdate",
            }
        )
        expected = {"errors": 0, "commands_processed": 4}
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()

    def test_bulk_add_scan_result_bad(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
    ) -> None:
        action = Util.default_connector(BulkAddScanResult())
        with self.assertRaises(PluginException) as error:
            action.run(
                {
                    Input.SCAN_RESULTS: [
                        {
                            "host": {
                                "ip_address": "999.999.999.999",
                                "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"},
                            },
                            "scan_result_details": {
                                "description": "Example description",
                                "protocol_id": "6",
                                "scanner_id": "ProductZImport",
                                "source_id": "ProductZ",
                                "vulnerability_id": "943387",
                                "vulnerability_title": "Virus Wire 0",
                            },
                        }
                    ],
                    Input.OPERATION: "ScanUpdate",
                }
            )
        self.assertEqual(error.exception.cause, "The provided IP address 999.999.999.999 is invalid.")
        self.assertEqual(error.exception.assistance, "Please provide a valid IP address for the host and try again.")
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()
