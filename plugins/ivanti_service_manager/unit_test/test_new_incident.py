import sys
import os
import timeout_decorator
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, mock_open
from icon_ivanti_service_manager.triggers.new_incident import NewIncident
from icon_ivanti_service_manager.triggers.new_incident.schema import Input
from unit_test.util import Util
from unit_test.mock import mock_request
from insightconnect_plugin_runtime.exceptions import PluginException


# Mocks the trigger's send request
class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


@patch("requests.Session.request", side_effect=mock_request)
class TestNewIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {"incident_number": 12345}

    def setUp(self) -> None:
        self.trigger = Util.default_connector(NewIncident())
        self.connection = self.trigger.connection

    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.helper.open_cachefile", mock_open(read_data='{"12345"}'))
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_new_incident_some_function_to_test(self, _mock_get, _mock_send):
        try:
            self.trigger.run({Input.FREQUENCY: 10})
        except PluginException:
            # Expect the plugin exception due to enforced timeout to allow exit from waiting for new incidents
            expected = {"incident": {"incident_number": 12345}}
            # Check that the trigger function was called with the correct input
            TestCase.assertEqual(TestCase(), MockTrigger.actual, expected)
