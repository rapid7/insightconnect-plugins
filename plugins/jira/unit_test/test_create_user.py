import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from komand_jira.actions.create_user import CreateUser
from komand_jira.connection.connection import Connection


class MockClient:
    def __init__(self, is_cloud) -> None:
        self.client = "some fake thing"
        self.is_cloud = is_cloud

    def add_user(self, fullname: str, email: str, password: str, notify: bool, username: str):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.notify = notify
        self.username = username

        if self.is_cloud == True and username == fullname:
            return {"result": "success"}
        elif self.is_cloud == False and username == "":
            return {"result": "success"}

        return {"result": "failed"}


class MockRestClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def add_user(self, username: str, email: str, password: str, products: list, notify: bool) -> bool:
        self.username = username
        self.email = email
        self.password = password
        self.products = products
        self.notify = notify
        return True


class TestCreateUser(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = CreateUser()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    def test_create_user_cloud_true(self) -> None:
        action_params = {
            "email": "user@example.com",
            "notify": True,
            "password": "mypassword",
            "username": "test_username",
        }

        self.test_conn.is_cloud = True
        self.test_conn.client = MockClient(self.test_conn.is_cloud)
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        result = self.test_action.run(action_params)

        self.assertTrue(result.get("success"))

    def test_create_user_cloud_false(self) -> None:
        action_params = {
            "email": "user@example.com",
            "notify": True,
            "password": "mypassword",
            "username": "test_username",
        }

        self.test_conn.is_cloud = False
        self.test_conn.client = MockClient(self.test_conn.is_cloud)
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        result = self.test_action.run(action_params)

        self.assertTrue(result.get("success"))
