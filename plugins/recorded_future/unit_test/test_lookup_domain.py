import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_recorded_future.connection.connection import Connection
from komand_recorded_future.actions.lookup_domain import LookupDomain
import json
import logging


class TestLookupDomain(TestCase):
    # def test_integration_lookup_domain(self):
    #      log = logging.getLogger("Test")
    #     test_conn = Connection()
    #     test_action = LookupDomain()
    #
    #     test_conn.logger = log
    #     test_action.logger = log
    #
    #     try:
    #         with open("../tests/lookup_domain.json") as file:
    #             test_json = json.loads(file.read()).get("body")
    #             connection_params = test_json.get("connection")
    #             action_params = test_json.get("input")
    #     except Exception as e:
    #         message = """
    #         Could not find or read sample tests from /tests directory
    #
    #         An exception here likely means you didn't fill out your samples correctly in the /tests directory
    #         Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
    #         """
    #         self.fail(message)
    #
    #     test_conn.connect(connection_params)
    #     test_action.connection = test_conn
    #     results = test_action.run(action_params)
    #
    #     self.assertIsNotNone(results)
    #     self.assertTrue("entity" in results.keys())
    #     self.assertTrue("analystNotes" in results.keys())
    #     self.assertTrue("metrics" in results.keys())
    #     self.assertTrue("risk" in results.keys())

    def test_get_domain(self):
        log = logging.getLogger("Test")
        test_action = LookupDomain()

        actual = test_action.get_domain("www.google.com")
        self.assertEquals(actual, "www.google.com")

        actual = test_action.get_domain("google.gs")
        self.assertEquals(actual, "google.gs")

        actual = test_action.get_domain("http://google.gs")
        self.assertEquals(actual, "google.gs")

        actual = test_action.get_domain("https://www.google.gs")
        self.assertEquals(actual, "www.google.gs")

        actual = test_action.get_domain("https://www.example.com/path/to/file")
        self.assertEquals(actual, "www.example.com")
