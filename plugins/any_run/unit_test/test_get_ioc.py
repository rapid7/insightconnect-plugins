import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.get_ioc import GetIoc
from icon_any_run.actions.get_ioc.schema import Input, Output
from icon_any_run.util.tools import prepare_csv_payload
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util

ANALYSIS_UUID = "44d88612-fea8-a8f3-6de8-2e1278abb02f"


@patch("icon_any_run.util.tools.datetime")
@patch("icon_any_run.actions.get_ioc.action.BaseSandboxConnector")
class TestGetIoc(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIoc())

    def test_get_ioc(self, mock_connector_cls: MagicMock, mock_datetime: MagicMock) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None

        iocs = [
            {
                "category": "network",
                "type": "ipv4",
                "name": "C2",
                "ioc": "198.51.100.1",
                "reputation": 2,
                "discoveringEntryId": "entry-1",
            }
        ]
        mock_cm.get_analysis_report.side_effect = [iter(["completed"]), iocs]

        actual = self.action.run({Input.ANALYSIS_UUID: ANALYSIS_UUID})

        validate(actual, self.action.output.schema)
        self.assertEqual(actual[Output.COUNT], 1)
        self.assertEqual(actual[Output.REPORT], prepare_csv_payload(ANALYSIS_UUID, iocs))

    def test_get_ioc_raises_plugin_exception(self, mock_connector_cls: MagicMock, mock_datetime: MagicMock) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_analysis_report.side_effect = RunTimeException("ioc error", 422)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ANALYSIS_UUID: ANALYSIS_UUID})

        self.assertEqual(error.exception.cause, "Failed to retrieve IOCs.")
        self.assertEqual(error.exception.assistance, "ioc error")
        self.assertEqual(error.exception.data, "{'description': 'ioc error', 'code': 422}")
