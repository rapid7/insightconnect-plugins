import sys
import os
import json

sys.path.append(os.path.abspath("../komand_rapid7_metasploit/"))

from unittest import TestCase
from komand_rapid7_metasploit.triggers.new_modules import NewModules
from komand_rapid7_metasploit.connection import Connection
import logging

class TestNewModules(TestCase):
    def test_integration_new_modules(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_trigger = NewModules()

        test_conn.logger = log
        test_trigger.logger = log

        try:
            with open("../tests/new_modules.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            message = "Missing json file"
            self.fail(message)

        test_conn.connect(connection_params)
        test_trigger.connection = test_conn
        results = test_trigger.run()
        self.assertIsNotNone(results)