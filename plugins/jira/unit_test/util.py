import logging
from collections import namedtuple
from unittest import TestCase

from komand_jira.connection import Connection


class MockIssue:
    def __init__(self):
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
    def permalink():
        return "https://example-demo.atlassian.net/browse/ISSUE-ID-1234"


class MockClient:
    def __init__(self):
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

    def projects(self):
        return self.project_object

    @staticmethod
    def search_issues(jql, startAt, maxResults, fields):
        return [MockIssue()]


class MockConnection:
    def __init__(self):
        self.client = MockClient()


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = MockConnection()
        action.logger = logging.getLogger("action logger")
        return action

    def check_error():
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

    def check_error_with_fields():
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
