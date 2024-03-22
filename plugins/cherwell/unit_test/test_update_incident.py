import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.update_incident import UpdateIncident
from komand_cherwell.actions.update_incident.schema import UpdateIncidentOutput
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestUpdateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateIncident())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/update_incident_success.json.inp"),
                Util.read_file_to_dict("expected/update_incident_success.json.exp"),
            ],
        ]
    )
    def test_update_incident(self, mock_request, test_name, input, expected):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, UpdateIncidentOutput.schema)
