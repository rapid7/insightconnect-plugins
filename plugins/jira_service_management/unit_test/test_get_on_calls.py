import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import patch

from icon_jira_service_management.actions.get_on_calls import GetOnCalls
from icon_jira_service_management.actions.get_on_calls.schema import GetOnCallsOutput
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send")
class TestGetOnCalls(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetOnCalls())

    def test_get_on_calls(self, mock_send: mock.Mock):
        mock_send.side_effect = [
            Util.MockResponse("get_on_calls_request.json", 200),
        ]

        input_params = {
            "identifier": "111111-9999-4ec2-8067-acde6abc040-1111123123",
        }

        expected = {
            "data": {
                "onCallParticipants": [
                    {"id": "bc667897-cb21-496f-a46e-7c05ff0419dd", "type": "team"},
                    {"id": "5b2b0e011b3a756623f4e25e", "type": "user"},
                    {
                        "id": "7a24e9d7-7a4f-4f86-a1df-21ca9c3112ac",
                        "type": "escalation",
                        "onCallParticipants": [
                            {
                                "id": "5b2b0e011b3a756623f4e25e",
                                "type": "user",
                                "forwardedFrom": {"id": "c5646941-3f05-404d-8594-825fa73af99f", "type": "user"},
                            }
                        ],
                    },
                ]
            }
        }

        actual = self.action.run(input_params)
        validate(actual, GetOnCallsOutput.schema)
        self.assertEqual(actual, expected)
