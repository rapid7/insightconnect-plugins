import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from typing import Optional
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.attach_issue import AttachIssue
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


######################
# Tests - Non-Cloud Mode (is_cloud=False)
######################


class TestAttachIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = AttachIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

        # Sample test file content (base64 encoded "Hello, World!")
        self.sample_file_content = base64.b64encode(b"Hello, World!").decode("utf-8")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "test.txt",
            "attachment_bytes": self.sample_file_content,
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)
        self.assertIsNotNone(result["id"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_with_image(self, mock_request: mock.Mock) -> None:
        # Create a simple base64 encoded image-like content
        image_content = base64.b64encode(b"\x89PNG\r\n\x1a\n test image content").decode("utf-8")
        action_params = {
            "id": "ED-24",
            "attachment_filename": "screenshot.png",
            "attachment_bytes": image_content,
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_with_different_extension(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "logfile.log",
            "attachment_bytes": self.sample_file_content,
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    def test_attach_issue_invalid_issue_id(self) -> None:
        action_params = {
            "id": "INVALID",
            "attachment_filename": "test.txt",
            "attachment_bytes": self.sample_file_content,
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("No issue found", str(context.exception))

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_invalid_base64(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "test.txt",
            "attachment_bytes": "invalid_base64!!!",
        }

        mock_conn = MockConnection(is_cloud=False)
        mock_conn.client = MockClient()
        self.test_action.connection = mock_conn
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("Unable to decode attachment bytes", str(context.exception))


######################
# Cloud Mode Tests (is_cloud=True) - Using REST Client
######################


class TestAttachIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = AttachIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

        # Sample test file content (base64 encoded "Hello, World!")
        self.sample_file_content = base64.b64encode(b"Hello, World!").decode("utf-8")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "test.txt",
            "attachment_bytes": self.sample_file_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)
        self.assertIsNotNone(result["id"])

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_with_pdf(self, mock_request: mock.Mock) -> None:
        pdf_content = base64.b64encode(b"%PDF-1.4 test pdf content").decode("utf-8")
        action_params = {
            "id": "PROJ-123",
            "attachment_filename": "document.pdf",
            "attachment_bytes": pdf_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_with_issue_key(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "PROJ-456",
            "attachment_filename": "report.xlsx",
            "attachment_bytes": self.sample_file_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    @mock.patch("requests.request", side_effect=mock_request_404)
    def test_attach_issue_cloud_invalid_issue(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "INVALID-999",
            "attachment_filename": "test.txt",
            "attachment_bytes": self.sample_file_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_filename_with_special_chars(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "my-test_file (1).txt",
            "attachment_bytes": self.sample_file_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_large_filename(self, mock_request: mock.Mock) -> None:
        long_filename = "a" * 200 + ".txt"
        action_params = {
            "id": "10002",
            "attachment_filename": long_filename,
            "attachment_bytes": self.sample_file_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_invalid_base64(self, mock_request: mock.Mock) -> None:
        action_params = {
            "id": "10002",
            "attachment_filename": "test.txt",
            "attachment_bytes": "not_valid_base64@@@",
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(action_params)

        self.assertIn("Unable to decode attachment bytes", str(context.exception))

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_attach_issue_cloud_empty_file(self, mock_request: mock.Mock) -> None:
        empty_content = base64.b64encode(b"").decode("utf-8")
        action_params = {
            "id": "10002",
            "attachment_filename": "empty.txt",
            "attachment_bytes": empty_content,
        }

        self.test_action.connection = MockConnection(is_cloud=True)
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        self.assertIn("id", result)
