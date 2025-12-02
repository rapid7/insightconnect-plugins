import logging
from collections import namedtuple
from typing import Any, Dict, List, Union
from unittest import TestCase

from insightconnect_plugin_runtime.action import Action
from insightconnect_plugin_runtime.trigger import Trigger
from komand_jira.connection import Connection


class MockIssue:
    def __init__(self) -> None:
        fields_dict = {
            "resolution": namedtuple("AnObject", ["name"])(["new years"]),
            "reporter": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "assignee": namedtuple("AnObject", ["displayName"])(["Bob Smith"]),
            "resolutiondate": "No idea what this is",
            "description": "A description",
            "summary": "A summary",
            "status": namedtuple("AnObject", ["name"])(["In Progress"]),
            "created": "15 minutes ago",
            "updated": "15 minutes ago",
            "labels": ["blocked"],
        }

        self.raw = {"fields": "something"}
        self.id = "12345"
        self.key = "12345"
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    @staticmethod
    def permalink() -> str:
        return "https://example-demo.atlassian.net/browse/ISSUE-ID-1234"


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"
        project = {
            "raw": {},
            "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
            "self": "https://example.atlassian.net/rest/api/2/project/12345",
            "id": "12345",
            "key": "projectKey",
            "name": "projectName",
            "avatarUrls": {},
            "entityId": "12345-12345-12345-12345",
            "uuid": "12345-12345-12345-12345",
        }
        self.project_object = [namedtuple("ObjectName", project.keys())(*project.values())]

    def projects(self) -> List[Any]:
        return self.project_object

    @staticmethod
    def search_issues(jql: str, startAt: int, maxResults: int, fields: str) -> List[MockIssue]:
        return [MockIssue()]

    @staticmethod
    def issue(id: str) -> MockIssue:
        return MockIssue()


class MockConnection:
    def __init__(self, is_cloud: bool = False) -> None:
        from komand_jira.util.api import JiraApi

        self.client = MockClient()
        # Use real JiraApi - requests.request will be mocked in tests
        self.rest_client = JiraApi(
            base_url="https://your-domain.atlassian.net",
            authorization={"Authorization": "Bearer fake_token"},
            logger=logging.getLogger("test"),
        )
        self.is_cloud = is_cloud


class MockTrigger:
    actual = None

    @staticmethod
    def send(params: Dict[str, Any]) -> None:
        MockTrigger.actual = params


class Util:
    @staticmethod
    def default_connector(action: Union[Action, Trigger]) -> Union[Action, Trigger]:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = MockConnection()
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def check_error() -> bool:
        expected = {
            "issue": {
                "attachments": [],
                "id": "12345",
                "key": "12345",
                "url": "https://example-demo.atlassian.net/browse/ISSUE-ID-1234",
                "summary": "A summary",
                "description": "A description",
                "status": ["In Progress"],
                "resolution": ["new years"],
                "reporter": ["Bob Smith"],
                "assignee": ["Bob Smith"],
                "created_at": "15 minutes ago",
                "updated_at": "15 minutes ago",
                "resolved_at": "No idea what this is",
                "labels": ["blocked"],
            }
        }
        if MockTrigger.actual == expected:
            return True

        TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)
        return False

    @staticmethod
    def check_error_with_fields() -> bool:
        expected = {
            "issue": {
                "attachments": [],
                "id": "12345",
                "key": "12345",
                "url": "https://example-demo.atlassian.net/browse/ISSUE-ID-1234",
                "summary": "A summary",
                "description": "A description",
                "status": ["In Progress"],
                "resolution": ["new years"],
                "reporter": ["Bob Smith"],
                "assignee": ["Bob Smith"],
                "created_at": "15 minutes ago",
                "updated_at": "15 minutes ago",
                "resolved_at": "No idea what this is",
                "labels": ["blocked"],
                "fields": "something",
            }
        }
        if MockTrigger.actual == expected:
            return True

        TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)
        return False
