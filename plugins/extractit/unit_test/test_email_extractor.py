from unittest import TestCase
from icon_extractit.actions.email_extractor import EmailExtractor
from icon_extractit.actions.email_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("email_extractor").get("parameters")


class TestEmailExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_emails(self, name, string, file, expected):
        action = EmailExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.EMAILS: expected}
        self.assertEqual(actual, expected)
