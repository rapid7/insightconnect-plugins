import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.list_tasks import ListTasks
from komand_cuckoo.actions.list_tasks.schema import ListTasksOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestListTasks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListTasks())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/list_tasks_success.json.inp"),
                Util.read_file_to_dict("expected/list_tasks_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_list_tasks(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, ListTasksOutput.schema)
