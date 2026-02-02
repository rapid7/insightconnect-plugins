import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.generate_adhoc_sql_report import GenerateAdhocSqlReport
from komand_rapid7_insightvm.actions.generate_adhoc_sql_report.schema import Input
from parameterized import parameterized

from util import Util

sys.path.append(os.path.abspath("../"))


class MockResponses:
    mock_responses = {
        "no_id": {"status_code": 200, "json": lambda: {"no_id": 1}},
        "return_id": {"status_code": 200, "json": lambda: {"id": 1}},
        "aborted": {
            "status_code": 200,
            "json": lambda: {"status": "aborted"},
        },
        "complete": {"status_code": 200, "json": lambda: {"status": "complete"}},
        "404": {
            "status_code": 404,
            "json": lambda: {"message:": "An error has occurred."},
            "text": '{"message:": "An error has occurred."}',
        },
        "401": {
            "status_code": 401,
            "json": lambda: {"message:": "An error has occurred."},
            "text": '{"message:": "An error has occurred."}',
        },
        "500": {
            "status_code": 500,
            "json": lambda: {"message:": "An error has occurred."},
            "text": '{"message:": "An error has occurred."}',
        },
        "503": {
            "status_code": 503,
            "json": lambda: {"message:": "An error has occurred."},
            "text": '{"message:": "An error has occurred."}',
        },
    }


class TestGenerateAdhocSqlReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GenerateAdhocSqlReport())
        cls.query = {
            Input.QUERY: "SELECT * FROM dim_asset",
            Input.SCOPE: "none",
            Input.FILTERS: """{"filter": "none"}""",
            Input.SCOPE_IDS: [1234, 5678],
        }

    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    @patch("requests.sessions.Session.delete", side_effect=Util.mocked_requests)
    def test_generate_report(self, mock_post, mock_get, mock_delete) -> None:
        actual = self.action.run(self.query)
        expected = {"report": {"content": "InN0cmluZyI=", "filename": "adhoc_sql_report.csv"}}
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "no_report_id",
                [Mock(**MockResponses.mock_responses["no_id"])],
                Util.mocked_requests,
                Util.mocked_requests,
                "Error: Failed to create report, report ID was not returned with create request",
                "Review InsightVM console logs and try again.",
            ],
            [
                "no_report_instance_id",
                [Mock(**MockResponses.mock_responses["return_id"]), Mock(**MockResponses.mock_responses["no_id"])],
                Util.mocked_requests,
                Util.mocked_requests,
                "Error: Failed to generate report, report instance ID was not returned with generate request.",
                "Review the report configuration and InsightVM console logs; then try again.",
            ],
            [
                "download_failed_401",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["complete"]), Mock(**MockResponses.mock_responses["401"])],
                "InsightVM returned an error message. Unauthorized",
                "Ensure that the user name and password are correct.",
            ],
            [
                "download_failed_404",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["complete"]), Mock(**MockResponses.mock_responses["404"])],
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
            ],
            [
                "download_failed_500",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["complete"]), Mock(**MockResponses.mock_responses["500"])],
                "InsightVM returned an error message. Internal Server Error",
                "If this issue persists contact support for assistance.",
            ],
            [
                "download_failed_503",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["complete"]), Mock(**MockResponses.mock_responses["503"])],
                "InsightVM returned an error message. Service Unavailable",
                "If this issue persists contact support for assistance.",
            ],
            [
                "delete_failed",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["complete"]), Mock(**MockResponses.mock_responses["404"])],
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
            ],
            [
                "status_aborted",
                Util.mocked_requests,
                Util.mocked_requests,
                [Mock(**MockResponses.mock_responses["aborted"]), Mock(**MockResponses.mock_responses["aborted"])],
                "Error: Report failed to generated with status aborted.",
                "Review the report configuration and InsightVM logs prior to trying again.",
            ],
        ]
    )
    @patch("requests.sessions.Session.get")
    @patch("requests.sessions.Session.delete")
    @patch("requests.sessions.Session.post")
    def test_generate_report_bad(
        self, name, post_response, get_response, delete_response, cause, assistance, mock_post, mock_get, mock_delete
    ) -> None:
        with self.assertRaises(PluginException) as e:
            mock_post.side_effect = post_response
            mock_get.side_effect = get_response
            mock_delete.side_effect = delete_response
            self.action.run(self.query)
        self.assertEqual(cause, e.exception.cause)
        self.assertEqual(assistance, e.exception.assistance)
