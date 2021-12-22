"""Test Cases for the Qradar Connection."""
import json
import logging
import os
import sys
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import ClientException

from icon_ibm_qradar.connection.connection import Connection

sys.path.append(os.path.abspath("../"))


class TestConnection(TestCase):
    """Test Qradar Connection."""

    def test_integration_connection_test(self):
        """To Test the integration connection with qradar."""
        log = logging.getLogger("Test")
        test_conn = Connection()

        test_conn.logger = log

        try:
            with open("tests/start_ariel_search.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except FileNotFoundError:
            message = """
            Could not find or read sample tests from /tests directory"""
            self.fail(message)

        try:
            test_conn.connect(connection_params)
        except ClientException:
            self.fail()

    def test_integration_connection_test_with_wrong_credentials(self):
        """To Test the integration connection with qradar."""
        log = logging.getLogger("Test")
        test_conn = Connection()

        test_conn.logger = log

        try:
            with open("tests/start_ariel_search.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                connection_params["username"] = ""
        except FileNotFoundError:
            message = """
            Could not find or read sample tests from /tests directory"""
            self.fail(message)

        with self.assertRaises(ClientException):
            test_conn.connect(connection_params)
