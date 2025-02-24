import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from collections import namedtuple
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.create_issue import CreateIssue
from komand_jira.connection import Connection

from payloads.client_fields import client_fields

######################
# MOCKS
######################

"""
This is a difficult test. The Jira API returns very big, very custom objects. To unit test the api
requires us to recreate those objects the best we can. Therefore there's a lot of mocks in this test

You'll see a lot of this: 

namedtuple("AnObject", ["name"])(["new years"]),

This will create a faux object that can be accessed like this: 

AnObject.name

That code can be used to quickly convert a dict to a fake object. 
"""


class MockRestClient:
    def add_attachment(self, key, filename, bytes):
        pass


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
            "created": "Yesterday",
            "updated": "Yesterday",
            "labels": ["blocked"],
        }

        self.raw = {"fields": "something"}
        self.id = "12345"
        self.key = "12345"
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    def permalink(self):
        return "https://example-demo.atlassian.net/browse/ISSUE-ID-1234"


class MockClient:
    def __init__(self):
        self.client = "some fake thing"

    def projects(self):
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

        # Need to convert this to an object to simulate the JiraObject return
        project_object = namedtuple("ObjectName", project.keys())(*project.values())

        return [project_object]

    def create_issue(self, fields):
        return MockIssue()

    def issue_types(self):
        issue_type = {
            "raw": {"name": "Task", "scope": {"type": "PROJECT", "project": {"id": "10000"}}, "id": "10001"},
            "name": "Task",
            "scope": {"type": "PROJECT", "project": {"id": "10000"}},
            "id": "10001",
        }
        issue_type_object = namedtuple("IssueType", issue_type.keys())(*issue_type.values())
        return [issue_type_object]

    def fields(self):
        return client_fields


class MockConnection:
    def __init__(self):
        self.client = MockClient()
        self.rest_client = MockRestClient()


######################
# Tests
######################


class TestCreateIssue(TestCase):
    def setUp(self):
        self.test_conn = Connection()
        self.test_action = CreateIssue()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    def test_create_issue(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": "A test description",
            "fields": {},
            "project": "projectName",
            "summary": "test Summary",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
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
                "created_at": "Yesterday",
                "updated_at": "Yesterday",
                "resolved_at": "No idea what this is",
                "labels": ["blocked"],
            }
        }

        self.assertEqual(result, expected)

    def test_create_issue_no_type_raise_exception(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": "A test description",
            "fields": {},
            "project": "projectName",
            "summary": "test Summary",
            "type": None,
        }

        self.test_action.connection = MockConnection()
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    def test_create_issue_fake_type_raise_exception(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": "A test description",
            "fields": {},
            "project": "projectName",
            "summary": "test Summary",
            "type": "Fake Task",
        }
        cause = "Issue type not known or user doesn't have permissions."
        assistance = "Talk to your Jira administrator to add the type or delegate necessary permissions, or choose an available type."
        self.test_action.connection = MockConnection()
        with self.assertRaises(PluginException) as error:
            self.test_action.run(action_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)

    def test_create_issue_no_description(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": "",
            "fields": {},
            "project": "projectName",
            "summary": "test Summary",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        # Just verifying no exceptions are raised
        self.assertIsNotNone(result)

    def test_create_issue_description_is_none(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": None,
            "fields": {},
            "project": "projectName",
            "summary": "test Summary",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        # Just verifying no exceptions are raised
        self.assertIsNotNone(result)

    def test_create_issue_with_unicode(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "",
            "description": "ΣΣΣΣ",
            "fields": {},
            "project": "projectName",
            "summary": "ΣΣΣ",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        # Just verifying no exceptions are raised
        self.assertIsNotNone(result)

    def test_create_issue_with_attachment(self):
        action_params = {
            "attachment_bytes": "VGhpcyBpcyBhIHRlc3QK",
            "attachment_filename": "test.txt",
            "description": "A test with an attachment",
            "fields": {},
            "project": "projectName",
            "summary": "An attachment",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)

    def test_create_issue_with_attachment_no_filename(self):
        action_params = {
            "attachment_bytes": "VGhpcyBpcyBhIHRlc3QK",
            "attachment_filename": "",
            "description": "A test with an attachment",
            "fields": {},
            "project": "projectName",
            "summary": "An attachment",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    def test_create_issue_with_attachment_no_bytes(self):
        action_params = {
            "attachment_bytes": "",
            "attachment_filename": "test.txt",
            "description": "A test with an attachment",
            "fields": {},
            "project": "projectName",
            "summary": "An attachment",
            "type": "Task",
        }

        self.test_action.connection = MockConnection()
        with self.assertRaises(PluginException):
            self.test_action.run(action_params)

    # Leave this here, it comes in handy for debugging.

    # Uncomment and add connection info to run integration test

    # def test_create_issue_integration_test(self):
    #     action_params = {
    #         "attachment_bytes": "",
    #         "attachment_filename": "",
    #         "description": "A test description",
    #         "fields": {},
    #         "project": "IDR",
    #         "summary": "test Summary",
    #         "type": "Story"
    #     }
    #
    #     connection_params = {
    #         "api_key": {
    #             "secretKey": "SecretKey"
    #         },
    #         "url": "https://example.atlassian.net/",
    #         "user": "username@example.com"
    #     }
    #
    #     self.test_conn.connect(connection_params)
    #     self.test_action.connection = self.test_conn
    #
    #     results = self.test_action.run(action_params)
