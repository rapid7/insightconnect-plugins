import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.get_comments import GetComments
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_404

######################
# MOCKS
######################


class MockAuthor:
    def __init__(self, display_name: str = "Mia Krystof") -> None:
        self.displayName = display_name
        self.raw = {"displayName": display_name}


class MockComment:
    def __init__(self, comment_id: str = "10000", body: str = "Test comment") -> None:
        self.id = comment_id
        self.body = body
        self.author = MockAuthor("Mia Krystof")
        self.created = "2021-01-17T12:34:00.000+0000"
        self.updated = "2021-01-18T23:45:00.000+0000"
        self.raw = {
            "id": comment_id,
            "body": body,
            "author": {"displayName": "Mia Krystof"},
            "created": "2021-01-17T12:34:00.000+0000",
            "updated": "2021-01-18T23:45:00.000+0000",
        }


class MockIssue:
    def __init__(self, issue_id: str = "10002", issue_key: str = "ED-1") -> None:
        comments_list = [
            MockComment(comment_id="10000", body="First comment"),
            MockComment(comment_id="10001", body="Second comment"),
        ]

        fields_dict = {
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "summary": "Test issue summary",
            "comment": namedtuple("CommentContainer", ["comments"])(comments_list),
        }

        self.raw = {"fields": "something"}
        self.id = issue_id
        self.key = issue_key
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())


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


class TestGetComments(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = GetComments()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)
        self.assertIn("count", result)
        self.assertIsInstance(result["comments"], list)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_with_issue_key(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
        }

        self.test_action.connection = MockConnection(is_cloud=False)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)
        self.assertIn("count", result)

    def test_get_comments_invalid_issue_id(self) -> None:
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


class TestGetCommentsCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = GetComments()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_cloud(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)
        self.assertIn("count", result)
        self.assertIsInstance(result["comments"], list)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_cloud_with_issue_key(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)
        self.assertIn("count", result)

    @mock.patch("requests.Session.request", side_effect=mock_request_404)
    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_get_comments_cloud_invalid_issue(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_cloud_verify_count(self, mock_request: mock.Mock, mock_session_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("count", result)
        self.assertGreaterEqual(result["count"], 0)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_cloud_different_issue_id(
        self, mock_request: mock.Mock, mock_session_request: mock.Mock
    ) -> None:
        action_params = {
            "id": "10010",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_comments_cloud_verify_structure(
        self, mock_request: mock.Mock, mock_session_request: mock.Mock
    ) -> None:
        action_params = {
            "id": "10002",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("comments", result)
        self.assertIn("count", result)
        # Verify the count matches the number of comments
        self.assertEqual(result["count"], len(result["comments"]))
