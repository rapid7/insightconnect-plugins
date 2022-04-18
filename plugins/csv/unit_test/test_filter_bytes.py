import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_csv.actions.filter_bytes import FilterBytes
from komand_csv.actions.filter_bytes.schema import Input, Output


class TestFilterBytes(TestCase):
    def setUp(self) -> None:
        self.action = FilterBytes()

    def test_filter_bytes(self):
        actual = self.action.run(
            {
                Input.CSV: "c2VxLG5hbWUvZmlyc3QsbmFtZS9sYXN0LGFnZSxzdHJlZXQsY2l0eSxzdGF0ZSx6aXAsZG9sbGFyLHBpY2ssZGF0ZQoxLENyYWlnLEdvb2RtYW4sNDQsRXphemVoIEtleSxFaGFtYWtsdSxOTSw3MzQ5NCwkODk4Ni42MixZRUxMT1csMDgvMjAvMjAwNgoyLElzYWFjLFZlZ2EsNDgsRG9tdW5hIEp1bmN0aW9uLEVkZXZvbW92LE9SLDk1NTExLCQ4MTY3LjM4LFdISVRFLDEyLzE0LzE5NjMKMyxWZXJhLER1bmNhbiwzMCxEdWxlciBIaWdod2F5LEp1c2F2aW1paixERSwyMDE5NCwkOTguNDQsUkVELDAzLzA2LzE5NTQKNCxSaWNhcmRvLFNoYXJwLDU3LEphdnV6IE1hbm9yLElqa2lpaGEsSEksMTcyMTgsJDc5LjY3LEJMVUUsMDQvMTcvMTk2NQo1LEJydWNlLFN0ZXBoZW5zLDM3LEl3ZXV0YSBQbGFjZSxGb2NqZWxlLFVULDI3NTEyLCQ0OTIuMzAsR1JFRU4sMTIvMjAvMTk1Ngo2LEJldHRpZSxSaW9zLDU5LFB1Y2V2IENlbnRlcixHYWJ1dmEsQ1QsNzI2ODEsJDEwODUuMTgsWUVMTE9XLDA5LzEyLzE5NzM=",
                Input.FIELDS: "f2, f4-f5",
            }
        )
        expected = {
            Output.FILTERED: "bmFtZS9maXJzdCxhZ2Usc3RyZWV0CkNyYWlnLDQ0LEV6YXplaCBLZXkKSXNhYWMsNDgsRG9tdW5hIEp1bmN0aW9uClZlcmEsMzAsRHVsZXIgSGlnaHdheQpSaWNhcmRvLDU3LEphdnV6IE1hbm9yCkJydWNlLDM3LEl3ZXV0YSBQbGFjZQpCZXR0aWUsNTksUHVjZXYgQ2VudGVy"
        }
        self.assertEqual(actual, expected)

    def test_filter_bytes_empty_csv(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "",
                    Input.FIELDS: "f1",
                }
            )

        self.assertEqual(e.exception.cause, "CSV input is empty.")
        self.assertEqual(e.exception.assistance, "Please provide a valid CSV input.")

    def test_filter_bytes_empty_fields(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "c2VxLG5hbWUvZmlyc3QsbmFtZS9sYXN0LGFnZSxzdHJlZXQsY2l0eSxzdGF0ZSx6aXAsZG9sbGFyLHBpY2ssZGF0ZQoxLENyYWlnLEdvb2RtYW4sNDQsRXphemVoIEtleSxFaGFtYWtsdSxOTSw3MzQ5NCwkODk4Ni42MixZRUxMT1csMDgvMjAvMjAwNgo=",
                    Input.FIELDS: "",
                }
            )

        self.assertEqual(e.exception.cause, "Empty fields input.")
        self.assertEqual(e.exception.assistance, "Please provide valid fields.")

    def test_filter_bytes_invalid_fields_syntax(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "c2VxLG5hbWUvZmlyc3QsbmFtZS9sYXN0LGFnZSxzdHJlZXQsY2l0eSxzdGF0ZSx6aXAsZG9sbGFyLHBpY2ssZGF0ZQoxLENyYWlnLEdvb2RtYW4sNDQsRXphemVoIEtleSxFaGFtYWtsdSxOTSw3MzQ5NCwkODk4Ni42MixZRUxMT1csMDgvMjAvMjAwNgo=",
                    Input.FIELDS: "g3",
                }
            )

        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Improper syntax in fields string.")

    def test_filter_bytes_invalid_fields(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "c2VxLG5hbWUvZmlyc3QsbmFtZS9sYXN0LGFnZSxzdHJlZXQsY2l0eSxzdGF0ZSx6aXAsZG9sbGFyLHBpY2ssZGF0ZQoxLENyYWlnLEdvb2RtYW4sNDQsRXphemVoIEtleSxFaGFtYWtsdSxOTSw3MzQ5NCwkODk4Ni42MixZRUxMT1csMDgvMjAvMjAwNgo=",
                    Input.FIELDS: "f22",
                }
            )

        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Invalid field indices.")

    def test_filter_bytes_value_as_array(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMKdmFsdWUxLCB2YWx1ZTIsIHZhbHVlMwogdmFsdWU0LCJbdmFsdWUsIHZhbHVlXSIsIHZhbHVlNgo=",
                Input.FIELDS: "f2",
            }
        )
        expected = {Output.FILTERED: "Y29sdW1uMgp2YWx1ZTIKW3ZhbHVlLCB2YWx1ZV0="}

        self.assertEqual(actual, expected)

    def test_filter_bytes_empty_values(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMKLCB2YWx1ZTIsIHZhbHVlMwogdmFsdWU0LCwgdmFsdWU2Cg==",
                Input.FIELDS: "f2",
            }
        )
        expected = {Output.FILTERED: "Y29sdW1uMgp2YWx1ZTIK"}
        self.assertEqual(actual, expected)

    def test_filter_bytes_unicode(self):
        actual = self.action.run(
            {
                Input.CSV: "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMKLCBweXRow7bDtiwgdmFsdWUzCiB2YWx1ZTQsxIVhxIdjZcSZLCB2YWx1ZTYK",
                Input.FIELDS: "f2",
            }
        )
        expected = {Output.FILTERED: "Y29sdW1uMgpweXRow7bDtgrEhWHEh2NlxJk="}
        self.assertEqual(actual, expected)

    def test_filter_bytes_invalid_csv_syntax(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "Y29sdW1uMSxjb2x1bW4yZ2JubQp2YWx1ZTEsIHZhbHVlMiwgdmFsdWUzCiB2YWx1ZTQsIlt2YWx1ZSwgdmFsdWVdIiwgdmFsdWU2Cg==",
                    Input.FIELDS: "f2",
                }
            )
        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Improper syntax in CSV bytes.")
