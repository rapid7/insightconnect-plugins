import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.create_comment import CreateComment
from komand_rapid7_insightidr.actions.create_comment.schema import CreateCommentInput, CreateCommentOutput, Input
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestCreateComment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateComment())

    @parameterized.expand(Util.load_parameters("create_comment").get("parameters"))
    def test_create_comment(self, mock_request, name, target, body, attachments, expected) -> None:
        test_input = {Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments}
        validate(test_input, CreateCommentInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, CreateCommentOutput.schema)

    @parameterized.expand(Util.load_parameters("create_comment_bad").get("parameters"))
    def test_create_comment_bad(self, mock_request, name, target, body, attachments, cause, assistance) -> None:
        test_input = {Input.TARGET: target, Input.BODY: body, Input.ATTACHMENTS: attachments}
        validate(test_input, CreateCommentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
