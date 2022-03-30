import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_fireeye_hx.actions.get_alerts_by_host_id import GetAlertsByHostId
from icon_fireeye_hx.actions.get_alerts_by_host_id.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.sessions.Session.request", side_effect=Util.mocked_requests)
class TestGetAlertsByHostId(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(GetAlertsByHostId())

    @parameterized.expand(Util.load_parameters("get_alerts_by_host_id").get("parameters"))
    def test_get_alerts_by_host_id(self, mock_request, name, host_id, expected):
        actual = self.action.run({Input.HOST_ID: host_id})
        self.assertEqual(actual, expected)
