import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.view_file import ViewFile
from komand_cuckoo.actions.view_file.schema import ViewFileOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestViewFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ViewFile())

    @parameterized.expand(
        [
            [
                "Success_md5",
                Util.read_file_to_dict("input/view_file_md5_success.json.inp"),
                Util.read_file_to_dict("expected/view_file_success.json.exp"),
            ],
            [
                "Success_sha",
                Util.read_file_to_dict("input/view_file_sha_success.json.inp"),
                Util.read_file_to_dict("expected/view_file_success.json.exp"),
            ],
            [
                "Success_id",
                Util.read_file_to_dict("input/view_file_id_success.json.inp"),
                Util.read_file_to_dict("expected/view_file_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_view_file(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, ViewFileOutput.schema)
