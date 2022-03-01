import sys
import os
from pathlib import Path
from unittest import TestCase, mock
from icon_carbon_black_response.connection.connection import Connection
from icon_carbon_black_response.actions.uninstall_sensor import UninstallSensor
from cbapi import CbResponseAPI
import logging

sys.path.append(str(Path("../").absolute()))


class TestUninstallSensors(TestCase):
    def setUp(self) -> None:
        self.action = UninstallSensor()
        self.connection = Connection()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "id": "12"
        }

    @mock.patch("CbResponseAPI.put_object")
    def test_uninstall_sensor_ok(self, mock_put):
        self.action.run(self.params)
        mock_put.assert_called_once_with("12")
