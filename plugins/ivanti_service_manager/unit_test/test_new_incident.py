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
from unit_test.mock import MockResponse
from insightconnect_plugin_runtime.exceptions import PluginException


# Mocks the trigger's send request
class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


@patch("")
class TestNewIncident(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(NewIncident())

    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.helper.open_cachefile", mock_open(read_data='{"12345"}'))
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_new_incident_some_function_to_test(self, _mock_get, _mock_send):
        try:
            self.action.run({Input.FREQUENCY: 10}0
        except PluginException:
            #Expect the plugin exception due to enforced timeout to allow exit from waiting for new incidents
            expected = {
                "incident": {}
            }
            # Check that the trigger function was called with the correct input
            TestCase.assertEqual(TestCase(), MockTrigger.actual, expected)
