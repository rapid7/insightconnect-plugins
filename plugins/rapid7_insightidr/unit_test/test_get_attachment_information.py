import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_attachment_information import GetAttachmentInformation
from komand_rapid7_insightidr.actions.get_attachment_information.schema import (
    Input,
    GetAttachmentInformationInput,
    GetAttachmentInformationOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetAttachmentInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAttachmentInformation())

    @parameterized.expand(Util.load_parameters("get_attachment_information").get("parameters"))
    def test_get_attachment_information(self, mock_request, name, attachment_rrn, expected):
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, GetAttachmentInformationInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAttachmentInformationOutput.schema)

    @parameterized.expand(Util.load_parameters("get_attachment_information_bad").get("parameters"))
    def test_get_attachment_information_bad(self, mock_request, name, attachment_rrn, cause, assistance):
        test_input = {Input.ATTACHMENT_RRN: attachment_rrn}
        validate(test_input, GetAttachmentInformationInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
