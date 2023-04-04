import sys
import os
import json

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from unit_test.payload_stubs import STUB_CREATE_INCIDENT_PARAMETERS
from unit_test.mock import mock_request
from icon_ivanti_service_manager.actions.create_incident import CreateIncident
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=mock_request)
class TestCreateIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateIncident())
        self.connection = self.action.connection

    @parameterized.expand(
        [
            ["identifier"],
        ]
    )
    def test_create_incident_success(self, mock_request, customer):
        STUB_CREATE_INCIDENT_PARAMETERS["customer"] = customer
        actual = self.action.run(STUB_CREATE_INCIDENT_PARAMETERS)
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_create_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [["identifier_not_unique", "Multiple employees found."], ["no_identifier", "No employees found."]]
    )
    def test_create_incident_fail(self, mock_request, customer, cause):
        with self.assertRaises(PluginException) as exception:
            STUB_CREATE_INCIDENT_PARAMETERS["customer"] = customer
            self.action.run(STUB_CREATE_INCIDENT_PARAMETERS)
        self.assertEqual(exception.exception.cause, cause)
