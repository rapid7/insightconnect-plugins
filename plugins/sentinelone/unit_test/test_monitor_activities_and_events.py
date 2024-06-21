import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.tasks.monitor_activities_and_events import MonitorActivitiesAndEvents
from komand_sentinelone.tasks.monitor_activities_and_events.schema import MonitorActivitiesAndEventsOutput
from util import Util
from parameterized import parameterized
from jsonschema import validate


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMonitorActivitiesAndEvents(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MonitorActivitiesAndEvents())

    def test_monitor_activities_and_events(self, mock_request, test_name, input_params, expected):
      actual = self.action.run(input_params)
      self.assertEqual(expected, actual)
      validate(actual, MonitorActivitiesAndEventsOutput.schema)

    def test_monitor_activites_and_events_api_errors(self):
      pass

    def test_monitor_activitites_and_events_forbidden_error(self):
      pass