import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_advanced_regex.actions.replace import Replace
from icon_advanced_regex.actions.replace.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestReplace(TestCase):
    def setUp(self) -> None:
        self.action = Replace()

    @parameterized.expand(
        [
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "lorem",
                    Input.IN_STRING: "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, lorems odales",
                    Input.MAX_REPLACE: 0,
                    Input.MULTILINE: False,
                    Input.REPLACE_STRING: "REPLACED",
                },
                {
                    Output.RESULT: "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, REPLACEDs odales"
                },
            )
        ]
    )
    def test_replace(
        self, parameters: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        response = self.action.run(parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
