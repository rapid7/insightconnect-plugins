from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema.validators import validate
from smbprotocol.tree import TreeConnect
from komand_smb.actions.delete_file.action import DeleteFile
from util import Util


class TestDeleteFile(TestCase):
    def setUp(self) -> None:
        self.open_patcher = patch("komand_smb.actions.delete_file.action.Open")
        self.mock_open_class = self.open_patcher.start()
        self.addCleanup(self.open_patcher.stop)

        self.connect_patcher = patch("komand_smb.connection.connection.Connection.connect", return_value=None)
        self._connect_patcher = patch(
            "komand_smb.connection.connection.Connection._connect_to_smb_share",
            return_value=MagicMock(spec=TreeConnect),
        )

        self.mock_connect = self.connect_patcher.start()
        self.mock_connect_to_smb_share = self._connect_patcher.start()

        self.action = Util.default_connector(DeleteFile())

        self.mock_tree = self.mock_connect_to_smb_share.return_value

        self.action.connection._connect_to_smb_share = MagicMock(return_value=self.mock_tree)

    def test_delete_file(self):
        input_params = {"share_name": "share", "file_path": "text.txt", "timeout": 30}
        validate(input_params, self.action.input.schema)

        expect = {"deleted": True}
        actual = self.action.run(input_params)

        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
