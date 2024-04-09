import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.create_incident import CreateIncident
from komand_cherwell.actions.create_incident.schema import CreateIncidentOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestCreateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateIncident())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/create_incident_success.json.inp"),
                Util.read_file_to_dict("expected/create_incident_success.json.exp"),
            ],
        ]
    )
    def test_create_incident(self, mock_request, test_name, input, expected):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, CreateIncidentOutput.schema)

    @parameterized.expand(
        [
            [
                "http_scheme",
                Util.read_file_to_dict("inputs/create_incident_success.json.inp"),
                "The input URL does not contain a scheme",
                "Ensure the URL begins wih https:// or http://",
            ]
        ]
    )
    def test_create_incident_scheme_error(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action = Util.default_connector(action=CreateIncident(), custom_params={"url": "0.0.0.0"})
            self.action.run(input_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
