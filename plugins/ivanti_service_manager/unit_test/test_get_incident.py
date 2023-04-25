import sys
import os
import json
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from icon_ivanti_service_manager.actions.get_incident import GetIncident
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request
from unit_test.payload_stubs import STUB_GET_INCIDENT_PARAMETERS


@patch("requests.Session.request", side_effect=mock_request)
class TestGetIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetIncident())
        self.connection = self.action.connection

    @parameterized.expand(
        [
            ["12345"],
        ]
    )
    def test_get_incident_success(self, mock_request, incident_number):
        STUB_GET_INCIDENT_PARAMETERS["incident_number"] = incident_number
        actual = self.action.run(STUB_GET_INCIDENT_PARAMETERS)
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_get_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["54321", "Something unexpected occurred."],
        ]
    )
    def test_get_incident_fail(self, mock_request, incident_number, cause):
        with self.assertRaises(PluginException) as exception:
            STUB_GET_INCIDENT_PARAMETERS["incident_number"] = incident_number
            self.action.run(STUB_GET_INCIDENT_PARAMETERS)
        self.assertEqual(exception.exception.cause, cause)
