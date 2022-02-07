import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.rescan_indicator import RescanIndicator
from icon_rapid7_intsights.actions.rescan_indicator.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException


class TestRescanIndicator(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(RescanIndicator())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_rescan_indicator_should_success(self, make_request):
        actual = self.action.run({Input.INDICATOR_FILE_HASH: "000003a16a5a1c6ccddbe548e852614224891111"})
        expected = {"status": "Queued", "task_id": "abcdefg123456"}
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_rescan_indicator_should_failed(self, make_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INDICATOR_FILE_HASH: "bad"})

        self.assertEqual("IntSights returned an error response: ", error.exception.cause)
        self.assertEqual("Invalid IOC value. Supported IOC types: file hashes.", error.exception.assistance)
