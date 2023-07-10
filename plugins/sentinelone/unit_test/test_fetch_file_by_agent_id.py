import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.actions.fetch_file_by_agent_id import FetchFileByAgentId
from komand_sentinelone.actions.fetch_file_by_agent_id.schema import Input
from komand_sentinelone.connection.connection import Connection

from util import Util


class TestFetchFileByAgentId(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(FetchFileByAgentId())

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_fail_when_password_too_short(self, mock_post, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.AGENT_ID: "id",
                    Input.PASSWORD: "password",
                }
            )

        self.assertEqual("Invalid password.", error.exception.cause)
        self.assertEqual(
            "Password must have more than 10 characters and cannot contain whitespace.", error.exception.assistance
        )

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_fail_when_password_with_space(self, mock_post, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.AGENT_ID: "id",
                    Input.PASSWORD: "pass word",
                }
            )

        self.assertEqual("Invalid password.", error.exception.cause)
        self.assertEqual(
            "Password must have more than 10 characters and cannot contain whitespace.", error.exception.assistance
        )
