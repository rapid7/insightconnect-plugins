import base64
import json
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.get_intelligence import GetIntelligence
from icon_any_run.actions.get_intelligence.schema import Input, Output
from icon_any_run.util.tools import get_report_name
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("icon_any_run.util.tools.datetime")
@patch("icon_any_run.actions.get_intelligence.action.LookupConnector")
class TestGetIntelligence(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIntelligence())

    def test_get_intelligence(self, mock_lookup_cls: MagicMock, mock_datetime: MagicMock) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_lookup_cls.return_value.__enter__.return_value = mock_cm
        mock_lookup_cls.return_value.__exit__.return_value = None
        report = {"hits": [], "total": 0}
        mock_cm.get_intelligence.return_value = report

        query = "malware AND type:file"
        lookup_depth = 90
        actual = self.action.run({Input.QUERY: query, Input.LOOKUP_DEPTH: lookup_depth})

        validate(actual, self.action.output.schema)
        expected_url = (
            "https://intelligence.any.run/analysis/lookup#"
            "%7B%22query%22%3A%20%22malware%20AND%20type%3Afile%22%2C%20%22dateRange%22%3A%2090%7D"
        )
        self.assertEqual(actual[Output.LOOKUP_URL], expected_url)
        self.assertEqual(actual[Output.REPORT]["filename"], get_report_name("TI_LOOKUP", "json"))
        self.assertEqual(actual[Output.REPORT]["content"], base64.b64encode(json.dumps(report).encode()).decode())
        mock_cm.get_intelligence.assert_called_once_with(query=query, lookup_depth=lookup_depth)

    def test_get_intelligence_raises_plugin_exception(
        self, mock_lookup_cls: MagicMock, mock_datetime: MagicMock
    ) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_lookup_cls.return_value.__enter__.return_value = mock_cm
        mock_lookup_cls.return_value.__exit__.return_value = None
        mock_cm.get_intelligence.side_effect = RunTimeException("lookup error", 429)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.QUERY: "malware", Input.LOOKUP_DEPTH: 30})

        self.assertEqual(error.exception.cause, "Failed to get intelligence.")
        self.assertEqual(error.exception.assistance, "lookup error")
        self.assertEqual(error.exception.data, "{'description': 'lookup error', 'code': 429}")
