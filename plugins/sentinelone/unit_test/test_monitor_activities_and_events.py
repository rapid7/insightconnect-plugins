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
  pass