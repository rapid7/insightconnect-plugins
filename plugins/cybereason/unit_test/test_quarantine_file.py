import json
import sys
import os

sys.path.append(os.path.abspath('../'))
# Custom Imports

from unittest.mock import patch
from icon_cybereason.actions.quarantine_file.schema import Input
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cybereason.actions.quarantine_file import QuarantineFile
from unit_test.util import Util


class TestQuarantineFile(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(QuarantineFile())

    def test_get_sensor_details_bad_no_results(self):
        with self.assertRaises(PluginException):
            actual = self.action.run(
                {
                    Input.MALOP_ID: "MALOP_ID",
                    Input.QUARANTINE: True,
                    Input.SENSOR: "no-results"
                }
            )

    def test_get_sensor_details_bad_more_than_one_results(self):
        with self.assertRaises(PluginException):
            actual = self.action.run(
                {
                    Input.MALOP_ID: "MALOP_ID",
                    Input.QUARANTINE: True,
                    Input.SENSOR: "no-results"
                }
            )

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_quarantine_file(self, mock_request):
        actual = self.action.run(
            {
                Input.MALOP_ID: "MALOP_ID",
                Input.QUARANTINE: True,
                Input.SENSOR: "IPv4 Address"
            }
        )
        expected = '"totalNumberOfProbes": 1'
        assert json.dumps(actual).__contains__(expected)
