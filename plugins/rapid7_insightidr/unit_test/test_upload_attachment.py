import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.upload_attachment import UploadAttachment
from komand_rapid7_insightidr.actions.upload_attachment.schema import (
    Input,
    UploadAttachmentInput,
    UploadAttachmentOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestUploadAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UploadAttachment())

    @parameterized.expand(Util.load_parameters("upload_attachment").get("parameters"))
    def test_upload_attachment(self, mock_request, name, filename, file_content, expected):
        test_input = {Input.FILENAME: filename, Input.FILE_CONTENT: file_content}
        validate(test_input, UploadAttachmentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, UploadAttachmentOutput.schema)
