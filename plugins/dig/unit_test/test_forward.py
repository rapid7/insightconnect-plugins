import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_dig.connection.connection import Connection
from komand_dig.actions.forward import Forward
import json
import logging


class TestForward(TestCase):
    def test_forward(self):
        params = {
            "domain": "rapid7.com",
            "resolver": "8.8.8.8",
            "query": "MX"
        }

        test_action = Forward()
        result = test_action.run(params)

        self.assertEqual(result, {})

    def test_error(self):
        params = {
            "domain": "..com",
            "resolver": "8.8.8",
            "query": "p"
        }

        test_action = Forward()
        result = test_action.run(params)

        self.assertEqual(result, {})
