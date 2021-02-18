import sys
import os
sys.path.append(os.path.abspath('../'))

from komand_elasticsearch.util.helpers import get_search
from unittest import TestCase
from komand.exceptions import PluginException
import logging
import json

class TestHelpers(TestCase):
    def test_assertion_for_bad_query(self):
        log = logging.getLogger("Test")

        try:
            with open("../tests/search_documents.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory

            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        with self.assertRaises(PluginException):
            get_search(log,
                       connection_params.get("url"),
                       action_params.get("_index"),
                       action_params.get("_type"),
                       "{This is malformed json:",
                       connection_params.get("credentials").get("username"),
                       connection_params.get("credentials").get("password"),
                       action_params)
