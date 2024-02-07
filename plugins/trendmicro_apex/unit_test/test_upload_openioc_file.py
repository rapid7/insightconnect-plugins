import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.upload_openioc_file import UploadOpeniocFile
from icon_trendmicro_apex.actions.upload_openioc_file.schema import Input, Output
from jsonschema import validate
from unit_test.mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestUploadOpeniocFile(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(UploadOpeniocFile())
        self.params = {Input.FILES: [{"content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==", "filename": "file.txt"}]}

    @patch("requests.request", side_effect=mock_request_200)
    def test_upload_openioc_file(self, mock_post, mock_token):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected = {
            Output.FEATURECTRL: {"mode": "0"},
            Output.META: {"ErrorCode": 0, "Result": 1},
            Output.PERMISSIONCTRL: {"permission": "255"},
            Output.SYSTEMCTRL: {"TmcmSoDist_Role": "none"},
            Output.UPLOADED_INFO_LIST: {
                "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
                "FileName": "file.txt",
                "UploadedStatus": 1,
            },
            Output.UPLOADED_MESSAGE_LIST: {"Message": "Uploaded 1 OpenIOC file(s) successfully.", "MessageType": 1},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
