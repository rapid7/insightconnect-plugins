import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_paloalto_wildfire.actions import SubmitFileFromUrl
from komand_paloalto_wildfire.actions.submit_file_from_url.schema import Input, Output

from test_util import Util


class TestSubmitFileFromUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitFileFromUrl())

    @patch("pyldfire.WildFire.get_verdicts", side_effect=Util.mocked_get_verdict)
    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_submit_file_from_url(self, mock_get_verdicts: MagicMock, mock_requests: MagicMock) -> None:
        actual = self.action.run({Input.URL: "http://www.pdf995.com/samples/pdf.pdf"})
        expected = {
            Output.SUBMISSION: {
                "filename": "Unknown",
                "filetype": "Adobe PDF document",
                "md5": "8bd6509aba6eafe623392995b08c7047",
                "sha256": "ebb031c3945e884e695dbc63c52a5efcd075375046c49729980073585ee13c52",
                "size": "433994",
                "url": "http://www.pdf995.com/samples/pdf.pdf",
            }
        }
        self.assertEqual(actual, expected)

    @patch("pyldfire.WildFire.get_verdicts", side_effect=Util.mocked_get_verdict)
    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_submit_file_from_url_already_in_db(self, mock_get_verdicts: MagicMock, mock_requests: MagicMock) -> None:
        actual = self.action.run({Input.URL: "http://www.pdf995.com/samples/in_db.pdf"})
        expected = {Output.VERDICT: "Malware"}
        self.assertEqual(actual, expected)

    def test_unsupported_file_type_in_link(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.URL: "http://www.pdf995.com/samples/EICAR.txt"})

        self.assertEqual("Unsupported file was received by the plugin.", context.exception.cause)
        self.assertEqual(
            "Check if your file is one of the supported files and resubmit with an approved file type. Supported files: ('.apk', '.flash', '.jar', '.msi', '.dmg', '.pkg', '.doc', '.iqy', '.7z', '.slk', '.dll', '.dng', '.fon', '.lnk', '.ooxml', '.pkg', '.ps1', '.vbs', '.bat', '.docx', '.elf', '.hta', '.js', '.mach-o', '.pdf', '.pe', '.ppt', '.pptx', '.rar', '.rtf', '.xls', '.xlsx')",
            context.exception.assistance,
        )
