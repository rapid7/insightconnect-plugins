from datetime import datetime
import unittest
import json
import datetime
import io
import botocore.response as br

from parameterized import parameterized
from pathlib import Path
from icon_aws_ec2.util.common import ActionHelper


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @parameterized.expand(
        [
            ("snake_str_1", "SnakeStr1"),
            ("sssnake31_#test", "Sssnake31#Test"),
            ("s__o", "SO"),
            ("_private_variable", "PrivateVariable"),
        ],
    )
    def test_to_upper_camel_case(self, input_str, output_str):
        camel_case_str = ActionHelper.to_upper_camel_case(input_str)
        self.assertEqual(camel_case_str, output_str)

    def test_get_empty_input(self):
        formatted_params = ActionHelper.format_input({"$param1": {}, "$param2": {}, "$param3": [], "$param4": "test"})
        self.assertEqual(formatted_params, {"Param4": "test"})

    def test_get_empty_output(self):
        path = Path(__file__).parent / f"payloads/output_schema.json"
        with open(path) as file:
            output_schema = json.load(file)
        empty_output = ActionHelper.get_empty_output(output_schema)
        self.assertEqual(
            empty_output, {"reservations": [], "response_metadata": {"http_status_code": 0, "request_id": ""}}
        )

    @parameterized.expand(
        [
            (datetime.datetime(2022, 9, 4), "2022-09-04T00:00:00"),
            (2.467, "2.467"),
            (b"a", "YQ=="),
            (br.StreamingBody(io.BytesIO(b"\x01\x02\x03\x04"), 4), "AQIDBA=="),
            ("test string", "test string"),
            ([3.14, 2.71], ["3.14", "2.71"]),
            ([{"key1": 3.14}, {"key2": 2.71}], [{"key1": "3.14"}, {"key2": "2.71"}]),
        ]
    )
    def test_fix_output_types(self, input_type, output_type):
        ah = ActionHelper()
        date = ah.fix_output_types(input_type)
        self.assertEqual(output_type, date)

    @parameterized.expand(
        [
            ({"UpperCamel": "OutputValue"}, {"upper_camel": "OutputValue"}),
            ([{"UpperCamel": "OutputValue"}], [{"upper_camel": "OutputValue"}]),
        ]
    )
    def test_convert_all_to_snake_case(self, test_input, test_output):
        converted = ActionHelper.convert_all_to_snake_case(test_input)
        self.assertEqual(converted, test_output)

    def test_format_output(self):
        ah = ActionHelper()
        path = Path(__file__).parent / f"payloads/output_schema.json"
        with open(path) as file:
            output_schema = json.load(file)
        test_input = {"Reservations": [{"key1": 1}]}
        output = ah.format_output(output_schema, test_input)
        correct_output = {"reservations": [{"key1": 1}], "response_metadata": {"http_status_code": 0, "request_id": ""}}
        self.assertEqual(output, correct_output)

    @parameterized.expand(
        [
            ({"snake_case": "OutputValue"}, {"SnakeCase": "OutputValue"}),
            ([{"snake_case": "OutputValue"}], [{"SnakeCase": "OutputValue"}]),
        ]
    )
    def test_convert_all_to_upper_camel_case(self, test_input, test_output):
        converted = ActionHelper.convert_all_to_upper_camel_case(test_input)
        self.assertEqual(test_output, converted)
