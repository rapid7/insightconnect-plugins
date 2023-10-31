import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from komand_whois.connection.connection import Connection
from komand_whois.actions.domain import Domain
from parameterized import parameterized
from util import Util
import json
import logging


class TestDomain(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Domain())

    def test_integration_domain(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Domain()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/domain.json") as file:
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

    @parameterized.expand(
        [
            [
                "domain",
                Util.read_file_to_dict("inputs/domain.json.inp"),
                Util.read_file_to_dict("expected/domain.json.exp")
            ]
        ]
    )
    def test_domain(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEquals(actual, expected)


