import sys
import os

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.delete_incident import DeleteIncident
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request
from unit_test.payload_stubs import STUB_DELETE_INCIDENT_PARAMETERS


@patch("requests.Session.request", side_effect=mock_request)
class TestDeleteIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteIncident())
        self.connection = self.action.connection

    @parameterized.expand([[12345]])
    def test_delete_incident_success(self, mock_request, incident_number):
        STUB_DELETE_INCIDENT_PARAMETERS["incident_number"] = incident_number
        actual = self.action.run(STUB_DELETE_INCIDENT_PARAMETERS)
        expected = {"success": True}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [54321, "Something unexpected occurred."],
            [15243, "The response from the Ivanti Service Manager was not in the correct format."],
        ]
    )
    def test_delete_incident_fail(self, mock_request, incident_number, cause):
        with self.assertRaises(PluginException) as exception:
            STUB_DELETE_INCIDENT_PARAMETERS["incident_number"] = incident_number
            self.action.run(STUB_DELETE_INCIDENT_PARAMETERS)
        self.assertEqual(exception.exception.cause, cause)
