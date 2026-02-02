import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.scan import Scan
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestScan(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Scan())

    @parameterized.expand(
        [
            [
                "with_override_blackout_as_false",
                Util.read_file_to_dict("inputs/scan_with_override_blackout_as_false.json.inp"),
                Util.read_file_to_dict("expected/scan_with_override_blackout_as_false.json.exp"),
            ],
            [
                "with_override_blackout_as_true",
                Util.read_file_to_dict("inputs/scan_with_override_blackout_as_true.json.inp"),
                Util.read_file_to_dict("expected/scan_with_override_blackout_as_true.json.exp"),
            ],
            [
                "with_host",
                Util.read_file_to_dict("inputs/scan_with_host.json.inp"),
                Util.read_file_to_dict("expected/scan_with_override_blackout_as_false.json.exp"),
            ],
        ]
    )
    def test_scan(self, mock_post, test_name, input_params, expected) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_site_id",
                Util.read_file_to_dict("inputs/scan_invalid_site_id.json.inp"),
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
                "The resource does not exist or access is prohibited.",
            ]
        ]
    )
    def test_scan_bad(self, mock_post, test_name, input_params, cause, assistance, data) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
