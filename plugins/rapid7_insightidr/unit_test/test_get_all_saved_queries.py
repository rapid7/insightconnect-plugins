import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_rapid7_insightidr.actions.get_all_saved_queries.action import GetAllSavedQueries
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput
from komand_rapid7_insightidr.actions.get_all_saved_queries.schema import GetAllSavedQueriesOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from mock import (
    mock_get_request,
)
import logging
from jsonschema import validate


class TestGetAllSavedQueries(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(GetAllSavedQueries())
        self.connection = self.action.connection

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_get_all_saved_queries(self, _mock_req):
        actual = self.action.run()
        expected = {
            "saved_queries": [
                {
                    "id": "00000000-0000-1eec-0000-000000000000",
                    "leql": {
                        "during": {"from": 1234567890, "time_range": "yesterday", "to": 1234567890},
                        "statement": "where(931dde6c60>=800)",
                    },
                    "logs": ["bf8863fd-e46a-47b5-b117-0257564e43b9"],
                    "name": "Large Values Yesterday",
                },
                {
                    "id": "00000000-0000-2eec-0000-000000000000",
                    "leql": {
                        "during": {"from": 1234567890, "time_range": "yesterday", "to": 1234567890},
                        "statement": "where(931dde6c60>=800)",
                    },
                    "logs": ["55830c8d-de01-4dd0-8532-d5e0d79d6f1e"],
                    "name": "Large Values Today",
                },
                {
                    "id": "00000000-0000-3eec-0000-000000000000",
                    "leql": {
                        "during": {"from": 1234567890, "time_range": "yesterday", "to": 1234567890},
                        "statement": "where(931dde6c60>=800)",
                    },
                    "logs": ["a9cf11a2-82e3-4a73-8a77-682ec4bbd2ee"],
                    "name": "Large Values Tomorrow",
                },
            ]
        }
        self.assertEqual(actual, expected)
        validate(actual, GetAllSavedQueriesOutput.schema)
