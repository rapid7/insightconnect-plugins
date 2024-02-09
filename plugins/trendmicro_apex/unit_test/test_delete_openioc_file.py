import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.delete_openioc_file import DeleteOpeniocFile
from icon_trendmicro_apex.actions.delete_openioc_file.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestDeleteOpeniocFile(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DeleteOpeniocFile())
        self.params = {Input.FILE_HASH_ID_LIST: "695cad3121a1f496cff0e35d51ba25e33cf266650626b4c1d035a72d2f801343"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_delete_openioc_file(self, mock_delete, mock_token):
        mocked_request(mock_delete)
        response = self.action.run(self.params)

        expected = {
            Output.DATA: [{"DeletedStatus": 1, "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455"}],
            Output.FEATURECTRL: {"mode": "0"},
            Output.META: {"ErrorCode": 0, "Result": 1},
            Output.PERMISSIONCTRL: {"permission": "255"},
            Output.SYSTEMCTRL: {"TmcmSoDist_Role": "none"},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
