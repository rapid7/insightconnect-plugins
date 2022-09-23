import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.delete_comment import DeleteComment
from komand_rapid7_insightidr.actions.delete_comment.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestDeleteComment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteComment())

    @parameterized.expand(Util.load_parameters("delete_comment").get("parameters"))
    def test_delete_comment(self, mock_request, name, comment_rrn, expected):
        actual = self.action.run({Input.COMMENT_RRN: comment_rrn})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("delete_comment_bad").get("parameters"))
    def test_delete_comment_bad(self, mock_request, name, comment_rrn, cause, assistance):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.COMMENT_RRN: comment_rrn})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
