from unittest import TestCase
from icon_extractit.actions.email_extractor import EmailExtractor
from icon_extractit.actions.email_extractor.schema import Input, Output


class TestEmailExtractor(TestCase):
    def test_extract_emails_from_string(self):
        action = EmailExtractor()
        actual = action.run(
            {
                Input.STR: "user@example.com, user1@example.com, example_user@example.com, example.user@example.com, example-user@example.com are example emails",
            }
        )
        expected = {
            Output.EMAILS: [
                "user@example.com",
                "user1@example.com",
                "example_user@example.com",
                "example.user@example.com",
                "example-user@example.com",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_emails_from_file(self):
        action = EmailExtractor()
        actual = action.run(
            {
                Input.FILE: "dXNlckBleGFtcGxlLmNvbSwgdXNlcjFAZXhhbXBsZS5jb20sIGV4YW1wbGVfdXNlckBleGFtcGxlLmNvbSwgZXhhbXBsZS51c2VyQGV4YW1wbGUuY29tLCBleGFtcGxlLXVzZXJAZXhhbXBsZS5jb20gYXJlIGV4YW1wbGUgZW1haWxz",
            }
        )
        expected = {
            Output.EMAILS: [
                "user@example.com",
                "user1@example.com",
                "example_user@example.com",
                "example.user@example.com",
                "example-user@example.com",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_emails_from_string_bad(self):
        action = EmailExtractor()
        actual = action.run(
            {
                Input.STR: "@example.com user@example user@@example.com",
            }
        )
        expected = {Output.EMAILS: []}
        self.assertEqual(actual, expected)

    def test_extract_emails_from_file_bad(self):
        action = EmailExtractor()
        actual = action.run(
            {
                Input.STR: "QGV4YW1wbGUuY29tIHVzZXJAZXhhbXBsZSB1c2VyQEBleGFtcGxlLmNvbQ==",
            }
        )
        expected = {Output.EMAILS: []}
        self.assertEqual(actual, expected)
