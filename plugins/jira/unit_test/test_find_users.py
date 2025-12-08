import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from komand_jira.actions.find_users import FindUsers
from komand_jira.connection.connection import Connection


class User:
    def __init__(self, account_id="", name="") -> None:
        self.displayName = "test_display_name"
        self.active = True
        self.emailAddress = "test@example.com"
        self.accountId = account_id
        self.name = name
        self.raw = self.__dict__

    def get(self, key, default=None):
        """Support dictionary-like .get() method for cloud API compatibility"""
        return getattr(self, key, default)


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def search_users(self, user: str = "", maxResults: int = 10):
        self.username = user
        self.maxResults = maxResults

        if maxResults == 1:
            return [User(name="one")]
        else:
            return [User(name="one"), User(name="two"), User(name="three")]


class MockRestClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def find_users(self, query: str = "", max_results: int = 10):
        self.username = query
        self.max_results = max_results

        if max_results == 1:
            return [User(account_id=1)]
        else:
            return [User(account_id=1), User(account_id=2), User(account_id=3)]


class TestFindUsers(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = FindUsers()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

        self.test_conn.client = MockClient()
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

    def test_find_user_cloud_true_valid_1(self) -> None:
        action_params = {"query": "test_user", "max": 1}

        self.test_conn.is_cloud = True

        result = self.test_action.run(action_params)

        expected_users = [
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "account_id": 1,
            }
        ]

        self.assertDictEqual(result, {"users": expected_users})

    def test_find_user_cloud_true_valid_3(self) -> None:
        action_params = {"query": "test_user", "max": 3}

        self.test_conn.is_cloud = True

        result = self.test_action.run(action_params)

        expected_users = [
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "account_id": 1,
            },
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "account_id": 2,
            },
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "account_id": 3,
            },
        ]

        self.assertDictEqual(result, {"users": expected_users})

    def test_find_user_cloud_false_valid_1(self) -> None:
        action_params = {"query": "test_user", "max": 1}

        self.test_conn.is_cloud = False

        result = self.test_action.run(action_params)

        expected_users = [
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "name": "one",
            }
        ]

        self.assertDictEqual(result, {"users": expected_users})

    def test_find_user_cloud_false_valid_3(self) -> None:
        action_params = {"query": "test_user", "max": 3}

        self.test_conn.is_cloud = False

        result = self.test_action.run(action_params)

        expected_users = [
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "name": "one",
            },
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "name": "two",
            },
            {
                "display_name": "test_display_name",
                "active": True,
                "email_address": "test@example.com",
                "name": "three",
            },
        ]

        self.assertDictEqual(result, {"users": expected_users})
