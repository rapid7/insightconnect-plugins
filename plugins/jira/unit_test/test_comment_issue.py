import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from typing import Optional
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.comment_issue import CommentIssue
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_404

######################
# MOCKS
######################


class MockComment:
    def __init__(self, comment_id: str = "10000") -> None:
        self.id = comment_id
        self.body = "This is a test comment"
        self.author = namedtuple("Author", ["displayName"])("Mia Krystof")


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        fields_dict = {
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "summary": "Test issue summary",
        }

        self.raw = {"fields": "something"}
        self.id = issue_id
        self.key = issue_key
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    @staticmethod
    def issue(id: str) -> Optional[MockIssue]:
        if id == "INVALID":
            return None
        return MockIssue(issue_id=id)

    @staticmethod
    def add_comment(issue: MockIssue, comment: str) -> MockComment:
        return MockComment()


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


class TestCommentIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = CommentIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "This is a test comment",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)
        self.assertIsNotNone(result["comment_id"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_with_long_comment(self, mock_request: mock.Mock) -> None:
        long_comment = "This is a very long comment. " * 50
        action_params = {
            "id": "ED-24",
            "comment": long_comment,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_with_special_characters(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Comment with special chars: @#$%^&*()!",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_with_multiline(self, mock_request: mock.Mock) -> None:
        multiline_comment = """This is a multiline comment.
Line 2 of the comment.
Line 3 of the comment."""
        action_params = {
            "id": "10002",
            "comment": multiline_comment,
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    def test_comment_issue_invalid_issue_id(self) -> None:
        action_params = {
            "id": "INVALID",
            "comment": "Test comment",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("No issue found", str(context.exception))


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestCommentIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = CommentIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "This is a test comment",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)
        self.assertEqual(result["comment_id"], "10000")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_issue_key(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
            "comment": "Test comment with issue key",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_mentions(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Hey @testuser, please review this issue",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_markdown_style(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "# Header\n**bold text** and *italic text*\n- bullet point",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_code_block(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Here is some code:\n```python\nprint('Hello World')\n```",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_emoji(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Great work! 👍 🎉",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_url(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Check this out: https://example.com",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_comment_issue_cloud_invalid_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
            "comment": "Test comment",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_empty_comment(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_very_long_comment(self, mock_request: mock.Mock) -> None:
        very_long_comment = "A" * 10000
        action_params = {
            "id": "10002",
            "comment": very_long_comment,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_comment_issue_cloud_with_unicode(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "comment": "Unicode characters: 你好 مرحبا שלום",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comment_id", result)
