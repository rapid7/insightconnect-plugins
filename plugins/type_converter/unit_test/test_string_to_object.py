import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../icon_type_converter/"))

from unittest import TestCase
from icon_type_converter.actions.string_to_object import StringToObject
import logging


class TestStringToObject(TestCase):
    def test_string_to_object_simple(self):
        log = logging.getLogger("Test")
        test_action = StringToObject()
        test_action.logger = log

        working_params = {"input": '{"rapid7": "value"}'}
        results = test_action.run(working_params)
        expected = {"output": {"rapid7": "value"}}
        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)

    def test_string_to_object_different_value_types(self):
        log = logging.getLogger("Test")
        test_action = StringToObject()
        test_action.logger = log
        working_params = {"input": '{"name":"Doe", "age":100, "city":"El Dorado"}'}
        results = test_action.run(working_params)
        expected = {"output": {"name": "Doe", "age": 100, "city": "El Dorado"}}
        self.assertEqual(expected, results)

    def test_string_to_object_nested_object(self):
        log = logging.getLogger("Test")
        test_action = StringToObject()
        test_action.logger = log
        working_params = {"input": '{"object": ["rapid", "7"],"rapid7": "value"}'}
        results = test_action.run(working_params)
        expected = {"output": {"object": ["rapid", "7"], "rapid7": "value"}}
        self.assertEqual(expected, results)

    def test_string_to_object_negatives(self):
        log = logging.getLogger("Test")
        test_action = StringToObject()
        test_action.logger = log
        with self.assertRaises(PluginException):
            working_params = {'{"object": ["rapid", "7"],"rapid7": "value"}'}
            test_action.run(working_params)

        with self.assertRaises(PluginException):
            working_params = {"this is a string"}
            test_action.run(working_params)

        with self.assertRaises(PluginException):
            working_params = {"input": '{"object: ["rapid", "7"],"rapid7": "value"}'}
            test_action.run(working_params)

        with self.assertRaises(PluginException):
            working_params = {"input": '"object": ["rapid", "7"],"rapid7": "value"'}
            test_action.run(working_params)

        # Blank input
        with self.assertRaises(PluginException):
            working_params = {"input": ""}
            test_action.run(working_params)

        # Single Space
        with self.assertRaises(PluginException):
            working_params = {"input": " "}
            test_action.run(working_params)
