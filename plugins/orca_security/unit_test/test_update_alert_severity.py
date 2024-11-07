import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.update_alert_severity import UpdateAlertSeverity
from icon_orca_security.actions.update_alert_severity.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestUpdateAlertSeverity(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateAlertSeverity())

    @parameterized.expand(Util.load_parameters("update_alert_severity").get("parameters"))
    def test_update_alert_severity(self, mock_request, name, alert_id, severity, expected):
        actual = self.action.run({Input.ALERT_ID: alert_id, Input.SEVERITY: severity})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("update_alert_severity_bad").get("parameters"))
    def test_update_alert_severity_bad(self, mock_request, name, alert_id, severity, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ALERT_ID: alert_id, Input.SEVERITY: severity})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
