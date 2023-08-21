import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_html.actions.validate import Validate
from insightconnect_plugin_runtime.exceptions import PluginException


class TestValidate(TestCase):
    def test_validate(self):

        params = {"doc": "<!DOCTYPE html><html><title>Example</title><body><h1>Rapid7 InsightConnect</h1><p>Automate with InsightConnect!</p></body></html>"}

        test_action = Validate()
        result = test_action.run(params)

        self.assertEqual(
            result, True
        )

    def test_bad_input(self):

        params = {"doc": "bad input example"}

        test_action = Validate()
        result = test_action.run(params)

        self.assertEqual(
            result, False
        )

    def test_action_empty_string(self):
        params = {"doc": " "}

        test_action = Validate()

        with self.assertRaises(PluginException) as context:
            test_action.run(params)
        self.assertEqual(context.exception.cause, "Run: Invalid input.")
