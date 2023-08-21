import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.email_extractor import EmailExtractor
from icon_extractit.actions.email_extractor.schema import EmailExtractorOutput, Input, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("email_extractor").get("parameters")


class TestEmailExtractor(TestCase):
    def setUp(self) -> None:
        self.action = EmailExtractor()

    @parameterized.expand(parameters)
    def test_extract_emails(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.EMAILS: expected}
        validate(actual, EmailExtractorOutput.schema)
        self.assertEqual(actual, expected)
