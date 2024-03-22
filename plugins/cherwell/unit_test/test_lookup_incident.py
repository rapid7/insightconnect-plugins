import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.lookup_incident import LookupIncident
from komand_cherwell.actions.lookup_incident.schema import LookupIncidentOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestLookupIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupIncident())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/lookup_incident_success.json.inp"),
                Util.read_file_to_dict("expected/lookup_incident_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_file(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, LookupIncidentOutput.schema)
