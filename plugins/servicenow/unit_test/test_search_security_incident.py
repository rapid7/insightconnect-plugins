import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_servicenow.actions.search_security_incident import SearchSecurityIncident
from icon_servicenow.actions.search_security_incident.schema import SearchSecurityIncidentOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestSearchSecurityIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchSecurityIncident())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/search_security_incident_all.json.inp"),
                Util.read_file_to_dict("expected/search_security_incident_all.json.exp"),
            ],
            [
                "given_query",
                Util.read_file_to_dict("inputs/search_security_incident_query.json.inp"),
                Util.read_file_to_dict("expected/search_security_incident_query.json.exp"),
            ],
            [
                "given_limit_and_offset",
                Util.read_file_to_dict("inputs/search_security_incident_limit_offset.json.inp"),
                Util.read_file_to_dict("expected/search_security_incident_limit_offset.json.exp"),
            ],
            [
                "given_fields",
                Util.read_file_to_dict("inputs/search_security_incident_fields.json.inp"),
                Util.read_file_to_dict("expected/search_security_incident_fields.json.exp"),
            ],
            [
                "empty_list",
                Util.read_file_to_dict("inputs/search_security_incident_empty_list.json.inp"),
                Util.read_file_to_dict("expected/search_security_incident_empty_list.json.exp"),
            ],
        ]
    )
    def test_get_security_incident(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        validate(actual, SearchSecurityIncidentOutput.schema)
        self.assertDictEqual(actual, expected)
