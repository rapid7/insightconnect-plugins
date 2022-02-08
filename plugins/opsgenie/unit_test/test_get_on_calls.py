import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_opsgenie.actions.get_on_calls import GetOnCalls
from icon_opsgenie.actions.get_on_calls.schema import Output
from icon_opsgenie.connection.connection import Connection
from icon_opsgenie.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    STUB_SCHEDULE_ID,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestGetOnCalls(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.API_KEY: {"secretKey": "1234567e-123c-123c-123c-1234567e9xAd"}})

        self.action = GetOnCalls()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {"scheduleIdentifier": STUB_SCHEDULE_ID, "date": "2017-01-15T08:00:00+02:00"}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_on_calls_when_status_ok(self, mock_get):
        response = self.action.run(self.params)
        expected_response = {
            Output.DATA: {
                "_parent": {"id": "d875alp4-9b4e-4219-alp3-0c26936d18de", "name": "ScheduleName", "enabled": True},
                "onCallParticipants": [
                    {"id": "c569c016-alpc-4e20-8a28-bd5dc33b798e", "name": "TeamName", "type": "team"},
                    {
                        "id": "15445alp-e46c-446f-9236-7ad89ad1a4f7",
                        "name": "TeamName_escalation",
                        "type": "escalation",
                        "onCallParticipants": [
                            {
                                "id": "e55700e1-ff76-4cd0-a6e8-e1a982423alp",
                                "name": "TeamName_schedule",
                                "type": "schedule",
                                "escalationTime": 0,
                                "notifyType": "default",
                            },
                            {
                                "id": "e55700e1-ff76-4cd0-a6e8-e1a982423alp",
                                "name": "TeamName_schedule",
                                "type": "schedule",
                                "escalationTime": 5,
                                "notifyType": "next",
                            },
                            {
                                "id": "c569c016-alpc-4e20-8a28-bd5dc33b798e",
                                "name": "TeamName",
                                "type": "team",
                                "onCallParticipants": [
                                    {
                                        "id": "balp7783-a9f1-40e3-940c-ffde45656054",
                                        "name": "user5@opsgenie.com",
                                        "type": "user",
                                    },
                                    {
                                        "id": "4falpb2e-348d-4b7c-b71b-149efb8361e4",
                                        "name": "user4@opsgenie.com",
                                        "type": "user",
                                    },
                                ],
                                "escalationTime": 10,
                                "notifyType": "all",
                            },
                        ],
                    },
                ],
            },
            Output.ELAPSED_TIME: 0.305,
            Output.REQUESTID: "e28ce37b-d81c-4b1d-abb8-0c371d8alp5f",
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.NOT_FOUND),
            (mock_request_500, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_get_on_calls_when_status_error(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
