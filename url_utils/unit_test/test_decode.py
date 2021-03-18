import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_url_utils.connection.connection import Connection
from icon_url_utils.actions.decode import Decode
import json
import logging


class TestDecode(TestCase):
    def test_integration_decode(self):
        """
        TODO: Implement assertions at the end of this test case

        This is an integration test that will connect to the services your plugin uses. It should be used
        as the basis for tests below that can run independent of a "live" connection.

        This test assumes a normal plugin structure with a /tests directory. In that /tests directory should
        be json samples that contain all the data needed to run this test. To generate samples run:

        icon-plugin generate samples

        """

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Decode()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/decode.json") as file:
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
        self.assertEquals({}, results)


    def test_decode_default(self):

        log = logging.getLogger("Test")
        test_action = Decode()
        test_action.logger = log
        test_url = 'https://example.com/page?text=abc%24%25%5E-space%20here~%3C%3E%28%29%23%21123'
        result = test_action.decode_url(test_url, errors='')

        actual = 'https://example.com/page?text=abc$%^-space here~<>()#!123'
        self.assertEqual(result, actual)


    def test_decode_all(self):

        log = logging.getLogger("Test")
        test_action = Decode()
        test_action.logger = log
        test_url = 'https://example.com%2Fpage%3Ftext%3Dabc%24%25%5E-space%20here~%3C%3E%28%29%23%21123'
        result = test_action.decode_url(test_url, errors='')

        actual = 'https://example.com/page?text=abc$%^-space here~<>()#!123'
        self.assertEqual(result, actual)


    def test_decode_unicode(self):

        log = logging.getLogger("Test")
        test_action = Decode()
        test_action.logger = log
        test_url = '%C4%95%CF%87%C4%81m%C6%A5%C4%BC%C8%85.%C6%88%C8%AD%E1%B9%81'
        result = test_action.decode_url(test_url, errors='')

        actual = 'ĕχāmƥļȅ.ƈȭṁ'
        self.assertEqual(result, actual)


    def test_decode_replace(self):

        log = logging.getLogger("Test")
        test_action = Decode()
        test_action.logger = log
        test_url = 'example.com/utf8%3D%E2%9C%93%26replace%3D%99'
        result = test_action.decode_url(test_url, errors='replace')

        actual = 'example.com/utf8=✓&replace=�'
        self.assertEqual(result, actual)


    def test_decode_ignore(self):

        log = logging.getLogger("Test")
        test_action = Decode()
        test_action.logger = log
        test_url = 'example.com/utf8%3D%E2%9C%93%26replace%3D%99'
        result = test_action.decode_url(test_url, errors='ignore')

        actual = 'example.com/utf8=✓&replace='
        self.assertEqual(result, actual)
