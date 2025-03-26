import sys
import os
from util import Util

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_smb.actions.download_file import DownloadFile
from jsonschema import validate
from unittest.mock import MagicMock, patch, Mock
from util import MockSMBSession

CREATE_CLIENT_MOCK = MagicMock()


class TestDownloadFile(TestCase):
    @patch("smb.SMBConnection.SMBConnection.connect")
    def setUp(self, mock_smb: Mock) -> None:
        self.action = Util.default_connector(DownloadFile())

    @patch("smb.SMBConnection.SMBConnection.retrieveFile", side_effect=MockSMBSession.retrieveFile)
    def test_download_file(self, mock_smb: Mock) -> None:
        input_param = Util.load_json("inputs/download_file_input.json.exp")
        expect = Util.load_json("expected/download_file_output.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
