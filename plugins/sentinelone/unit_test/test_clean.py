import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_sentinelone.util.api import clean


class TestClean(TestCase):
    def test_clean_object_with_empty_objects(self):
        actual = clean([{}, {}, {}])
        expected = [{}, {}, {}]

        self.assertEqual(expected, actual)

    def test_clean_object(self):
        actual = clean(
            [
                {
                    "key1": "value1",
                    "key2": None,
                    "key3": "None",
                    "computerMemberOf": [],
                    "lastUserMemberOf": "None",
                    "locations": "None",
                    "networkInterfaces": "None",
                    "inet": "None",
                    "inet6": "None",
                    "userActionsNeeded": ["stop"],
                }
            ]
        )
        expected = [
            {
                "computerMemberOf": [],
                "inet": [],
                "inet6": [],
                "key1": "value1",
                "key3": "None",
                "lastUserMemberOf": [],
                "locations": [],
                "networkInterfaces": [],
                "userActionsNeeded": ["stop"],
            }
        ]

        self.assertEqual(expected, actual)
