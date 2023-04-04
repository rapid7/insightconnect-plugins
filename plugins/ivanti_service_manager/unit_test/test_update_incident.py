import sys
import os
import json
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.update_incident.schema import Input
from icon_ivanti_service_manager.actions.update_incident import UpdateIncident
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request
from unit_test.payload_stubs import STUB_UPDATE_INCIDENT_PARAMETERS, STUB_UPDATE_INCIDENT_PARAMETERS_FAIL


@patch("requests.Session.request", side_effect=mock_request)
class TestUpdateIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(UpdateIncident())
        self.connection = self.action.connection

    @parameterized.expand(
        [
            [12345],
        ]
    )
    def test_update_incident_success(self, _mock_req, incident_number):
        STUB_UPDATE_INCIDENT_PARAMETERS["incident_number"] = incident_number
        actual = self.action.run(
            STUB_UPDATE_INCIDENT_PARAMETERS
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_update_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [54321, "Something unexpected occurred."],
            [12345, "At least one action input is required."],
        ]
    )
    def test_update_incident_fail(self, mock_request, incident_number, cause):
        _input = None
        if incident_number == 12345:
            _input = STUB_UPDATE_INCIDENT_PARAMETERS_FAIL
        else:
            STUB_UPDATE_INCIDENT_PARAMETERS["incident_number"] = incident_number
            _input = STUB_UPDATE_INCIDENT_PARAMETERS
        with self.assertRaises(PluginException) as exception:
            self.action.run(_input)
        self.assertEqual(exception.exception.cause, cause)

