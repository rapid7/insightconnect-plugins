import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.create_comment import CreateComment
from komand_rapid7_insightidr.actions.create_comment.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestCreateComment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateComment())

    @parameterized.expand(Util.load_parameters("create_comment").get("parameters"))
    def test_create_comment(self, mock_request, name, target, body, attachments, expected):
        actual = self.action.run({Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("create_comment_bad").get("parameters"))
    def test_create_comment_bad(self, mock_request, name, target, body, attachments, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
