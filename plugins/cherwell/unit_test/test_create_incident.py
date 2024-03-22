import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.create_incident import CreateIncident
from komand_cherwell.actions.create_incident.schema import CreateIncidentOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestCreateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateIncident())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/create_incident_success.json.inp"),
                Util.read_file_to_dict("expected/create_incident_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_file(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, CreateIncidentOutput.schema)