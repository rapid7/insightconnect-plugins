import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.get_screenshots import GetScreenshots
from komand_cuckoo.actions.get_screenshots.schema import GetScreenshotsOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestGetScreenshots(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetScreenshots())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/get_screenshots_success.json.inp"),
                Util.read_file_to_dict("expected/get_screenshots_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_screenshots(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, GetScreenshotsOutput.schema)
