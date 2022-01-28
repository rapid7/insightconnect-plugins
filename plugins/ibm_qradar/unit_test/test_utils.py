import os
import sys

from unittest import TestCase

from icon_ibm_qradar.util.utils import delete_none, validate_query_range

sys.path.append(os.path.abspath("../"))


class TestUtils(TestCase):
    """Test class to manage the util test cases."""

    def test_delete_none(self):
        """
        Test delete key from dict having none value.

        :return:
        """
        input_dict = {"A": None, "B": "B"}

        self.assertEqual(len(delete_none(input_dict).keys()), 1)

    def test_delete_none_with_nested_dict(self):
        """
        Test delete key from nested dict having none value.

        :return:
        """
        input_dict = {"A": {"A": None, "B": "B"}}

        self.assertEqual(len(delete_none(input_dict)["A"].keys()), 1)

    def test_validate_query_range(self):
        """
        Test invalid Validate query range provided.

        :return:
        """
        check, _ = validate_query_range("-1-2")
        self.assertFalse(check)
