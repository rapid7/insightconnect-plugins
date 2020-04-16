from unittest import TestCase
from icon_microsoft_teams.util.strip_html import strip_html

class TestStripHTML(TestCase):
    def test_strip_html(self):
        test_string = "<h1><b>test</b></h1>"
        result = strip_html(test_string)
        self.assertEqual("test", result)

    def test_strip_teams_html(self):
        test_string = "<div>\n<div itemprop=\"copy-paste-block\">\n\n<div style=\"font-size:14px\">!purge-mail subject=\"A very specific\" delete=True</div>\n</div>\n</div>"
        result = strip_html(test_string)
        expected = "!purge-mail subject=\"A very specific\" delete=True"
        self.assertEqual(expected, result)

    def test_strip_doesnt_get_inner_newlines(self):
        test_string = "\n\n\n\n\n<b>some\nstuff</b>\n\n\n\n"
        result = strip_html(test_string)
        expected = "some\nstuff"
        self.assertEqual(expected, result)
