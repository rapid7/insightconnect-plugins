import json
import logging
import os
import re
import string
import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from icon_azure_ad_admin.actions.create_user import CreateUser
from icon_azure_ad_admin.actions.create_user.action import _pw_gen
from icon_azure_ad_admin.connection.connection import Connection

from mocks import MockRequest


class TestGeneratePassword(TestCase):
    def test_generate_password(self) -> None:
        generate_password = _pw_gen()
        has_lowercase = re.search(r"[a-z]", generate_password)
        has_uppercase = re.search(r"[A-Z]", generate_password)
        has_digits = re.search(r"[0-9]", generate_password)
        has_punctuation = [char for char in generate_password if char in string.punctuation]
        self.assertTrue(has_lowercase)
        self.assertTrue(has_uppercase)
        self.assertTrue(has_digits)
        self.assertTrue(has_punctuation)


class TestCreateUser(TestCase):
    def setUp(self) -> None:
        self.connection = mock.create_autospec(Connection())
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.tenant = "tenant_id"

        self.action = CreateUser()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action loger")

        self.password = _pw_gen()
        self.app_id = "application_id"
        self.app_secret = {"application_secret": {"secretKey": "secret_key"}}
        self.params = {
            "accountEnabled": True,
            "displayName": "ExampleUser",
            "mailNickname": "example@user.com",
            "userPrincipalName": "ExampleName",
            "passwordProfile": {"forceChangePasswordNextSignIn": True, "password": self.password},
            "notify_from": "example@user.com",
            "notify_recipient": "example@user.com",
            "notify_email_body": "Example Notify",
        }
        self.message = "Text Message"
        self.mailbox = "mailbox_id"

    @mock.patch("requests.post", return_value=MockRequest(201))
    def test_create_user_status_ok(self, mock_request: MagicMock) -> None:
        create_user = self.action._create_user(self.params, self.password)
        self.assertEqual(create_user, True)

    @mock.patch("requests.post", return_value=MockRequest(400))
    def test_create_user_status_bad(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action._create_user(self.params, self.password)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes["unknown"],
        )

    def test_compose_email(self) -> None:
        compose_email = self.action._compose_email(self.params, self.password)
        expected_result = {
            "message": {
                "subject": "New user created",
                "body": {"contentType": "text", "content": "Example Notify"},
                "from": {"emailAddress": {"address": "example@user.com"}},
                "toRecipients": [{"emailAddress": {"address": "example@user.com"}}],
                "ccRecipients": [],
                "bccRecipients": [],
            },
            "saveToSentItems": "false",
        }

        self.assertEqual(compose_email, json.dumps(expected_result))

    @mock.patch("requests.post", return_value=MockRequest(202))
    def test_send_message_status_ok(self, mock_request: MagicMock) -> None:
        send_message = self.action.send_message(self.message, self.mailbox)
        self.assertEqual(send_message, True)

    @mock.patch("requests.post", return_value=MockRequest(400))
    def test_send_message_status_bad(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.send_message(self.message, self.mailbox)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes["unknown"],
        )

    @mock.patch("icon_azure_ad_admin.actions.create_user.action.CreateUser._create_user", return_value=True)
    @mock.patch("icon_azure_ad_admin.actions.create_user.action.CreateUser._compose_email", return_value={})
    @mock.patch("icon_azure_ad_admin.actions.create_user.action.CreateUser.send_message", return_value=True)
    def test_run_action(self, create_user: MagicMock, compose_email: MagicMock, send_message: MagicMock) -> None:
        self.assertEqual(self.action.run(), {"success": True})
