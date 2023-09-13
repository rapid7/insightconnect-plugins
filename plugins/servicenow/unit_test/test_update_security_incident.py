import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_servicenow.actions.update_security_incident import UpdateSecurityIncident
from icon_servicenow.actions.update_security_incident.schema import UpdateSecurityIncidentOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.patch", side_effect=Util.mocked_requests)
class TestUpdateSecurityIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateSecurityIncident())

    @parameterized.expand(
        [
            [
                "only_one_field",
                Util.read_file_to_dict("inputs/update_security_incident_only_one_field.json.inp"),
                Util.read_file_to_dict("expected/update_security_incident_success.json.exp"),
            ],
            [
                "all_fields",
                Util.read_file_to_dict("inputs/update_security_incident_all_fields.json.inp"),
                Util.read_file_to_dict("expected/update_security_incident_success.json.exp"),
            ],
        ]
    )
    def test_update_security_incident(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        validate(actual, UpdateSecurityIncidentOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/update_security_incident_invalid_id.json.inp"),
                "Error in API request to ServiceNow. ",
                "Status code: 404, Error: {'error': {'message': 'No Record found', 'detail': \"Record doesn't exist or ACL restricts the record retrieval\"}, 'status': 'failure'}",
            ]
        ]
    )
    def test_update_security_incident_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
