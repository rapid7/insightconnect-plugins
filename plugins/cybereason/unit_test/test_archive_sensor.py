import json
import sys
import os

sys.path.append(os.path.abspath("../"))
# Custom Imports

from unittest.mock import patch
from icon_cybereason.actions.archive_sensor.schema import Input
from unittest import TestCase
from icon_cybereason.actions.archive_sensor import ArchiveSensor
from unit_test.util import Util


class TestArchiveSensor(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ArchiveSensor())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_archive_sensor(self, mock_request):
        actual = self.action.run(
            {
                Input.SENSOR_IDS: ["5e77883de4b0575ddcf824ef:PylumClient_integration_6999418007474704516"],
                Input.ARGUMENT: "Unused Sensor",
            }
        )
        expected = '"batchId": -12345678'
        assert json.dumps(actual).__contains__(expected)
        # find a way to make this shi work
