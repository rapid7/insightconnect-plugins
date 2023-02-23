import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.delete_incident import DeleteIncident
from icon_ivanti_service_manager.actions.delete_incident.schema import Input
import icon_ivanti_service_manager.connection
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request


class TestDeleteIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "good_id": 12345,
            "bad_id": 54321
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteIncident())
        self.connection = self.action.connection

    # change to call api and sort out side_effect
    @patch("requests.Session.request", side_effect=mock_request)
    @patch("requests.Session.request", side_effect=mock_request)
    def test_delete_incident_success(self, _mock_req, _mock_req_2):
        actual = self.action.run({Input.INCIDENT_NUMBER: self.params.get("good_id")})
        expected = {"success": "true"}
        self.assertEqual(actual, expected)

    # # change to call api and sort out side_effect
    # @patch("api._call_api", side_effect=mock_request)
    # def test_delete_incident_fail(self, _mock_req):
    #     with self.assertRaises(PluginException) as exception:
    #         self.action.run({Input.INCIDENT_NUMBER: self.params.get("bad_id")})
    #     cause = "No incidents found."
    #     self.assertEqual(exception.exception.cause, cause)
