from unittest import TestCase
from icon_microsoft_teams.util.words_utils import add_words_values_to_message
import json

class TestAddWords(TestCase):
    def test_add_words(self):
        with open("../examples/message.json") as json_file:
            data = json.load(json_file)

        result = add_words_values_to_message(data.get("message"))

        self.assertTrue("words" in result.keys())
        self.assertTrue("first_word" in result.keys())
        self.assertEqual(result.get("first_word"), "Hello")
        self.assertEqual(result.get("words"), ['Hello', 'from', 'a', 'command', 'line', 'test!'])

