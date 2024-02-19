import sys
import os

sys.path.append(os.path.abspath("../"))

import timeout_decorator
from icon_rapid7_intsights.triggers.new_alert import NewAlert
from icon_rapid7_intsights.triggers.new_alert.schema import Input, NewAlertInput
from util import Util
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized_class
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


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


@parameterized_class(
    (
        "input_source",
        "time_value",
    ),
    [
        (Input.SOURCE_DATE_FROM_ENUM, "Hour"),
        (Input.SOURCE_DATE_FROM_ENUM, "Week"),
        (Input.SOURCE_DATE_FROM_ENUM, "Day"),
        (Input.SOURCE_DATE_FROM, "1633047083142"),
    ],
)
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
        input_params = {Input.IS_CLOSED: "Open"}
        validate(input_params, NewAlertInput.schema)
        self.action.run(input_params)

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_trigger_with_list_of_alert_types(self, make_request, ss):
        ErrorChecker.set_expected({"alert_ids": ["7cafac7ec5adaebf62257a4a", "7cafac7ec5adaebf62257a4b"]})
        input_params = {Input.ALERT_TYPE: ["Phishing", "AttackIndication"]}
        validate(input_params, NewAlertInput.schema)
        self.action.run(input_params)

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
        validate({}, NewAlertInput.schema)
        self.action.run()

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_trigger_with_source_date_from_input(self, make_request, ss):
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
        input_params = {self.input_source: self.time_value}
        validate(input_params, NewAlertInput.schema)
        self.action.run(input_params)

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_trigger_with_enum_and_string_input(self, make_request, ss):
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
        exception = "You cannot have both enum and string."
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.SOURCE_DATE_FROM_ENUM: "Hour", Input.SOURCE_DATE_FROM: "1633047083142"})
        self.assertEqual(context.exception.cause, exception)
