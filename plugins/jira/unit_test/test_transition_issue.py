import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
from collections import namedtuple
from typing import Any
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from jira.exceptions import JIRAError
from komand_jira.actions.transition_issue import TransitionIssue
from komand_jira.connection import Connection
from parameterized import param, parameterized

from jira_mocks import ADF_DOCUMENT, WIKI_MARKUP, get_request, get_urls, mock_request_200, text_as_adf
from util import MockConnection


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


class TestTransitionIssueCloud(TestCase):
    def setUp(self) -> None:
        self.test_action = TransitionIssue()
        self.test_action.logger = logging.getLogger("test")
        self.test_action.connection = MockConnection(is_cloud=True)

    @parameterized.expand(
        [
            param("wiki_markup", WIKI_MARKUP, {}, "/rest/api/2/", WIKI_MARKUP),
            param("json_not_adf", "42", {}, "/rest/api/2/", "42"),
            param("adf_document", json.dumps(ADF_DOCUMENT), {}, "/rest/api/3/", ADF_DOCUMENT),
            param(
                "adf_in_fields",
                WIKI_MARKUP,
                {"customfield_10010": ADF_DOCUMENT},
                "/rest/api/3/",
                text_as_adf(WIKI_MARKUP),
            ),
        ]
    )
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_transition_issue_cloud_api_version(
        self,
        name: str,
        comment: str,
        fields: dict[str, Any],
        api_path: str,
        expected_comment: Any,
        mock_request: mock.Mock,
    ) -> None:
        self.test_action.run({"id": "10002", "transition": "31", "comment": comment, "fields": dict(fields)})

        url, payload = get_request(mock_request, "POST")
        self.assertIn(api_path, url)
        self.assertEqual(expected_comment, payload["update"]["comment"][0]["add"]["body"])
        for get_url in get_urls(mock_request, "GET"):
            self.assertIn("/rest/api/3/", get_url)
