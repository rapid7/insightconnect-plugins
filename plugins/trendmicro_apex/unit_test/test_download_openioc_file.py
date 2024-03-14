import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.download_openioc_file import DownloadOpeniocFile
from icon_trendmicro_apex.actions.download_openioc_file.schema import Input, Output
from mock import Util, mock_request_200, mocked_request
from jsonschema import validate


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestDownloadOpeniocFile(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DownloadOpeniocFile())
        self.params = {Input.FILE_HASH_ID: "abcdef"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_download_openioc_file(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.DATA: {
                "FileContentBase64": "abcdef",
                "FileName": "file.txt",
            },
            Output.FEATURECTRL: {"mode": "0"},
            Output.META: {"ErrorCode": 0, "Result": 1},
            Output.PERMISSIONCTRL: {"permission": "255"},
            Output.SYSTEMCTRL: {"TmcmSoDist_Role": "none"},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
