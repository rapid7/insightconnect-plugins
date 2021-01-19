import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightidr.connection.connection import Connection
from komand_rapid7_insightidr.actions.advanced_query_on_log_set import AdvancedQueryOnLogSet
from komand.exceptions import PluginException
import json
import logging


class TestAdvancedQueryOnLogSet(TestCase):
    def setup(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AdvancedQueryOnLogSet()
        test_conn.logger = log
        test_action.logger = log
        try:
            with open("../tests/advanced_query_on_log_set.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            self.fail("Likely could not find tests in test directory. Generate and fill out samples to fix this.")
        return action_params, connection_params, test_action, test_conn

    def test_integration_advanced_query(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertTrue("results" in results.keys())
        self.assertTrue(len(results.get("results")) > 0)

    def test_get_log(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        result = test_action.get_log_set_id("Asset Authentication")

        self.assertIsNotNone(result) # Best we can do here, the log ID will change based on the instance used.

    def test_get_log_fails(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        with self.assertRaises(PluginException):
            test_action.get_log_set_id("Do not find this log")

    def test_parse_dates(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn

        time_test1 = "2005/10/31T17:11:09"
        time_test2 = "01-01-2020"
        time_test3 = "01-01-2020T18:01:01"
        time_test4 = "02/24/1978"
        time_test5 = "13:25"
        time_test6 = "01/27/2020 10:00 PM"
        time_test7 = "01-01-2020"
        time_test8 = "12-31-2020"

        res1, res2 = test_action.parse_dates(time_test1, time_test2)
        res3, res4 = test_action.parse_dates(time_test3, time_test4)
        res5, res6 = test_action.parse_dates(time_test5, time_test6)
        res7, res8 = test_action.parse_dates(time_test7, time_test8)

        self.assertEquals(res1, 1130800269000)
        self.assertEquals(res2, 1577858400000)
        self.assertEquals(res3, 1577923261000)
        self.assertEquals(res4, 257148000000)
        self.assertIsNotNone(res5) # This will be today @ 1:25 PM.
        self.assertEquals(res6, 1580184000000)
        self.assertEquals(res7, 1577858400000)
        self.assertEquals(res8, 1609394400000)

        not_used, now_result = test_action.parse_dates(time_test1, None)
        self.assertIsNotNone(now_result)

        with self.assertRaises(PluginException):
            test_action.parse_dates("AAA", None)
