import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from anyrun import RunTimeException
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_any_run.actions.download_pcap import DownloadPcap
from icon_any_run.actions.download_pcap.schema import Input, Output
from icon_any_run.util.tools import get_report_name

from util import Util


@patch("icon_any_run.util.tools.datetime")
@patch("icon_any_run.actions.download_pcap.action.BaseSandboxConnector")
class TestDownloadPcap(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadPcap())

    def test_download_pcap(self, mock_connector_cls: MagicMock, mock_datetime: MagicMock) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        pcap_bytes = b"\xd4\xc3\xb2\xa1"
        mock_cm.download_pcap.return_value = pcap_bytes

        analysis_uuid = "44d88612-fea8-a8f3-6de8-2e1278abb02f"
        actual = self.action.run({Input.ANALYSIS_UUID: analysis_uuid})

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual[Output.PCAP]["filename"],
            get_report_name(analysis_uuid, "pcap"),
        )
        self.assertEqual(actual[Output.PCAP]["content"], base64.b64encode(pcap_bytes).decode())
        mock_cm.download_pcap.assert_called_once_with(analysis_uuid)

    def test_download_pcap_raises_plugin_exception(
        self, mock_connector_cls: MagicMock, mock_datetime: MagicMock
    ) -> None:
        self.action.logger = MagicMock()
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.download_pcap.side_effect = RunTimeException("pcap error", 500)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ANALYSIS_UUID: "44d88612-fea8-a8f3-6de8-2e1278abb02f"})

        self.assertEqual(error.exception.cause, "Failed to download analysis pcap.")
        self.assertEqual(error.exception.assistance, "pcap error")
        self.assertEqual(error.exception.data, "{'description': 'pcap error', 'code': 500}")
