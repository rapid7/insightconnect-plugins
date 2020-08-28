import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.add_to_udso_list import AddToUdsoList
from komand.exceptions import PluginException
import json
import logging

from requests.packages.urllib3 import exceptions
import warnings
warnings.simplefilter('ignore', exceptions.InsecureRequestWarning)

class TestAddToUdsoList(TestCase):
    def test_integration_add_to_udso_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddToUdsoList()

        test_conn.logger = log
        test_action.logger = log

        the_good_files = ["test_add_ip_to_udso_list.json",
                          "test_add_domain_to_udso_list.json",
                          "test_add_url_to_udso_list.json",
                          "test_add_sha_to_udso_list.json"]

        the_bad_files = ["test_add_ip_to_udso_list_bad.json",
                          "test_add_domain_to_udso_list_bad.json",
                          "test_add_url_to_udso_list_bad1.json",
                          "test_add_url_to_udso_list_bad2.json"]

        for test_file in the_good_files:
            try:
                file_to_open = "../tests/" + test_file
                with open(file_to_open) as file:
                    test_json = json.loads(file.read()).get("body")
                    connection_params = test_json.get("connection")
                    action_params = test_json.get("input")
            except Exception as e:
                message = f"Could not read sample test file {file_to_open}.  Exception is: {e}"
                self.fail(message)


            test_conn.connect(connection_params)
            test_action.connection = test_conn
            results = test_action.run(action_params)

            self.assertEqual({"success": True}, results)

        for test_file in the_bad_files:
            try:
                file_to_open = "../tests/" + test_file
                with open(file_to_open) as file:
                    test_json = json.loads(file.read()).get("body")
                    connection_params = test_json.get("connection")
                    action_params = test_json.get("input")
            except Exception as e:
                message = f"Could not read sample test file {file_to_open}.  Exception is: {e}"
                self.fail(message)

            test_conn.connect(connection_params)
            test_action.connection = test_conn

            print(f"testing file 8888888 : {file_to_open}")
            self.assertRaises(PluginException, test_action.run, action_params)
