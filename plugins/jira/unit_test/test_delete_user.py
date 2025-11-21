import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.actions.delete_user import DeleteUser
from komand_jira.connection.connection import Connection


class MockClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def delete_user(
        self,
        username: str = "",
    ):
        self.username = username

        return {"result": "success"}


class MockRestClient:
    def __init__(self) -> None:
        self.client = "some fake thing"

    def delete_user(self, account_id: str = ""):
        self.account_id = account_id

        return {"result": "success"}


class TestDeleteUser(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.test_conn = Connection()
        self.test_action = DeleteUser()

        test_logger = logging.getLogger("test")
        self.test_conn.logger = test_logger
        self.test_action.logger = test_logger

    def test_delete_user_cloud_true_valid(self) -> None:
        action_params = {"account_id": "5ec00968833be70b7e50df20"}

        self.test_conn.is_cloud = True
        self.test_conn.client = MockClient()
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        result = self.test_action.run(action_params)

        self.assertTrue(result.get("success"))

    def test_delete_user_cloud_false_valid(self) -> None:
        action_params = {"username": "user1"}

        self.test_conn.is_cloud = False
        self.test_conn.client = MockClient()
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        result = self.test_action.run(action_params)

        self.assertTrue(result.get("success"))

    def test_delete_user_cloud_true_invalid(self) -> None:
        action_params = {"username": "user1"}

        self.test_conn.is_cloud = True
        self.test_conn.client = MockClient()
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        with self.assertRaises(PluginException) as plg_err:
            self.test_action.run(action_params)

        self.assertIn("Account ID not provided", plg_err.exception.cause)

    def test_delete_user_cloud_false_invalid(self) -> None:
        action_params = {"account_id": "5ec00968833be70b7e50df20"}

        self.test_conn.is_cloud = False
        self.test_conn.client = MockClient()
        self.test_conn.rest_client = MockRestClient()
        self.test_action.connection = self.test_conn

        with self.assertRaises(PluginException) as plg_err:
            self.test_action.run(action_params)

        self.assertIn("Username not provided", plg_err.exception.cause)
