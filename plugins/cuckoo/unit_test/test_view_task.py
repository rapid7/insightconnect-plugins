import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.view_task import ViewTask
from komand_cuckoo.actions.view_task.schema import ViewTaskOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestViewTask(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ViewTask())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/view_task_success.json.inp"),
                Util.read_file_to_dict("expected/view_task_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_view_task(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, ViewTaskOutput.schema)
