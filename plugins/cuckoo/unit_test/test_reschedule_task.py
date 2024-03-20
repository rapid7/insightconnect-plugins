import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.reschedule_task import RescheduleTask
from komand_cuckoo.actions.reschedule_task.schema import RescheduleTaskOutput

from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate

class TestRescheduleTask(TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    cls.action = Util.default_connector(RescheduleTask())

  @parameterized.expand(
    [
      [
        "Success",
        Util.read_file_to_dict("input/reschedule_task_success.json.inp"),
        Util.read_file_to_dict("expected/reschedule_task_success.json.exp"),
      ],
    ]
  )
  @patch("requests.request", side_effect=Util.mock_request)
  def test_reschedule_task(self, test_name, input, expected, mock_request):
    actual = self.action.run(input)
    self.assertEqual(expected, actual)
    validate(actual, RescheduleTaskOutput.schema)
