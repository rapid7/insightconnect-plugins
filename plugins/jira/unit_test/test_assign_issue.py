import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from typing import Optional
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.assign_issue import AssignIssue
from komand_jira.connection import Connection

from jira_mocks import mock_request_200, mock_request_404
from util import MockConnection

######################
# MOCKS
######################


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
    def assign_issue(issue: MockIssue, assignee: str) -> bool:
        return True


######################
# Tests - Non-Cloud Mode (is_cloud=False)
######################


class TestAssignIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = AssignIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "assignee": "testuser",
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue_with_different_user(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
            "assignee": "anotheruser",
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    def test_assign_issue_invalid_issue_id(self) -> None:
        action_params = {
            "id": "INVALID",
            "assignee": "testuser",
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("No issue found", str(context.exception))


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestAssignIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = AssignIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue_cloud(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "assignee": "testuser",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertTrue(result["success"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue_cloud_different_user(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "ED-24",
            "assignee": "anotheruser",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue_cloud_with_issue_key(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-123",
            "assignee": "testuser",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_assign_issue_cloud_invalid_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
            "assignee": "testuser",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_assign_issue_cloud_invalid_user(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "assignee": "nonexistentuser",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_assign_issue_cloud_username_with_special_chars(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "assignee": "test.user@example.com",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertTrue(result["success"])
