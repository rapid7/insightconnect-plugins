import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.update_incident.schema import Input
from icon_ivanti_service_manager.actions.update_incident import UpdateIncident
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request


class TestUpdateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "customer": "user@example.com",
            "assignee": "John Doe",
            "status": "Logged",
            "category": "How-To",
            "cause_code": "Software",
            "resolution": "This incident was resolved by InsightConnect",
            "incident_number_good": 12345,
            "incident_number_bad": 54321,
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(UpdateIncident())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_update_incident_success(self, _mock_req):
        actual = self.action.run(
            {
                Input.STATUS: self.params.get("category"),
                Input.CAUSE_CODE: self.params.get("cause_code"),
                Input.RESOLUTION: self.params.get("resolution"),
                Input.INCIDENT_NUMBER: self.params.get("incident_number_good"),
            }
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_update_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_update_incident_fail_no_action_input(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run({Input.INCIDENT_NUMBER: self.params.get("incident_number")})
        cause = "At least one action input is required."
        self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_update_incident_fail(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.STATUS: self.params.get("category"),
                    Input.CAUSE_CODE: self.params.get("cause_code"),
                    Input.RESOLUTION: self.params.get("resolution"),
                    Input.INCIDENT_NUMBER: self.params.get("incident_number_bad"),
                }
            )
        cause = "Something unexpected occurred."
        self.assertEqual(exception.exception.cause, cause)
