from unittest import TestCase
from komand_html.actions.text import Text


class TestText(TestCase):

    def test_run(self):
        params = {
            "doc": "<i>This is some text</i>"
        }

        test_action = Text()
        result = test_action.run(params)

        self.assertEqual(result, {"text": "This is some text"})

    def test_run_no_text(self):
        params = {
            "doc": ""
        }

        test_action = Text()
        result = test_action.run(params)

        self.assertEqual(result, {"text": ""})

    def test_difficult_html(self):
        test_text = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
        params = {
            'doc': test_text
        }

        test_action = Text()
        result = test_action.run(params)

        expected = {'text': "\nThe Dormouse's story\n\nThe Dormouse's story\nOnce upon a time there were three little sisters; and their names were\nElsie,\nLacie and\nTillie;\nand they lived at the bottom of a well.\n...\n"}

        self.assertEqual(result, expected)

    def test_run_bad_html(self):
        params = {
            "doc": "<a>This is fubar.<b></c> Moar fubar"
        }

        test_action = Text()
        result = test_action.run(params)

        self.assertEqual(result, {"text": "This is fubar. Moar fubar"})
