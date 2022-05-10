import sys
from pathlib import Path
from unittest import TestCase

from icon_azure_sentinel.util.tools import return_non_empty

sys.path.append(str(Path("../").absolute()))


class TestTools(TestCase):
    def test_return_non_empty_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}})

    def test_return_non_empty_with_empty_list_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}, "7": []}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}})

    def test_return_non_empty_with_list_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}, "7": ["8", "9"]}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}, "7": ["8", "9"]})
