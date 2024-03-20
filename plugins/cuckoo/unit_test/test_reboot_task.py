import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.reboot_task import RebootTask
from komand_cuckoo.actions.reboot_task.schema import RebootTaskOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestRebootTask(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RebootTask())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/reboot_task_success.json.inp"),
                Util.read_file_to_dict("expected/reboot_task_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_reboot_task(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, RebootTaskOutput.schema)
