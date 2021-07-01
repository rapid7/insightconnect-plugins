import logging
from unittest import TestCase, mock
from komand_jira.connection import Connection
from komand_jira.actions.create_issue import CreateIssue
from collections import namedtuple
from unit_test.payloads.client_fields import client_fields

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


class MockIssue():


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
            "labels": ["blocked"]
        }

        self.raw = {"fields": "something"}
        self.id = "12345"
        self.key = "12345"
        self.fields = namedtuple("ObjectName", fields_dict.keys())(*fields_dict.values())

    def permalink(self):
        return 'https://example-demo.atlassian.net/browse/ISSUE-ID-1234'


class MockClient():
    def __init__(self):
        self.client = "some fake thing"

    def projects(self):
        project = {
            'raw': {},
            'expand': 'description,lead,issueTypes,url,projectKeys,permissions,insight',
            'self': 'https://example.atlassian.net/rest/api/2/project/12345',
            'id': '12345',
            'key': 'projectKey',
            'name': 'projectName',
            'avatarUrls': {},
            'entityId': '12345-12345-12345-12345',
            'uuid': '12345-12345-12345-12345'
        }

        # Need to convert this to an object to simulate the JiraObject return
        project_object = namedtuple("ObjectName", project.keys())(*project.values())

        return [project_object]

    def create_issue(self, fields):
        return MockIssue()

    def issue_type_by_name(self, issue_type):
        pass

    def fields(self):
        return client_fields


class MockConnection():


    def __init__(self):
        self.client = MockClient()


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
            "type": "Task"
        }

        self.test_action.connection = MockConnection()
        result = self.test_action.run(action_params)

        self.assertIsNotNone(result)
        expected = {'issue': {'attachments': [], 'id': '12345', 'key': '12345',
                              'url': 'https://example-demo.atlassian.net/browse/ISSUE-ID-1234', 'summary': 'A summary',
                              'description': 'A description', 'status': ['In Progress'], 'resolution': ['new years'],
                              'reporter': ['Bob Smith'], 'assignee': ['Bob Smith'], 'created_at': 'Yesterday',
                              'updated_at': 'Yesterday', 'resolved_at': 'No idea what this is', 'labels': ['blocked'],
                              'fields': {}}}

        self.assertEqual(result, expected)

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
    #         "url": "https://komand-demo.atlassian.net/",
    #         "user": "username@example.com"
    #     }
    #
    #     self.test_conn.connect(connection_params)
    #     self.test_action.connection = self.test_conn
    #
    #     results = self.test_action.run(action_params)
