import os.path
import sys
from unittest import TestCase

from parameterized import param, parameterized

sys.path.append(os.path.abspath("../"))
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_dynamodb.util.extra_schemas.scan import exclusive_start_key_schema
from komand_dynamodb.util.validation import additional_argument_validator

KEY_NAME = "exclusive_start_key"


class DummyAction:
    @additional_argument_validator(KEY_NAME, exclusive_start_key_schema)
    def run(self, params={}):
        return params


class TestValidation(TestCase):
    @parameterized.expand(
        [
            (
                {KEY_NAME: {"AccountID": {"S": "123456"}}},
                {KEY_NAME: {"AccountID": {"S": "123456"}}},
            ),
            ({KEY_NAME: {"AccountID": {"N": "2"}}}, {KEY_NAME: {"AccountID": {"N": "2"}}}),
            (
                {KEY_NAME: {"AccountID": {"BOOL": True}}},
                {KEY_NAME: {"AccountID": {"BOOL": True}}},
            ),
            (
                {KEY_NAME: {"AccountID": {"SS": ["jakub", "szczepan"]}}},
                {KEY_NAME: {"AccountID": {"SS": ["jakub", "szczepan"]}}},
            ),
            (
                {KEY_NAME: {"AccountID": {"L": [{"S": "string"}]}}},
                {KEY_NAME: {"AccountID": {"L": [{"S": "string"}]}}},
            ),
            (
                {KEY_NAME: {"AccountID": {"B": "abcde"}}},
                {KEY_NAME: {"AccountID": {"B": "abcde"}}},
            ),
            (
                {KEY_NAME: {"AccountID": {"NULL": True}}},
                {KEY_NAME: {"AccountID": {"NULL": True}}},
            ),
        ]
    )
    def test_validation_success(self, input_params, expected_output):
        action = DummyAction()
        result = action.run(params=input_params)
        self.assertEqual(expected_output, result)

    @parameterized.expand([param({KEY_NAME: {"AccountID": 3}}), param({KEY_NAME: {"AccountID": {"S": 2}}})])
    def test_validation_fail(self, wrong_input):
        action = DummyAction()
        with self.assertRaises(PluginException) as ctx:
            result = action.run(params=wrong_input)
