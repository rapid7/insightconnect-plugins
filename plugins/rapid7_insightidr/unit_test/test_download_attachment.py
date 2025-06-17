import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.download_attachment import DownloadAttachment
from komand_rapid7_insightidr.actions.download_attachment.schema import (
    Input,
    DownloadAttachmentInput,
    DownloadAttachmentOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestDownloadAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadAttachment())

    @parameterized.expand(Util.load_parameters("download_attachment").get("parameters"))
    def test_download_attachment(self, mock_request, name, attachment_rrn, expected):
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DownloadAttachmentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, DownloadAttachmentOutput.schema)

    @parameterized.expand(Util.load_parameters("download_attachment_bad").get("parameters"))
    def test_download_attachment_bad(self, mock_request, name, attachment_rrn, cause, assistance):
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DownloadAttachmentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
