from unittest import TestCase
from komand_string.actions.trim import Trim


class TestTrim(TestCase):
    def test_trim(self):
        trim = Trim()

        params = {
            "string": " This is a string "
        }

        result = trim.run(params)
        actual = result.get("trimmed")
        self.assertIsNotNone(actual)
        self.assertEqual(actual, "This is a string")
