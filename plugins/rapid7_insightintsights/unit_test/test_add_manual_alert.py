import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.add_manual_alert import AddManualAlert
from icon_rapid7_intsights.actions.add_manual_alert.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException


class TestAddManualAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AddManualAlert())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_manual_alert_should_success(self, make_request):
        actual = self.action.run(
            {
                Input.TITLE: "Test Alert",
                Input.DESCRIPTION: "Test description",
                Input.TYPE: "Phishing",
                Input.SUB_TYPE: "SuspiciousEmailAddress",
                Input.SEVERITY: "High",
                Input.SOURCE_TYPE: "Application Store",
                Input.SOURCE_NETWORK_TYPE: "ClearWeb",
                Input.SOURCE_URL: "http://www.rapid7.com",
                Input.SOURCE_DATE: "2020-01-01T20:01:27.344Z",
                Input.FOUND_DATE: "2020-01-01T20:01:27.344Z",
                Input.IMAGES: [{"type": "gif", "data": "R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="}],
            }
        )
        expected = {"alert_id": "7cafac7ec5adaebf62257a4c"}
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_manual_alert_should_fail_when_wrong_image(self, make_request):
        params = {
            Input.TITLE: "Test Alert",
            Input.DESCRIPTION: "Test description",
            Input.TYPE: "Phishing",
            Input.SUB_TYPE: "SuspiciousEmailAddress",
            Input.SEVERITY: "High",
            Input.SOURCE_TYPE: "Application Store",
            Input.SOURCE_NETWORK_TYPE: "ClearWeb",
            Input.SOURCE_URL: "http://www.example.com",
            Input.SOURCE_DATE: "2020-01-01T20:01:27.344Z",
            Input.FOUND_DATE: "2020-01-01T20:01:27.344Z",
            Input.IMAGES: [{"type": "gif"}],
        }
        with self.assertRaises(PluginException) as error:
            self.action.run(params)

        self.assertEqual("Wrong input parameter.", error.exception.cause)
        self.assertEqual("Wrong image: 'data'.", error.exception.assistance)
