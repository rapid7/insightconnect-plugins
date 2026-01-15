import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.download_attachment import DownloadAttachment
from komand_rapid7_insightidr.actions.download_attachment.schema import (
    DownloadAttachmentInput,
    DownloadAttachmentOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestDownloadAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadAttachment())

    @parameterized.expand(Util.load_parameters("download_attachment").get("parameters"))
    def test_download_attachment(self, mock_request, name, attachment_rrn, expected) -> None:
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DownloadAttachmentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, DownloadAttachmentOutput.schema)

    @parameterized.expand(Util.load_parameters("download_attachment_bad").get("parameters"))
    def test_download_attachment_bad(self, mock_request, name, attachment_rrn, cause, assistance) -> None:
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DownloadAttachmentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
