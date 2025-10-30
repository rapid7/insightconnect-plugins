# plugins/csv/unit_test/test_json_to_csv_string.py

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_csv.actions.json_to_csv_string import JsonToCsvString
from komand_csv.actions.json_to_csv_string.schema import Input, Output


class TestJsonToCsvString(TestCase):
    def test_json_to_csv_string(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "value5", "column3": "value6"},
                    {"column1": "value7", "column2": "value8", "column3": "value9"},
                ],
            }
        )
        expected = {
            Output.CSV_STRING: "column1,column2,column3\r\nvalue1,value2,value3\r\nvalue4,value5,value6\r\nvalue7,value8,value9\r\n"
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_empty_json(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [],
            }
        )
        expected = {Output.CSV_STRING: ""}
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_value_as_array(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": ["value", "value"], "column3": "value6"},
                ],
            }
        )
        # Arrays of scalars are joined with "|" now
        expected = {
            Output.CSV_STRING: "column1,column2,column3\r\nvalue1,value2,value3\r\nvalue4,value|value,value6\r\n"
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_value_as_object(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": {"column2_1": "value", "column": "value"}, "column3": "value6"},
                ],
            }
        )
        # Objects are expanded into additional columns
        expected = {
            Output.CSV_STRING: "column1,column2,column3,column2.column2_1,column2.column\r\nvalue1,value2,value3,,\r\nvalue4,,value6,value,value\r\n"
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_empty_object(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "value5", "column3": "value6"},
                    {},
                ],
            }
        )
        expected = {
            Output.CSV_STRING: "column1,column2,column3\r\nvalue1,value2,value3\r\nvalue4,value5,value6\r\n,,\r\n"
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_empty_fields(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "", "column3": "value3"},
                    {"column1": "", "column2": "value5", "column3": "value6"},
                    {"column1": "value7", "column2": "value8", "column3": ""},
                ],
            }
        )
        expected = {
            Output.CSV_STRING: "column1,column2,column3\r\nvalue1,,value3\r\n,value5,value6\r\nvalue7,value8,\r\n"
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_unicode(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "ąaćceę", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "pythöö\u00f6n", "column3": "value6"},
                ],
            }
        )
        expected = {Output.CSV_STRING: "column1,column2,column3\r\nąaćceę,value2,value3\r\nvalue4,pythööön,value6\r\n"}
        self.assertEqual(actual, expected)

    def test_json_to_csv_string_unstructured_data(self):
        action = JsonToCsvString()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "value5"},
                    {"column1": "value7", "column2": "value8", "column3": "value9", "column4": "value10"},
                ],
            }
        )
        expected = {
            Output.CSV_STRING: "column1,column2,column3,column4\r\nvalue1,value2,value3,\r\nvalue4,value5,,\r\nvalue7,value8,value9,value10\r\n"
        }
        self.assertEqual(actual, expected)
