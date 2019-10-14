import icon_microsoft_office365_email.util.email_cleaner as EmailCleaner
from unittest import TestCase


class test_email_cleaner(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_email_as_list(self):
        actual = EmailCleaner.get_emails_as_list("//dont@findme.com sometext bob@test.com somemore text <>!@#$%^ <bob@test2.com> 12341234")
        self.assertEqual(actual[0], "bob@test.com")
        self.assertEqual(actual[1], "bob@test2.com")

    def test_get_emails_as_string(self):
        actual = EmailCleaner.get_emails_as_string("//dont@findme.com sometext bob@test.com somemore text <>!@#$%^ <bob@test2.com> 12341234")
        self.assertEqual(actual, 'bob@test.com, bob@test2.com')

    def test_get_email_as_list_blank_list(self):
        actual = EmailCleaner.get_emails_as_list("")
        self.assertEqual(actual, [])
