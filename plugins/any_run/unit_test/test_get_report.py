import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_any_run.actions.get_report import GetReport
from icon_any_run.actions.get_report.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetReport())

    @parameterized.expand(Util.load_parameters("get_report").get("parameters"))
    def test_get_report(self, mock_request, name, uuid, expected):
        actual = self.action.run({Input.TASK: uuid})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_report_bad").get("parameters"))
    def test_get_report_bad(self, mock_request, name, uuid, cause, assistance):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.TASK: uuid})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
