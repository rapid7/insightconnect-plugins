import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.verify_alert import VerifyAlert
from icon_orca_security.actions.verify_alert.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestVerifyAlert(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(VerifyAlert())

    @parameterized.expand(Util.load_parameters("verify_alert").get("parameters"))
    def test_verify_alert(self, mock_request, name, alert_id, expected):
        actual = self.action.run({Input.ALERT_ID: alert_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("verify_alert_bad").get("parameters"))
    def test_verify_alert_bad(self, mock_request, name, alert_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ALERT_ID: alert_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
