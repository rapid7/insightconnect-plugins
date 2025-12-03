import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_any_run.actions.get_report import GetReport
from icon_any_run.actions.get_report.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetReport())

    @parameterized.expand(Util.load_parameters("get_report").get("parameters"))
    def test_get_report(self, mock_request: MagicMock, name: str, uuid: str, expected: Dict[str, Any]) -> None:
        actual = self.action.run({Input.TASK: uuid})
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_report_bad").get("parameters"))
    def test_get_report_bad(self, mock_request: MagicMock, name: str, uuid: str, cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TASK: uuid})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
