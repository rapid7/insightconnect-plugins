import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.delete_task import DeleteTask
from komand_cuckoo.actions.delete_task.schema import DeleteTaskOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestDeleteTask(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteTask())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/delete_task_success.json.inp"),
                Util.read_file_to_dict("expected/delete_task_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_delete_task(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, DeleteTaskOutput.schema)
