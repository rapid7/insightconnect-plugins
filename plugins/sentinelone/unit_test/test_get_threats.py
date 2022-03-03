import sys
import os
import timeout_decorator
from komand_sentinelone.triggers import GetThreats
from komand_sentinelone.triggers.get_threats.schema import Input
from unit_test.util import Util
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


def timeout_pass(error_callback=None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError as e:
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
    expected = {"threat": {"id": "1111-1111-11111111-1111", "status": "active"}}
    if MockTrigger.actual == expected:
        return True

    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


class TestGetThreats(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetThreats())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_poll_threats(self, mock_request, ss):
        self.action.run(
            {
                Input.FREQUENCY: 5,
                Input.RESOLVED: True,
                Input.CLASSIFICATIONS: ["class1"],
                Input.AGENT_IS_ACTIVE: True,
                Input.ENGINES: ["engine1"],
            }
        )
