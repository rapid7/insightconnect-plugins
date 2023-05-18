import sys
import os
import timeout_decorator

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightappsec.triggers.new_vulnerabilities import NewVulnerabilities
from komand_rapid7_insightappsec.triggers.new_vulnerabilities.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from typing import Callable, Optional
from datetime import datetime


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                if error_callback:
                    return error_callback()
                return None

        return func_wrapper

    return func_timeout


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


def check_error():
    expected = Util.read_file_to_dict("expected/new_vulnerabilities.json.exp")
    if MockTrigger.actual == expected:
        return True
    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


@patch(
    "komand_rapid7_insightappsec.triggers.new_vulnerabilities.trigger.NewVulnerabilities.get_current_time",
    return_value=datetime.strptime("2023-04-28T08:34:46", "%Y-%m-%dT%H:%M:%S"),
)
@patch("requests.sessions.Session.post", side_effect=Util.mock_request)
class TestNewVulnerabilities(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(NewVulnerabilities())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_new_vulnerabilities(self, mock_request, mock_get_time, mock_send):
        self.action.run({Input.FREQUENCY: 1})
