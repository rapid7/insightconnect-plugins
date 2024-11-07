import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.update_alert_status import UpdateAlertStatus
from icon_orca_security.actions.update_alert_status.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestUpdateAlertStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateAlertStatus())

    @parameterized.expand(Util.load_parameters("update_alert_status").get("parameters"))
    def test_update_alert_status(self, mock_request, name, alert_id, status, expected):
        actual = self.action.run({Input.ALERT_ID: alert_id, Input.STATUS: status})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("update_alert_status_bad").get("parameters"))
    def test_update_alert_status_bad(self, mock_request, name, alert_id, status, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ALERT_ID: alert_id, Input.STATUS: status})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
