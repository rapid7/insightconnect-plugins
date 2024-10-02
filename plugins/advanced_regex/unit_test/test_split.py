import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_advanced_regex.actions.split import Split
from icon_advanced_regex.actions.split.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestSplit(TestCase):
    def setUp(self) -> None:
        self.action = Split()

    @parameterized.expand(
        [
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "lorem",
                    Input.IN_STRING: "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, lorems odales sed",
                    Input.MAX_SPLIT: 0,
                    Input.MULTILINE: False,
                },
                {
                    Output.RESULT: [
                        "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, ",
                        "s odales sed",
                    ]
                },
            )
        ]
    )
    def test_split(self, parameters: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
