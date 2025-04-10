from unittest import TestCase
from unittest.mock import patch, MagicMock
from jsonschema.validators import validate
from smbprotocol.tree import TreeConnect
from komand_smb.actions.download_file.action import DownloadFile
from util import Util


class TestDownloadFile(TestCase):
    def setUp(self) -> None:
        self.open_patcher = patch("komand_smb.actions.download_file.action.Open")
        self.mock_open_class = self.open_patcher.start()
        self.addCleanup(self.open_patcher.stop)

        self.connect_patcher = patch("komand_smb.connection.connection.Connection.connect", return_value=None)
        self._connect_patcher = patch(
            "komand_smb.connection.connection.Connection._connect_to_smb_share",
            return_value=MagicMock(spec=TreeConnect),
        )

        self.mock_connect = self.connect_patcher.start()
        self.mock_connect_to_smb_share = self._connect_patcher.start()

        self.action = Util.default_connector(DownloadFile())

        self.mock_tree = self.mock_connect_to_smb_share.return_value
        self.action.connection._connect_to_smb_share = MagicMock(return_value=self.mock_tree)

    def test_download_file(self):
        input_params = {"share_name": "share", "file_path": "testing33.pdf", "timeout": 30}
        validate(input_params, self.action.input.schema)

        mock_open_instance = self.mock_open_class.return_value

        mock_bytes = MagicMock()
        mock_bytes.decode = MagicMock(return_value="What's up guys!")
        mock_open_instance.read.return_value = mock_bytes

        expect = {"file": {"content": "What's up guys!", "filename": "testing33.pdf"}}
        actual = self.action.run(input_params)

        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
