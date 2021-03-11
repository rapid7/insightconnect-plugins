import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_url_utils.connection.connection import Connection
from icon_url_utils.actions.encode import Encode
import json
import logging


class TestEncode(TestCase):
    def test_encode(self):

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Encode()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/encode.json") as file:
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


        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        expected = {'url': 'example.com%3Ftest%3Dresult%3Fkey%3Dvalue'}
        self.assertEquals(expected, results)


    def test_encode_all(self):

        log = logging.getLogger("Test")
        test_action = Encode()
        test_action.logger = log
        test_url = 'https://example.com/page?text=abc$%^-space here~<>()#!123'
        result = test_action.encode_url(True, test_url)

        actual = 'https://example.com%2Fpage%3Ftext%3Dabc%24%25%5E-space%20here~%3C%3E%28%29%23%21123'
        self.assertEqual(result, actual)
