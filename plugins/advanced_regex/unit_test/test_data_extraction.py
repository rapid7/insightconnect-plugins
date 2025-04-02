import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_advanced_regex.actions.data_extraction import DataExtraction
from icon_advanced_regex.actions.data_extraction.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestDataExtraction(TestCase):
    def setUp(self) -> None:
        self.action = DataExtraction()

    @parameterized.expand(
        [
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "lorem",
                    Input.IN_STRING: "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, lorems odales",
                    Input.MULTILINE: False,
                },
                {Output.MATCHES: [["lorem"]]},
            )
        ]
    )
    def test_data_extraction(
        self, parameters: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        response = self.action.run(parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
