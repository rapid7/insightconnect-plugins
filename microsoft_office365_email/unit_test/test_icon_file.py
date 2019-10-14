from icon_microsoft_office365_email.util.icon_file import IconFile
from unittest import TestCase


# This class tests icon file
class test_icon_file(TestCase):
    def setUp(self) -> None:
        pass

    def test_create_file(self):
        icon_file = IconFile(file_name="test.txt", content="content", content_type="plain/text")
        self.assertEqual(icon_file.file_name, "test.txt")
        self.assertEqual(icon_file.content, "content")
        self.assertEqual(icon_file.content_type, "plain/text")

    def test_make_serializable(self):
        icon_file = IconFile(file_name="test.txt", content="content", content_type="plain/text")
        actual = icon_file.make_serializable()

        expected = {'content': 'content', 'content_type': 'plain/text', 'file_name': 'test.txt'}
        self.assertEqual(actual, expected)
