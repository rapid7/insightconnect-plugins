import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from jsonschema import validate
from komand_rapid7_insightidr.actions.create_investigation import CreateInvestigation
from komand_rapid7_insightidr.actions.create_investigation.schema import (
    CreateInvestigationInput,
    CreateInvestigationOutput,
    Input,
)
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from mock_utils import STUB_USER_EMAIL, mock_post_request
from util import Util


class TestCreateInvestigation(TestCase):
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
        self.action = Util.default_connector(CreateInvestigation())
        self.connection = self.action.connection

    @patch("requests.Session.send", side_effect=mock_post_request)
    def test_create_investigation(self, _mock_req) -> None:
        test_input = {Input.TITLE: "Example Title", Input.EMAIL: STUB_USER_EMAIL}
        validate(test_input, CreateInvestigationInput.schema)
        actual = self.action.run(test_input)
        expected = {
            "investigation": {
                "assignee": {"email": "user@example.com", "name": "Ellen Example"},
                "created_time": "2018-06-06T16:56:42Z",
                "disposition": "BENIGN",
                "first_alert_time": "2018-06-06T16:56:42Z",
                "last_accessed": "2018-06-06T16:56:42Z",
                "latest_alert_time": "2018-06-06T16:56:42Z",
                "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
                "priority": "CRITICAL",
                "rrn": "rrn:example",
                "source": "ALERT",
                "status": "OPEN",
                "title": "Example Title",
            }
        }
        self.assertEqual(actual, expected)
        validate(actual, CreateInvestigationOutput.schema)
