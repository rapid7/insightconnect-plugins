import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_attachment_information import GetAttachmentInformation
from komand_rapid7_insightidr.actions.get_attachment_information.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetAttachmentInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAttachmentInformation())

    @parameterized.expand(Util.load_parameters("get_attachment_information").get("parameters"))
    def test_get_attachment_information(self, mock_request, name, attachment_rrn, expected):
        actual = self.action.run({Input.ATTACHMENT_RRN: attachment_rrn})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_attachment_information_bad").get("parameters"))
    def test_get_attachment_information_bad(self, mock_request, name, attachment_rrn, cause, assistance):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ATTACHMENT_RRN: attachment_rrn})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
