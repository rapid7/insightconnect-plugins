import base64
import json
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate

from icon_any_run.actions.get_intelligence import GetIntelligence
from icon_any_run.actions.get_intelligence.schema import Input, Output
from icon_any_run.util.tools import get_report_name

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
            "https://intelligence.any.run/analysis/lookup#{%22query%22:%22"
            + query.replace('"', "%5C%22").replace(" ", "%20")
            + "%22,%22dateRange%22:180}"
        )
        self.assertEqual(actual[Output.LOOKUP_URL], expected_url)
        self.assertEqual(actual[Output.REPORT]["filename"], get_report_name("TI_LOOKUP", "json"))
        self.assertEqual(actual[Output.REPORT]["content"], base64.b64encode(json.dumps(report).encode()).decode())
        mock_cm.get_intelligence.assert_called_once_with(query=query, lookup_depth=lookup_depth)
