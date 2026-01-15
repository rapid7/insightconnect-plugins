import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from jsonschema import validate
from komand_rapid7_insightidr.actions.create_threat import CreateThreat
from komand_rapid7_insightidr.actions.create_threat.schema import CreateThreatInput, CreateThreatOutput, Input
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestCreateThreat(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            Input.INDICATORS: ["example.com", "10.0.0.1"],
            Input.NOTE_TEXT: "Threat created via InsightConnect",
            Input.THREAT_NAME: "Threat created via InsightConnect",
        }
        cls.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(CreateThreat())
        self.connection = self.action.connection

    def test_create_a_threat(self, _mock_req) -> None:
        validate(self.params, CreateThreatInput.schema)
        actual = self.action.run(self.params)
        expected = {
            "rejected_indicators": ["example.com", "10.0.0.1"],
            "threat": {
                "indicator_count": 2,
                "name": "Threat created via InsightConnect",
                "note": "Threat created via InsightConnect",
                "published": False,
            },
        }
        self.assertEqual(actual, expected)
        validate(actual, CreateThreatOutput.schema)
