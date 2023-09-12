import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_servicenow.actions.get_security_incident import GetSecurityIncident
from icon_servicenow.actions.get_security_incident.schema import GetSecurityIncidentOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetSecurityIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetSecurityIncident())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/get_security_incident_success.json.inp"),
                Util.read_file_to_dict("expected/get_security_incident_success.json.exp"),
            ],
        ]
    )
    def test_get_security_incident(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        validate(actual, GetSecurityIncidentOutput.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_sys_id",
                Util.read_file_to_dict("inputs/get_security_incident_invalid_id.json.inp"),
                "Error in API request to ServiceNow. ",
                """Status code: 404, Error: {'error': {'message': 'No Record found', 'detail': "Record doesn't exist or ACL restricts the record retrieval"}, 'status': 'failure'}""",
            ],
        ]
    )
    def test_get_security_incident_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
