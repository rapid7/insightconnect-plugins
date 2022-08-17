import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.get_alerts import GetAlerts
from icon_orca_security.actions.get_alerts.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetAlerts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlerts())

    @parameterized.expand(Util.load_parameters("get_alerts").get("parameters"))
    def test_get_alerts(self, mock_request, name, filters, limit, expected):
        actual = self.action.run({Input.FILTERS: filters, Input.LIMIT: limit})
        self.assertEqual(actual, expected)
