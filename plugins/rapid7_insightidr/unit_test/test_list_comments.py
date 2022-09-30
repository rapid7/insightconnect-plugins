import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.list_comments import ListComments
from komand_rapid7_insightidr.actions.list_comments.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestListComments(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListComments())

    @parameterized.expand(Util.load_parameters("list_comments").get("parameters"))
    def test_list_comments(self, mock_request, name, target, index, size, expected):
        actual = self.action.run({Input.TARGET: target, Input.INDEX: index, Input.SIZE: size})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("list_comments_bad").get("parameters"))
    def test_list_comments_bad(self, mock_request, name, target, index, size, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TARGET: target, Input.INDEX: index, Input.SIZE: size})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
