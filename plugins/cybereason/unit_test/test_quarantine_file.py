import json
import sys
import os


sys.path.append(os.path.abspath("../"))
# Custom Imports

from parameterized import parameterized
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

    @parameterized.expand(
        [
            [
                "get_sensor_details_bad_no_results",
                "MALOP_ID",
                True,
                "no-results",
                "No sensors found using identifier: no-results.",
                "Please validate inputs and try again.",
            ],
            [
                "get_sensor_details_bad_more_than_one_result",
                "MALOP_ID",
                True,
                "more_than_one_result",
                "Multiple sensors found using identifier: more_than_one_result.",
                "Please provide a unique identifier and try again.",
            ],
            [
                "check_status_codes_bad",
                "MALOP_ID",
                True,
                "JSONDecodeError",
                "Invalid username or password provided.",
                "Verify your username and password are correct.",
            ],
            [
                "quarantine_file_bad",
                "BAD_MALOP_ID",
                True,
                "IPv4 Address",
                "Unable to retrieve Malop information for BAD_MALOP_ID.",
                "Please ensure that provided Malop GUID is valid and try again.",
            ],
            [
                "quarantine_file_bad_visual_search",
                "MALOP_ID",
                False,
                "Machine_name_visual_search",
                "No results found.",
                "No Visual Search results returned for the provided filter.",
            ],
        ]
    )
    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_api_bad(self, test_name, malop_id, quarantine, sensor, cause, assistance, mock_request):
        with self.assertRaises(PluginException) as context:
            actual = self.action.run(
                {
                    Input.MALOP_ID: malop_id,
                    Input.QUARANTINE: quarantine,
                    Input.SENSOR: sensor,
                }
            )
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_quarantine_file(self, mock_request):
        actual = self.action.run({Input.MALOP_ID: "MALOP_ID", Input.QUARANTINE: True, Input.SENSOR: "IPv4 Address"})
        expected = '"malopId": "11.2189746432167327222", "remediationId": "5144cf82-94c4-49f8-82cd-9ce1fcbd6a23", "start": 1624819406074, "initiatingUser": "user@example.com", "statusLog": []'
        assert json.dumps(actual).__contains__(expected)
