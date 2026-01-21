import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.delete_attachment import DeleteAttachment
from komand_rapid7_insightidr.actions.delete_attachment.schema import (
    DeleteAttachmentInput,
    DeleteAttachmentOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestDeleteAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteAttachment())

    @parameterized.expand(Util.load_parameters("delete_comment").get("parameters"))
    def test_delete_attachment(self, mock_request, name, attachment_rrn, expected) -> None:
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DeleteAttachmentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, DeleteAttachmentOutput.schema)

    @parameterized.expand(Util.load_parameters("delete_comment_bad").get("parameters"))
    def test_delete_attachment_bad(self, mock_request, name, attachment_rrn, cause, assistance) -> None:
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, DeleteAttachmentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
