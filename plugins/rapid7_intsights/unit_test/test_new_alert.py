import sys
import os
import timeout_decorator
from icon_rapid7_intsights.triggers import NewAlert
from icon_rapid7_intsights.triggers.new_alert.schema import Input
from unit_test.util import Util
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

actual = None


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


class ErrorChecker:
    expected = {}

    @staticmethod
    def set_expected(expected):
        ErrorChecker.expected = expected

    @staticmethod
    def check_error():
        if MockTrigger.actual == ErrorChecker.expected:
            return True

        TestCase.assertDictEqual(TestCase(), MockTrigger.actual, ErrorChecker.expected)


def check_error_empty():
    expected = {"alert_ids": []}
    if MockTrigger.actual == expected:
        return True

    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


class TestNewAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(NewAlert())

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("requests.request", side_effect=Util.mock_request)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_trigger(self, mock_request, ss):
        ErrorChecker.set_expected(
            {
                "alert_ids": [
                    "7cafac7ec5adaebf62257a4c",
                    "7cafac7ec5adaebf62257a4d",
                    "7cafac7ec5adaebf62257a4e",
                    "7cafac7ec5adaebf62257a4f",
                ]
            }
        )
        self.action.run({Input.IS_CLOSED: "Open"})

    @timeout_pass(error_callback=check_error_empty)
    @timeout_decorator.timeout(2)
    @patch("requests.request", side_effect=Util.mock_request)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_trigger_with_empty(self, mock_request, ss):
        self.action.run({Input.ALERT_TYPE: ["Phishing"]})

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_trigger_with_list_of_alert_types(self, make_request, ss):
        ErrorChecker.set_expected({"alert_ids": ["7cafac7ec5adaebf62257a4a", "7cafac7ec5adaebf62257a4b"]})
        self.action.run({Input.ALERT_TYPE: ["Phishing", "AttackIndication"]})

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_trigger_with_no_inputs(self, make_request, ss):
        ErrorChecker.set_expected(
            {
                "alert_ids": [
                    "7cafac7ec5adaebf62257a4c",
                    "7cafac7ec5adaebf62257a4d",
                    "7cafac7ec5adaebf62257a4e",
                    "7cafac7ec5adaebf62257a4f",
                ]
            }
        )
        self.action.run()
