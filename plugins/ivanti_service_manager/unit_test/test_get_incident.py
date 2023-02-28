import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from icon_ivanti_service_manager.actions.get_incident.schema import Input
from icon_ivanti_service_manager.actions.get_incident import GetIncident
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request


class TestGetIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {"good_id": 12345, "bad_id": 54321}

    def setUp(self) -> None:
        self.action = Util.default_connector(GetIncident())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_get_incident_success(self, _mock_req):
        actual = self.action.run({Input.INCIDENT_NUMBER: self.params.get("good_id")})
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_get_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_get_incident_fail(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run({Input.INCIDENT_NUMBER: self.params.get("bad_id")})
        cause = "Something went wrong"
        self.assertEqual(exception.exception.cause, cause)
