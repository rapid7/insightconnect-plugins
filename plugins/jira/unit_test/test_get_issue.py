import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.get_issue import GetIssue
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_404

######################
# MOCKS
######################


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        fields_dict = {
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "reporter": namedtuple("Reporter", ["displayName"])("John Doe"),
            "summary": "Test issue summary",
            "description": "Test description",
            "status": namedtuple("Status", ["name"])("Open"),
            "priority": namedtuple("Priority", ["name"])("High"),
            "resolution": None,
            "resolutiondate": None,
            "created": "2021-01-17T12:34:00.000+0000",
            "updated": "2021-01-18T23:45:00.000+0000",
            "comment": namedtuple("Comment", ["comments"])([]),
            "attachment": [],
            "labels": ["bug", "urgent"],
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
    def issue(id: str):
        if id == "INVALID":
            return None
        return MockIssue(issue_id=id)


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


class TestGetIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = GetIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("found", result)
        self.assertIn("issue", result)
        self.assertTrue(result["found"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_with_issue_key(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])
        self.assertIsNotNone(result["issue"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_with_attachments(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "get_attachments": True,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])

    def test_get_issue_invalid_issue_id(self) -> None:
        action_params = {
            "id": "INVALID",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("No issue found", str(context.exception))


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestGetIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = GetIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("found", result)
        self.assertIn("issue", result)
        self.assertTrue(result["found"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud_with_issue_key(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud_with_attachments(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "get_attachments": True,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_get_issue_cloud_invalid_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud_verify_structure(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("found", result)
        self.assertIn("issue", result)
        self.assertTrue(result["found"])
        self.assertIsNotNone(result["issue"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud_numeric_id(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10005",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_issue_cloud_without_attachments(
        self, mock_session_request: mock.Mock, mock_request: mock.Mock
    ) -> None:
        action_params = {
            "id": "10002",
            "get_attachments": False,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["found"])
