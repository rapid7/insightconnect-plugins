import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.list_machines import ListMachines
from komand_cuckoo.actions.list_machines.schema import ListMachinesOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestListMachines(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListMachines())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("expected/list_machines_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_list_machines(self, test_name, expected, mock_request):
        actual = self.action.run()
        self.assertEqual(expected, actual)
        validate(actual, ListMachinesOutput.schema)
