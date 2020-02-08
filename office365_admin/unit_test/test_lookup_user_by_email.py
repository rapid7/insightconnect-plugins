import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_office365_admin.connection.connection import Connection
from komand_office365_admin.actions.lookup_user_by_email import LookupUserByEmail
import json
import logging


class TestLookupUserByEmail(TestCase):
    def test_integration_lookup_user_by_email(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = LookupUserByEmail()

        test_conn.logger = log
        test_action.logger = log

        with open("../tests/lookup_user_by_email.json") as file:
            test_json = json.loads(file.read()).get("body")
            connection_params = test_json.get("connection")
            action_params = test_json.get("input")

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(results['user']['value'], [], "user -> values is an empty array")

        #jmcadams@komanddev.onmicrosoft.com
        user_is_there_params = {"email_address" : "jmcadams@komanddev.onmicrosoft.com"}
        user_is_there_results = test_action.run(user_is_there_params)
        self.assertNotEqual({}, user_is_there_results, "returns non - empty results")
        self.assertEqual(1, len(user_is_there_results['user']['value']), "there is 1 user returned")
        self.assertEqual(user_is_there_results['user']['value'][0]['givenName'], 'Joey', "user -> values -> 0 -> givenName is Joey")

        empty_params = {}
        empty_results = test_action.run(empty_params)
        self.assertEqual({}, empty_results, "returns empty results")


