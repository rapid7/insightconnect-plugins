import sys
import os
import timeout_decorator

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.triggers.new_alert import NewAlert
from icon_orca_security.triggers.new_alert.schema import Input
from util import Util
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Callable, Optional


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
    expected = Util.load_parameters("new_alert_expected")
    if MockTrigger.actual == expected:
        return True
    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


@patch("requests.request", side_effect=Util.mocked_requests)
class TestNewAlert(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(NewAlert())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_new_alert(self, mock_request, mock_send):
        self.action.run({Input.INTERVAL: 60, Input.FILTERS: [{"field": "state.severity", "includes": ["hazardous"]}]})

    def test_new_alert_invalid_filter(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INTERVAL: 60, Input.FILTERS: [{"includes": ["hazardous"]}]})
        self.assertEqual(
            error.exception.cause,
            "The name of the field against which the alerts should be filtered was not specified in the filter: "
            "{'includes': ['hazardous']}.",
        )
        self.assertEqual(error.exception.assistance, "Please provide a field name and try again.")

    def test_new_alert_invalid_filter_2(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INTERVAL: 60, Input.FILTERS: [{"field": "state.severity"}]})
        self.assertEqual(
            error.exception.cause,
            "No values were given for the field to include or exclude in the filter: {'field': 'state.severity'}.",
        )
        self.assertEqual(error.exception.assistance, "Please provide 'includes' or 'excludes' fields and try again.")
