import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.delete_comment import DeleteComment
from komand_rapid7_insightidr.actions.delete_comment.schema import Input, DeleteCommentInput, DeleteCommentOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestDeleteComment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteComment())

    @parameterized.expand(Util.load_parameters("delete_comment").get("parameters"))
    def test_delete_comment(self, mock_request, name, comment_rrn, expected):
        test_input = {Input.COMMENT_RRN: comment_rrn}
        validate(test_input, DeleteCommentInput.schema)
        actual = self.action.run()
        self.assertEqual(actual, expected)
        validate(actual, DeleteCommentOutput.schema)

    @parameterized.expand(Util.load_parameters("delete_comment_bad").get("parameters"))
    def test_delete_comment_bad(self, mock_request, name, comment_rrn, cause, assistance):
        test_input = {Input.COMMENT_RRN: comment_rrn}
        validate(test_input, DeleteCommentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
