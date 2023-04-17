import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from unit_test.util import Util
from komand_rapid7_insightvm.actions.generate_adhoc_sql_report import GenerateAdhocSqlReport
from komand_rapid7_insightvm.actions.generate_adhoc_sql_report.schema import Input
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

class MockResponse:
    def __init__(self, json_data, text, status_code=200):
        self.json_data = json_data
        self.text = ""
        self.status_code = status_code

    def json(self):
        return self.json_data

class TestGenerateAdhocSqlReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GenerateAdhocSqlReport())
        logging.basicConfig(level=logging.ERROR)

    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.delete", side_effect=Util.mocked_requests)
    def test_generate_report(self, mock_post, mock_get, mock_delete):
        actual = self.action.run(
            {
                Input.QUERY: "SELECT * FROM dim_asset",
                Input.SCOPE: "none",
                Input.FILTERS: """{"filter": "none"}""",
                Input.SCOPE_IDS: [1234, 5678]
            }
        )
        expected = {'report': {'content': 'InN0cmluZyI=', 'filename': 'adhoc_sql_report.csv'}}
        self.assertEqual(actual, expected)

    @patch("requests.sessions.Session.post")
    def test_generate_report_no_report_id(self, mock_post):
        with self.assertRaises(PluginException) as e:
            mock_post.return_value = Mock(status_code=200, json=lambda: {"no_id": 1})
            self.action.run(
                {
                    Input.QUERY: "SELECT * FROM dim_asset",
                    Input.SCOPE: "none",
                    Input.FILTERS: """{"filter": "none"}""",
                    Input.SCOPE_IDS: [1234, 5678]
                }
            )
        self.assertEqual(e.exception.cause, "Error: Failed to create report, report ID was not returned with create request")
        self.assertEqual(e.exception.assistance, "Review InsightVM console logs and try again.")

    @patch("requests.sessions.Session.post", side_effect=[Mock(status_code=200, json=lambda: {"id": 1}), Mock(status_code=200, json=lambda: {"no_id": 1})])
    def test_generate_report_no_report_instance_id(self, mock_post):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.QUERY: "SELECT * FROM dim_asset",
                    Input.SCOPE: "none",
                    Input.FILTERS: """{"filter": "none"}""",
                    Input.SCOPE_IDS: [1234, 5678]
                }
            )
        self.assertEqual(e.exception.cause, "Error: Failed to generate report, report instance ID was not returned with generate request.")
        self.assertEqual(e.exception.assistance, "Review the report configuration and InsightVM console logs; then try again.")

    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.get", side_effect=[Mock(status_code=200, json=lambda: {"status": "aborted"}), Mock(status_code=200, json=lambda: {"status": "aborted"})])
    def test_generate_report_status_failed(self, mock_post, mock_get):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.QUERY: "SELECT * FROM dim_asset",
                    Input.SCOPE: "none",
                    Input.FILTERS: """{"filter": "none"}""",
                    Input.SCOPE_IDS: [1234, 5678]
                }
            )
        self.assertEqual(e.exception.cause, "Error: Report failed to generated with status aborted.")
        self.assertEqual(e.exception.assistance, "Review the report configuration and InsightVM logs prior to trying "
                                                 "again.")

    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.get", side_effect=[Mock(status_code=200, json=lambda: {"status": "complete"}), Mock(status_code=404, text='{"message:": "An error has occurred."}', json={"message:": "An error has occurred."})])
    def test_generate_report_download_failed(self, mock_post, mock_get):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.QUERY: "SELECT * FROM dim_asset",
                    Input.SCOPE: "none",
                    Input.FILTERS: """{"filter": "none"}""",
                    Input.SCOPE_IDS: [1234, 5678]
                }
            )
        self.assertEqual(e.exception.cause, "InsightVM returned an error message. Not Found")
        self.assertEqual(e.exception.assistance, "Ensure that the requested resource exists.")

    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.delete", side_effect=[Mock(status_code=404, text='{"message:": "An error has occurred."}', json={"message:": "An error has occurred."})])
    def test_generate_report_delete_failed(self, mock_post, mock_get, mock_delete):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.QUERY: "SELECT * FROM dim_asset",
                    Input.SCOPE: "none",
                    Input.FILTERS: """{"filter": "none"}""",
                    Input.SCOPE_IDS: [1234, 5678]
                }
            )
        self.assertEqual(e.exception.cause, "InsightVM returned an error message. Not Found")
        self.assertEqual(e.exception.assistance, "Ensure that the requested resource exists.")
