import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

import timeout_decorator
from jsonschema import validate
from komand_recorded_future.triggers.get_new_alerts import GetNewAlerts
from komand_recorded_future.triggers.get_new_alerts.schema import Input, Output

from util import Util

TRIGGERS_OUTPUT = None


# This will catch timeout errors and return None. This tells the test framework our test passed.
# This is needed because the run function in a trigger is an endless loop.
def timeout_pass(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except timeout_decorator.timeout_decorator.TimeoutError:
            return None

    return func_wrapper


# This mocks insightconnect_plugin_runtime.Trigger.send
# We need this to fake out the plugin into thinking it's sending output in the trigger's run function
class FakeSender:
    @staticmethod
    def send(data: dict[str, Any]) -> None:
        global TRIGGERS_OUTPUT
        TRIGGERS_OUTPUT = data


class TestGetNewAlerts(TestCase):
    def setUp(self) -> None:
        self.trigger = Util.default_connector(GetNewAlerts())

    @timeout_pass
    @timeout_decorator.timeout(2)
    def run_trigger(self) -> None:
        self.trigger.run({Input.FREQUENCY: 30})

    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=FakeSender.send)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_integration_get_new_alerts(self, mock_send: MagicMock, mock_requests: MagicMock) -> None:
        # Run the trigger
        self.run_trigger()

        # Validate the output
        self.assertIsNotNone(TRIGGERS_OUTPUT)
        validate(TRIGGERS_OUTPUT, self.trigger.output.schema)
        self.assertIn(Output.ALERT, TRIGGERS_OUTPUT)
        self.assertEqual(TRIGGERS_OUTPUT[Output.ALERT]["id"], "deZcB9")
