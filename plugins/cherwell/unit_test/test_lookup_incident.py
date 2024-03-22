import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.lookup_incident import LookupIncident
from komand_cherwell.actions.lookup_incident.schema import LookupIncidentOutput
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mock_request)
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
    def test_lookup_incident(self, mock_request, test_name, input, expected):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, LookupIncidentOutput.schema)

    @parameterized.expand(
        [
            [
                "400",
                Util.read_file_to_dict("inputs/lookup_incident_400.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 400 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
            [
                "401",
                Util.read_file_to_dict("inputs/lookup_incident_401.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 401 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
            [
                "403",
                Util.read_file_to_dict("inputs/lookup_incident_403.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 403 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
            [
                "404",
                Util.read_file_to_dict("inputs/lookup_incident_404.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 404 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
            [
                "409",
                Util.read_file_to_dict("inputs/lookup_incident_409.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 409 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
            [
                "500",
                Util.read_file_to_dict("inputs/lookup_incident_500.json.inp"),
                "An error was received when running Lookup Incident.",
                "Request status code of 500 was returned. Please make sure connections have been configured correctly as well as the correct input for the action.",
                "Response was: {}",
            ],
        ]
    )
    def test_lookup_incident_errors(self, mock_request, test_name, input_params, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)
