import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_dig.connection.connection import Connection
from komand_dig.actions.reverse import Reverse
import json
import logging


class TestReverse(TestCase):
    def test_reverse(self):
        params = {
            "resolver": "8.8.8.8",
            "address": "13.33.252.129"
        }

        test_action = Reverse()
        result = test_action.run(params)

        self.assertEqual(result, {})

    def test_error(self):
        params = {
            "resolver": "8.8.8",
            "address": "13.33.2"
        }

        test_action = Reverse()
        result = test_action.run(params)

        self.assertEqual(result, {})
