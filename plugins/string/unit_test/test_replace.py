from unittest import TestCase
from komand_string.actions.replace import Replace
import logging


class TestReplace(TestCase):
    def test_replace(self):
        logger = logging.getLogger("Test")
        test_action = Replace()
        test_action.log = logger

        params = {"in_string": "abcde", "string_part_to_find": "b", "replacement_value": "c"}

        result = test_action.run(params)
        expected = {"result_string": "accde"}
        self.assertEqual(result, expected)

    def test_replace_blank(self):
        logger = logging.getLogger("Test")
        test_action = Replace()
        test_action.log = logger

        params = {"in_string": "abcde", "string_part_to_find": "b", "replacement_value": ""}

        result = test_action.run(params)
        expected = {"result_string": "acde"}
        self.assertEqual(result, expected)

    def test_replace_full_string(self):
        logger = logging.getLogger("Test")
        test_action = Replace()
        test_action.log = logger

        params = {"in_string": "the cow jumped over the moon", "string_part_to_find": "cow", "replacement_value": "cat"}

        result = test_action.run(params)
        expected = {"result_string": "the cat jumped over the moon"}
        self.assertEqual(result, expected)

    def test_replace_real_use_case(self):
        logger = logging.getLogger("Test")
        test_action = Replace()
        test_action.log = logger

        params = {
            "in_string": '{\\"id\\":\\"R1155\\",\\"title\\":\\"Account Executive\\"}',
            "string_part_to_find": "\\",
            "replacement_value": "",
        }

        result = test_action.run(params)
        expected = {"result_string": '{"id":"R1155","title":"Account Executive"}'}
        self.assertEqual(result, expected)
