import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from jsonschema import validate
from komand_rapid7_insightidr.actions.get_a_log import GetALog
from komand_rapid7_insightidr.actions.get_a_log.schema import GetALogInput, GetALogOutput, Input
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetALog(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {Input.ID: "test_id"}
        cls.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(GetALog())
        self.connection = self.action.connection

    def test_get_a_log(self, _mock_req) -> None:
        validate(self.params, GetALogInput.schema)
        actual = self.action.run(self.params)
        expected = {
            "log": {
                "log": {
                    "id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f",
                    "links": [{"href": "https://example.com", "rel": "Related"}],
                    "logsets_info": [
                        {
                            "id": "bc38a911-65f1-4755-cca3-a330a6336b3a",
                            "links": [
                                {"href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85", "rel": "Self"}
                            ],
                            "name": "Unparsed Data",
                            "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a",
                        }
                    ],
                    "name": "Windows Defender",
                    "retention_period": "default",
                    "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a",
                    "source_type": "token",
                    "structures": ["1238a911-65f1-4755-cca3-a330a6336b3a"],
                    "token_seed": None,
                    "tokens": ["bc38a911-65f1-4755-cca3-a330a6336b3a"],
                    "user_data": {"platform_managed": "true"},
                }
            }
        }
        self.assertEqual(actual, expected)
        validate(actual, GetALogOutput.schema)
