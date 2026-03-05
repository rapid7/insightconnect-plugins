import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.label_issue import LabelIssue
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_404

######################
# MOCKS
######################


class MockFields:
    def __init__(self) -> None:
        self.assignee = namedtuple("AnObject", ["displayName"])(["Bob Smith"])
        self.summary = "Test issue summary"
        self.labels = ["existing-label"]


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        self.raw = {"fields": "something"}
        self.id = issue_id
        self.key = issue_key
        self.fields = MockFields()

    def update(self, fields=None) -> bool:
        if fields and "labels" in fields:
            self.fields.labels = fields["labels"]
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


class TestLabelIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = LabelIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_single_label(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "bug",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_multiple_labels(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "bug,urgent,security",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_with_issue_key(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
            "label": "enhancement",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    def test_label_issue_invalid_issue_id(self) -> None:
        action_params = {
            "id": "INVALID",
            "label": "bug",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        # Should raise exception about invalid issue
        self.assertTrue("No issue found" in str(context.exception) or "INVALID" in str(context.exception))


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestLabelIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = LabelIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_single_label(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "bug",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_multiple_labels(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "bug,urgent,security",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_with_issue_key(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
            "label": "enhancement",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_label_issue_cloud_invalid_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
            "label": "bug",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_with_hyphens(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "needs-review,high-priority",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_with_underscores(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "tech_debt,code_review",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_many_labels(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "label1,label2,label3,label4,label5",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_label_issue_cloud_numeric_label(self, mock_session_request: mock.Mock, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "label": "v1.0,release-2024",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])
