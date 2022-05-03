import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_csv.actions.to_json import ToJson
from komand_csv.actions.to_json.schema import Input, Output


class TestToJson(TestCase):
    def setUp(self) -> None:
        self.action = ToJson()

    def test_to_json(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMKdmFsdWUxLHZhbHVlMix2YWx1ZTMKdmFsdWU0LHZhbHVlNSx2YWx1ZTYKdmFsdWU3LHZhbHVlOCx2YWx1ZTkK",
                Input.VALIDATION: True,
            }
        )
        expected = {
            Output.JSON: [
                {"column1": "value1", "column2": "value2", "column3": "value3"},
                {"column1": "value4", "column2": "value5", "column3": "value6"},
                {"column1": "value7", "column2": "value8", "column3": "value9"},
            ]
        }
        self.assertEqual(actual, expected)

    def test_to_json_empty_csv(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "",
                    Input.VALIDATION: True,
                }
            )

        self.assertEqual(e.exception.cause, "CSV input is empty.")
        self.assertEqual(e.exception.assistance, "Please provide a valid CSV input.")

    def test_to_json_value_as_array(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSwgY29sdW1uMixjb2x1bW4zDQp2YWx1ZTEsIHZhbHVlMiwgdmFsdWUzDQp2YWx1ZTQsIlt2YWx1ZSwgdmFsdWVdIiwgdmFsdWU2DQo=",
                Input.VALIDATION: True,
            }
        )
        expected = {
            Output.JSON: [
                {"column1": "value1", "column2": "value2", "column3": "value3"},
                {"column1": "value4", "column2": "[value, value]", "column3": "value6"},
            ]
        }
        self.assertEqual(actual, expected)

    def test_to_json_empty_values(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSwsdmFsdWUzDQosdmFsdWU1LHZhbHVlNg0KdmFsdWU3LHZhbHVlOCwNCg==",
                Input.VALIDATION: True,
            }
        )
        expected = {
            Output.JSON: [
                {"column1": "value1", "column2": "", "column3": "value3"},
                {"column1": "", "column2": "value5", "column3": "value6"},
                {"column1": "value7", "column2": "value8", "column3": ""},
            ],
        }
        self.assertEqual(actual, expected)

    def test_to_json_unicode(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCsSFYcSHY2XEmSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQscHl0aMO2w7bDtm4sdmFsdWU2DQo=",
                Input.VALIDATION: True,
            }
        )
        expected = {
            Output.JSON: [
                {"column1": "ąaćceę", "column2": "value2", "column3": "value3"},
                {"column1": "value4", "column2": "pythöö\u00f6n", "column3": "value6"},
            ]
        }
        self.assertEqual(actual, expected)

    def test_to_json_invalid_csv_syntax(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMsY29sdW1uNA0KdmFsdWUxLHZhbHVlMix2YWx1ZTMsDQp2YWx1ZTQsdmFsdWU1DQp2YWx1ZTcsdmFsdWU4LHZhbHVlOSx2YWx1ZTEwDQo=",
                    Input.VALIDATION: True,
                }
            )
        self.assertEqual(e.exception.cause, "Malformed CSV.")
        self.assertEqual(e.exception.assistance, "Wrong CSV syntax.")
