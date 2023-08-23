import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.list_attachments import ListAttachments
from komand_rapid7_insightidr.actions.list_attachments.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestListAttachments(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAttachments())

    @parameterized.expand(Util.load_parameters("list_attachments").get("parameters"))
    def test_list_attachments(self, mock_request, name, target, index, size, expected):
        actual = self.action.run({Input.TARGET: target, Input.INDEX: index, Input.SIZE: size})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("list_attachments_bad").get("parameters"))
    def test_list_attachments_bad(self, mock_request, name, target, index, size, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TARGET: target, Input.INDEX: index, Input.SIZE: size})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
