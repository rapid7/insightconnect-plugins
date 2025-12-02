import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Any
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.connection import Connection
from parameterized import param, parameterized


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @parameterized.expand(
        [
            param(
                {
                    "user": "jakub",
                    "api_key": {"secretKey": "1234567"},
                    "url": "http://jira-123456.eastus.cloudapp.azure.com",
                }
            ),
            param(
                {
                    "pat": {"secretKey": "1234567"},
                    "url": "http://jira-123456.eastus.cloudapp.azure.com",
                }
            ),
        ]
    )
    def test__validate_params_ok(self, params: dict[str, Any]) -> None:
        self.connection._validate_params(params)

    @parameterized.expand(
        [
            param(
                {
                    "api_key": {"secretKey": "12345"},
                    "url": "http://jira-123456.eastus.cloudapp.azure.com",
                },
                "Password provided but no username.",
            ),
            param(
                {
                    "user": "jakub",
                    "url": "http://jira-123456.eastus.cloudapp.azure.com",
                },
                "Username provided but no password.",
            ),
            param(
                {
                    "pat": {"secretKey": "1234567"},
                    "user": "jakub",
                    "api_key": {"secretKey": "12345"},
                    "url": "http://jira-123456.eastus.cloudapp.azure.com",
                },
                "Both Basic Auth and PAT credentials provided",
            ),
        ]
    )
    def test__validate_params_raise(self, params: dict[str, Any], cause: str) -> None:
        with self.assertRaises(PluginException) as exception_ctx:
            self.connection._validate_params(params)
        self.assertEqual(exception_ctx.exception.cause, cause)
