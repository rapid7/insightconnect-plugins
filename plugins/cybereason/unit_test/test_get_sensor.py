import json
import sys
import os

sys.path.append(os.path.abspath('../'))
# Custom Imports

from unittest.mock import patch
from icon_cybereason.actions.get_sensor.schema import Input
from unittest import TestCase
from icon_cybereason.actions.get_sensor import GetSensor
from unit_test.util import Util


class TestGetSensor(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetSensor())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_get_sensor(self, mock_request):
        actual = self.action.run(
            {
                Input.INDICATOR: "10.100.229.174",
            }
        )
        expected = '"sensorId": "valid_sensor_Id"'
        assert json.dumps(actual).__contains__(expected)

# add test that get different status codes
