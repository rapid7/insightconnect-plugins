import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from collections import namedtuple
from unittest import TestCase

from komand_jira.util.util import look_up_project


class MockClient:
    def __init__(self):
        project = {
            "raw": {},
            "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
            "self": "https://example.atlassian.net/rest/api/2/project/12345",
            "id": "12345",
            "key": "keyDB",
            "name": "nameDB",
            "avatarUrls": {},
            "entityId": "12345-12345-12345-12345",
            "uuid": "12345-12345-12345-12345",
        }

        # Need to convert this to an object to simulate the JiraObject return
        project_object = namedtuple("ObjectName", project.keys())(*project.values())

        self.test_project_list = [project_object]

    def projects(self):
        return self.test_project_list


class TestUtil(TestCase):
    def test_lookup_project(self):
        logger = logging.getLogger("Test")
        mock_client = MockClient()
        result = look_up_project("keyDB", mock_client, logger)
        self.assertTrue(result)

        result = look_up_project("nameDB", mock_client, logger)
        self.assertTrue(result)

        result = look_up_project("Dont Find This", mock_client, logger)
        self.assertFalse(result)
