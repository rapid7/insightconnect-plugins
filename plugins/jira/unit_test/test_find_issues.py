import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase, mock

from komand_jira.actions.find_issues import FindIssues
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_400

######################
# MOCKS
######################


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        fields_dict = {
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "reporter": namedtuple("Reporter", ["displayName"])("John Doe"),
            "summary": "Test issue summary",
            "status": namedtuple("Status", ["name"])("Open"),
            "resolution": None,
            "resolutiondate": None,
            "created": "2021-01-17T12:34:00.000+0000",
            "updated": "2021-01-18T23:45:00.000+0000",
            "comment": namedtuple("Comment", ["comments"])([]),
            "attachment": [],
            "labels": ["bug"],
            "description": "Test description",
        }

        self.raw = {"fields": fields_dict}
        self.id = issue_id
        self.key = issue_key
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    def permalink(self) -> str:
        return f"https://your-domain.atlassian.net/browse/{self.key} - {self.fields.summary}"


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    @staticmethod
    def search_issues(jql_str: str, maxResults: int):
        if "invalid" in jql_str.lower():
            return []
        return [
            MockIssue(issue_id="10002"),
            MockIssue(issue_id="10003", issue_key="ED-2"),
        ]


class MockConnection:
    def __init__(self, is_cloud: bool = False) -> None:
        import logging

        from komand_jira.util.api import JiraApi

        self.client = MockClient()
        # Use real JiraApi - requests.request will be mocked in tests
        self.rest_client = JiraApi(
            base_url="https://your-domain.atlassian.net",
            authorization={"Authorization": "Bearer fake_token"},
            logger=logging.getLogger("test"),
        )
        self.is_cloud = is_cloud


######################
# Tests - Non-Cloud Mode (is_cloud=False)
######################


class TestFindIssues(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = FindIssues()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "project = TEST",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)
        self.assertIsInstance(result["issues"], list)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_with_max_results(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "assignee = currentUser()",
            "max": 10,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_with_attachments(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "project = TEST",
            "max": 50,
            "get_attachments": True,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_complex_jql(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": 'project = TEST AND status = "In Progress" AND assignee = currentUser()',
            "max": 100,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestFindIssuesCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = FindIssues()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "project = TEST",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)
        self.assertIsInstance(result["issues"], list)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_with_status(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "status = Open",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_with_assignee(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "assignee = currentUser()",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_with_attachments(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "project = TEST",
            "max": 50,
            "get_attachments": True,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_max_results_limit(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "project = TEST",
            "max": 1,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_complex_jql(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": 'project = TEST AND status IN ("Open", "In Progress") ORDER BY created DESC',
            "max": 100,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)

    @mock.patch("requests.request", side_effect=mock_request_400)
    def test_find_issues_cloud_invalid_jql(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "invalid jql syntax here",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=True)

        # This should raise an exception due to invalid JQL
        from insightconnect_plugin_runtime.exceptions import PluginException

        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_find_issues_cloud_with_labels(self, mock_request: mock.Mock) -> None:
        action_params = {
            "jql": "labels = bug",
            "max": 50,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("issues", result)
