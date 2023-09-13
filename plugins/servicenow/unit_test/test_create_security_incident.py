import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_servicenow.actions.create_security_incident import CreateSecurityIncident
from icon_servicenow.actions.create_security_incident.schema import CreateSecurityIncidentOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestCreateSecurityIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateSecurityIncident())

    @parameterized.expand(
        [
            [
                "only_required_field",
                Util.read_file_to_dict("inputs/create_security_incident_only_required_field.json.inp"),
                Util.read_file_to_dict("expected/create_security_incident_success.json.exp"),
            ],
            [
                "all_fields",
                Util.read_file_to_dict("inputs/create_security_incident_all_fields.json.inp"),
                Util.read_file_to_dict("expected/create_security_incident_success.json.exp"),
            ],
        ]
    )
    def test_create_security_incident(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        validate(actual, CreateSecurityIncidentOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "missing_field",
                Util.read_file_to_dict("inputs/create_security_incident_missing_field.json.inp"),
                "An attempt was made to assign the user test_user responsible for this incident, but the assignment group was not provided.",
                "To assign a user responsible for a given incident, the assignment group must also be provided.",
            ]
        ]
    )
    def test_create_security_incident_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
