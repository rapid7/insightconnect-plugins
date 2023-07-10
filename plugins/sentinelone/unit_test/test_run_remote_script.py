import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
from unittest import TestCase
from unittest.mock import patch

from komand_sentinelone.actions.run_remote_script import RunRemoteScript
from komand_sentinelone.actions.run_remote_script.schema import Input
from komand_sentinelone.connection.connection import Connection

from util import Util


class TestRunRemoteScript(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(RunRemoteScript())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success(self, mock_request):
        expected = {"affected": 1}
        actual = self.action.run(
            {
                Input.IDS: ["1470609440131178177"],
                Input.SCRIPT_ID: "100000000000",
                Input.TASK_DESCRIPTION: "Test task description",
            }
        )
        self.assertEqual(expected, actual)
