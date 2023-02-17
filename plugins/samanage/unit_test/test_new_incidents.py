import sys
import os
import logging
import json
import timeout_decorator


sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, mock_open
from komand_samanage.connection.connection import Connection
from komand_samanage.triggers.new_incidents import NewIncidents
from komand_samanage.triggers.new_incidents.schema import Input
from unit_test.util import Util, mock_request_200
from typing import Callable, Optional
from insightconnect_plugin_runtime.exceptions import PluginException


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestNewIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(NewIncidents())

    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.helper.open_cachefile", mock_open(read_data='{"20000"}'))
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_new_incidents(self, mock_get, mock_send):
        try:
            self.action.run({Input.FREQUENCY: 10})
        except PluginException:
            # Expect the plugin exception due to enforced timeout to allow exit from waiting for new incidents
            expected = {
                "incident": {
                    "id": 10000,
                    "number": "1000",
                    "name": "Incident Example Name",
                    "description": "Example incident description",
                    "state": "New",
                    "site": {"id": 1, "name": "Austin TX, USA", "location": "AUS"},
                }
            }
            # Check that the trigger function (mocked) was called with the correct input
            TestCase.assertEqual(TestCase(), MockTrigger.actual, expected)
