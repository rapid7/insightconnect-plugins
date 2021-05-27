import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_devo.util.api import DevoAPI
from icon_devo.connection.connection import Connection
import json
import logging


class TestQueryLogs(TestCase):
    def test_integration_connection_test(self):
        try:
            with open("../tests/query_logs.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            self.fail()

        test_connection = Connection()
        test_connection.logger = logging.getLogger("Test")
        test_connection.connect(connection_params)
        test_api = test_connection.api

        test_api.test_connection()

    def test_convert_time(self):
        test_api = DevoAPI(logging.getLogger("Test"), api_token="some_token", region="USA")

        actual = test_api._convert_time_to_epoch("now")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("Now")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("2 hours ago")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("1/24/2000")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("1/24/2000 12:00:00")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("1/1/2000T12:00:00")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("5 minutes ago")
        self.assertIsInstance(actual, int)
        actual = test_api._convert_time_to_epoch("24 hours ago")
        self.assertIsInstance(actual, int)

        with self.assertRaises(PluginException):
            test_api._convert_time_to_epoch("some gibberish that doesn't mean anything")

