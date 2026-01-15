import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from jsonschema import validate
from komand_rapid7_insightidr.actions.list_investigations import ListInvestigations
from komand_rapid7_insightidr.actions.list_investigations.schema import (
    Input,
    ListInvestigationsInput,
    ListInvestigationsOutput,
)
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestListInvestigations(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "query_id": "00000000-0000-1eec-0000-000000000000",
            "not_found_query_id": "00000000-0000-8eec-0000-000000000000",
            "invalid_query_id": "0000000-000-9ee-000-00000000000",
        }
        self.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(ListInvestigations())
        self.connection = self.action.connection

    def test_list_investigations(self, _mock_req) -> None:
        test_input = {
            Input.INDEX: 0,
            Input.SIZE: 1,
            Input.STATUSES: ["INVESTIGATING"],
            Input.SOURCES: ["USER", "ALERT"],
        }
        validate(test_input, ListInvestigationsInput.schema)
        actual = self.action.run(test_input)
        expected = {
            "investigations": [
                {
                    "assignee": {"email": "example@test.com", "name": "Ellen Example"},
                    "created_time": "2018-06-06T16:56:42Z",
                    "disposition": "BENIGN",
                    "first_alert_time": "2018-06-06T16:56:42Z",
                    "last_accessed": "2018-06-06T16:56:42Z",
                    "latest_alert_time": "2018-06-06T16:56:42Z",
                    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
                    "priority": "CRITICAL",
                    "rrn": "rrn:example",
                    "source": "ALERT",
                    "status": "INVESTIGATING",
                    "title": "Example Title",
                    "responsibility": "CUSTOMER",
                    "tags": ["Incident", "Security Test"],
                }
            ],
            "metadata": {"index": 0, "size": 1, "total_data": 1, "total_pages": 1},
        }
        self.assertEqual(actual, expected)
        validate(actual, ListInvestigationsOutput.schema)

    def test_list_attachments_bad(self, _mock_req) -> None:
        test_input = {Input.INDEX: 0, Input.SIZE: 1, Input.STATUSES: ["OPEN"], Input.SOURCES: ["INVALID_SOURCE"]}
        validate(test_input, ListInvestigationsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, PluginException.causes[PluginException.Preset.BAD_REQUEST])
        self.assertEqual(error.exception.assistance, PluginException.assistances[PluginException.Preset.BAD_REQUEST])
