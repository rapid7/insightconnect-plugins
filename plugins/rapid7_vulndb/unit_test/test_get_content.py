import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_vulndb.actions.get_content import GetContent
from komand_rapid7_vulndb.actions.get_content.schema import GetContentInput, GetContentOutput, Input

from mock import mock_request


class TestGetContent(TestCase):
    def setUp(self) -> None:
        self.params = {
            "identifier": "3395856ce81f2b7382dee72602f798b642f14140-cve",
            "identifier_404": "4416967df92g3c8493eff83513g819c753g23241-cve",
            "identifier_504": "5527178eg13h4d9514egg94624h921d864h34352-cve",
        }
        self.params_list = [
            ("404", "4416967df92g3c8493eff83513g819c753g23241-cve", "The requested resource could not be found."),
            ("504", "5527178eg13h4d9514egg94624h921d864h34352-cve", "Server error occurred"),
        ]
        self.action = GetContent()

    @patch("requests.get", side_effect=mock_request)
    def test_get_content(self, mock_requests: MagicMock) -> None:

        input_data = {Input.IDENTIFIER: self.params.get("identifier")}
        validate(input_data, GetContentInput.schema)
        actual = self.action.run(input_data)
        expected = {
            "content_result": {
                "title": "test_title_1",
                "description": "\n    <p>test_description_1</p>\n  ",
                "references": "test_reference_1",
                "published_at": "2021-01-01T00:00:00.000Z",
                "content_type": "vulnerability",
                "solutions": "test_solution_1",
                "severity": "4",
                "alternate_ids": "CVE/2021-12345,DEBIAN/DSA-1234,URL/https://example.com.html",
            }
        }
        self.assertEqual(actual, expected)
        validate(actual, GetContentOutput.schema)
        mock_requests.assert_called()

    @patch("requests.get", side_effect=mock_request)
    def test_get_content_error(self, mock_requests: MagicMock) -> None:
        for error, identifier, expected in self.params_list:
            with self.assertRaises(PluginException) as exception:
                input_data = {Input.IDENTIFIER: identifier}
                validate(input_data, GetContentInput.schema)
                self.action.run(input_data)
            self.assertEqual(exception.exception.cause, expected)
        mock_requests.assert_called()
