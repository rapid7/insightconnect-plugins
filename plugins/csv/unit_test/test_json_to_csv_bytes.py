# plugins/csv/unit_test/test_json_to_csv_bytes.py

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_csv.actions.json_to_csv_bytes import JsonToCsvBytes
from komand_csv.actions.json_to_csv_bytes.schema import Input, Output


class TestJsonToCsvBytes(TestCase):
    def test_json_to_csv_bytes(self):
        action = JsonToCsvBytes()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "value1", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "value5", "column3": "value6"},
                    {"column1": "value7", "column2": "value8", "column3": "value9"},
                ],
            }
        )
        # Expect unwrapped base64 (single line, no trailing newline)
        expected = {
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFsdWU1LHZhbHVlNg0KdmFsdWU3LHZhbHVlOCx2YWx1ZTkNCg=="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_empty_json(self):
        action = JsonToCsvBytes()
        actual = action.run(
            {
                Input.JSON: [],
            }
        )
        expected = {Output.CSV_BYTES: ""}
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_value_as_array(self):
        action = JsonToCsvBytes()
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
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFsdWV8dmFsdWUsdmFsdWU2DQo="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_value_as_object(self):
        action = JsonToCsvBytes()
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
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMsY29sdW1uMi5jb2x1bW4yXzEsY29sdW1uMi5jb2x1bW4NCnZhbHVlMSx2YWx1ZTIsdmFsdWUzLCwNCnZhbHVlNCwsdmFsdWU2LHZhbHVlLHZhbHVlDQo="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_empty_object(self):
        action = JsonToCsvBytes()
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
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFsdWU1LHZhbHVlNg0KLCwNCg=="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_empty_fields(self):
        action = JsonToCsvBytes()
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
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSwsdmFsdWUzDQosdmFsdWU1LHZhbHVlNg0KdmFsdWU3LHZhbHVlOCwNCg=="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_unicode(self):
        action = JsonToCsvBytes()
        actual = action.run(
            {
                Input.JSON: [
                    {"column1": "ąaćceę", "column2": "value2", "column3": "value3"},
                    {"column1": "value4", "column2": "pythöö\u00f6n", "column3": "value6"},
                ],
            }
        )
        expected = {
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCsSFYcSHY2XEmSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQscHl0aMO2w7bDtm4sdmFsdWU2DQo="
        }
        self.assertEqual(actual, expected)

    def test_json_to_csv_bytes_unstructured_data(self):
        action = JsonToCsvBytes()
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
            Output.CSV_BYTES: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMsY29sdW1uNA0KdmFsdWUxLHZhbHVlMix2YWx1ZTMsDQp2YWx1ZTQsdmFsdWU1LCwNCnZhbHVlNyx2YWx1ZTgsdmFsdWU5LHZhbHVlMTANCg=="
        }
        self.assertEqual(actual, expected)
