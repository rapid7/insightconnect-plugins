import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from ..icon_cisco_umbrella_destinations.connection.connection import Connection
from ..icon_cisco_umbrella_destinations.actions.dAdd import DAdd
import json
import logging

class TestDAdd(TestCase):
    def test_dAdd(self):

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DAdd()

        test_conn.logger = log
        test_action.logger = log
        try:
            with open(f"responses/dAdd.json.resp") as file:
                test_json = json.loads(file.read())
                connection_params = test_json
        except Exception as e:
            self.fail(msg="Test Failed")