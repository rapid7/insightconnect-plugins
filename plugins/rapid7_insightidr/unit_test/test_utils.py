import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_rapid7_insightidr.util.resource_helper import convert_list_to_string, get_sort_param
from parameterized import parameterized


class TestUtils(TestCase):
    @parameterized.expand(
        [
            ("Create time Ascending", "create_time,ASC"),
            ("Create time Descending", "create_time,DESC"),
            ("Priority Ascending", "priority,ASC"),
            ("Priority Descending", "priority,DESC"),
            ("Last alert time Ascending", "last_alert_time,ASC"),
            ("Last alert time Descending", "last_alert_time,DESC"),
            ("RRN Ascending", "rrn,ASC"),
            ("RRN Descending", "rrn,DESC"),
            ("Alerts most recent created time Ascending", "alerts_most_recent_created_time,ASC"),
            ("Alerts most recent created time Descending", "alerts_most_recent_created_time,DESC"),
            ("Alerts most recent detection created time Ascending", "alerts_most_recent_detection_created_time,ASC"),
            ("Alerts most recent detection created time Descending", "alerts_most_recent_detection_created_time,DESC"),
        ]
    )
    def test_get_sort_param(self, input_sort_str, expected_result) -> None:
        result = get_sort_param(input_sort_str)
        self.assertEqual(expected_result, result)

    @parameterized.expand([(["LOW"], "LOW"), (["LOW", "MEDIUM", "HIGH"], "LOW,MEDIUM,HIGH")])
    def test_convert_list_to_string(self, input_list_of_str, expected_result) -> None:
        result = convert_list_to_string(input_list_of_str)
        self.assertEqual(expected_result, result)
