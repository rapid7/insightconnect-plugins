import sys
import os

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.add_scan_result import AddScanResult
from icon_cisco_firepower_management_center.actions.add_scan_result.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.send", side_effect=Util.mock_send)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
class TestAddScanResult(TestCase):
    def test_add_scan_result(self, mock_connect, mock_write, mock_send, mock_recv, mock_post, mock_request):
        action = Util.default_connector(AddScanResult())
        actual = action.run(
            {
                Input.SCAN_RESULT: {
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
                },
                Input.OPERATION: "ScanUpdate",
            }
        )
        expected = {"errors": 0, "commands_processed": 4}
        self.assertEqual(actual, expected)

    def test_add_scan_result_bad(self, mock_connect, mock_write, mock_send, mock_recv, mock_post, mock_request):
        action = Util.default_connector(AddScanResult())
        with self.assertRaises(PluginException) as error:
            action.run(
                {
                    Input.SCAN_RESULT: {
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
                    },
                    Input.OPERATION: "ScanUpdate",
                }
            )
        self.assertEqual(error.exception.cause, "The provided IP address 999.999.999.999 is invalid.")
        self.assertEqual(error.exception.assistance, "Please provide a valid IP address for the host and try again.")
