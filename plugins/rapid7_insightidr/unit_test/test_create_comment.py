import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.create_comment import CreateComment
from komand_rapid7_insightidr.actions.create_comment.schema import Input, CreateCommentInput, CreateCommentOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestCreateComment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateComment())

    @parameterized.expand(Util.load_parameters("create_comment").get("parameters"))
    def test_create_comment(self, mock_request, name, target, body, attachments, expected):
        test_input = {Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments}
        validate(test_input, CreateCommentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, CreateCommentOutput.schema)

    @parameterized.expand(Util.load_parameters("create_comment_bad").get("parameters"))
    def test_create_comment_bad(self, mock_request, name, target, body, attachments, cause, assistance):
        test_input = {Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments}
        validate(test_input, CreateCommentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
