import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from jsonschema import validate
from komand_sleep.actions.sleep import Sleep
from komand_sleep.actions.sleep.schema import Input, Output

STUB_INTERVAL_TIME = 1


class TestSleep(TestCase):
    def setUp(self) -> None:
        self.action = Sleep()

    def test_sleep(self):
        response = self.action.run({Input.INTERVAL: STUB_INTERVAL_TIME})
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.SLEPT: STUB_INTERVAL_TIME})

    def test_sleep_error(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.INTERVAL: -2})
        self.assertEqual(context.exception.cause, "Wrong input")
        self.assertEqual(context.exception.assistance, "Interval should not be less than zero")
