import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unit_test.util import Util
from parameterized import parameterized
from icon_happyfox.util.helpers import convert_dict_keys_case, clean_dict, parse_date_from_datetime


class TestHelpers(TestCase):
    @parameterized.expand(Util.load_parameters("convert_dict_keys_case").get("parameters"))
    def test_convert_dict_keys_case(self, name, dictionary, case_type, expected):
        actual = convert_dict_keys_case(dictionary, case_type)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("clean_dict").get("parameters"))
    def test_clean_dict(self, name, dictionary, expected):
        actual = clean_dict(dictionary)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("parse_date_from_datetime").get("parameters"))
    def test_parse_date_from_datetime(self, name, date_time, expected):
        actual = parse_date_from_datetime(date_time)
        self.assertEqual(actual, expected)
