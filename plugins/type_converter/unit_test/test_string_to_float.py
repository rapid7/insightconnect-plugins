import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../icon_type_converter/"))

from unittest import TestCase
from icon_type_converter.actions.string_to_float import StringToFloat
import logging


class TestStringToFloat(TestCase):
    def test_string_to_float(self):
        log = logging.getLogger("Test")
        test_action = StringToFloat()
        test_action.logger = log

        working_params = {"input": "123.456"}
        results = test_action.run(working_params)
        expected = {"output": 123.456}

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)

        working_params = {"input": "1"}
        results = test_action.run(working_params)
        expected = {"output": 1}
        self.assertEqual(expected, results)

        working_params = {"input": "0"}
        results = test_action.run(working_params)
        expected = {"output": 0}
        self.assertEqual(expected, results)

        working_params = {"input": "3.14159265359"}
        results = test_action.run(working_params)
        expected = {"output": 3.14159265359}
        self.assertEqual(expected, results)

        with self.assertRaises(PluginException):
            working_params = {"this is a string"}
            test_action.run(working_params)

        with self.assertRaises(PluginException):
            working_params = {"input": "twenty"}
            test_action.run(working_params)

        with self.assertRaises(PluginException):
            working_params = {"123.456"}
            test_action.run(working_params)
