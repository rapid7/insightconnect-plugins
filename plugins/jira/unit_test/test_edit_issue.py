import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase, mock

from komand_jira.actions.edit_issue import EditIssue
from komand_jira.connection import Connection

from jira_mocks import mock_request_200

######################
# MOCKS
######################


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        fields_dict = {
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "summary": "Test issue summary",
            "description": "Test description",
            "labels": ["bug", "urgent"],
        }

        self.raw = {"fields": "something"}
        self.id = issue_id
        self.key = issue_key
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    def update(self, notify=True, **kwargs) -> bool:
        return True


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


class TestEditIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = EditIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_summary(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "Updated summary",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_description(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
            "description": "Updated description",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_multiple_fields(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "New summary",
            "description": "New description",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_notify_false(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "Updated summary",
            "notify": False,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestEditIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = EditIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "Updated summary",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_with_description(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
            "description": "Updated description with ADF conversion",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_multiple_fields(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "New summary",
            "description": "New description",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_notify_false(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "Updated summary",
            "notify": False,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_with_priority(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "priority": {"name": "High"},
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_with_labels(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "labels": ["bug", "urgent", "security"],
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_edit_issue_cloud_empty_fields(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "summary": "",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])
