import sys
import os


sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_jira_service_management.actions.create_alert import CreateAlert
from icon_jira_service_management.actions.create_alert.schema import CreateAlertInput, CreateAlertOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send", side_effect=Util.mocked_requests)
class TestCreateAlert(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateAlert())

    def test_create_alert_success(self, mock_request):
        input_params = Util.read_file_to_dict("inputs/create_alert_all_fields.json.inp")
        expected = Util.read_file_to_dict("expected/create_alert_success.json.exp")

        actual = self.action.run(input_params)
        validate(actual, CreateAlertOutput.schema)
        self.assertEqual(actual, expected)
