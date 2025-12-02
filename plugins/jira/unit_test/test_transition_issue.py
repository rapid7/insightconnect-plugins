import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jira.exceptions import JIRAError
from komand_jira.actions.transition_issue import TransitionIssue
from komand_jira.connection import Connection


class MockIssue:
    def __init__(self, id) -> None:
        fields_dict = {
            "resolution": namedtuple("AnObject", ["name"])(["new years"]),
            "reporter": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "resolutiondate": "No idea what this is",
            "description": "A description",
            "summary": "A summary",
            "status": namedtuple("AnObject", ["name"])(["In Progress"]),
            "created": "Yesterday",
            "updated": "Yesterday",
            "labels": ["blocked"],
        }

        self.raw = {"fields": "something"}
        self.id = id
        self.key = "12345"
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    def permalink(self) -> str:
        return "https://example-demo.atlassian.net/browse/ISSUE-ID-1234"


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def issue(self, id):
        if id == "12345" or id == "10000":
            return MockIssue(id)
        else:
            return None

    def transition_issue(self, issue, transition, comment, fields) -> str:
        if issue.id == "12345":
            return "Success"
        raise JIRAError("Key error")


class TestTransitionIssue(TestCase):
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = TransitionIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    def test_transition_issue(self) -> None:
        action_params = {
            "id": "12345",
            "transition": "something",
            "comment": "this is a comment",
            "fields": ["some", "fields"],
        }

        self.test_conn.client = MockClient()
        self.test_action.connection = self.test_conn

        result = self.test_action.run(action_params)

        self.assertTrue(result.get("success"))

    def test_transition_issue_id_not_found(self) -> None:
        action_params = {
            "id": "NOT 12345",
        }

        self.test_conn.client = MockClient()
        self.test_action.connection = self.test_conn

        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    def test_transition_issue_id_throws_key_error(self) -> None:
        action_params = {
            "id": "10000",
            "transition": "something",
            "comment": "this is a comment",
            "fields": ["some", "fields"],
        }

        self.test_conn.client = MockClient()
        self.test_action.connection = self.test_conn

        with self.assertRaises(PluginException) as e:
            self.test_action.run(action_params)

        self.assertIn("Key error", e.exception.cause)
