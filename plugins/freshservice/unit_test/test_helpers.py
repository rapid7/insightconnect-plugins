import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unit_test.util import Util
from parameterized import parameterized
from icon_freshservice.util.helpers import dict_keys_to_camel_case, process_list


class TestHelpers(TestCase):
    @parameterized.expand(Util.load_parameters("dict_keys_to_camel_case").get("parameters"))
    def test_dict_keys_to_camel_case(self, name, dictionary, expected):
        actual = dict_keys_to_camel_case(dictionary)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("process_list").get("parameters"))
    def test_process_list(self, name, list_to_process, expected):
        actual = process_list(list_to_process)
        self.assertEqual(actual, expected)
