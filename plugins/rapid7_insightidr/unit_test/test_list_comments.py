import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.list_comments import ListComments
from komand_rapid7_insightidr.actions.list_comments.schema import Input, ListCommentsInput, ListCommentsOutput
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestListComments(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListComments())

    @parameterized.expand(Util.load_parameters("list_comments").get("parameters"))
    def test_list_comments(self, mock_request, name, target, index, size, expected) -> None:
        test_input = {Input.TARGET: target, Input.INDEX: index, Input.SIZE: size}
        validate(test_input, ListCommentsInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, ListCommentsOutput.schema)

    @parameterized.expand(Util.load_parameters("list_comments_bad").get("parameters"))
    def test_list_comments_bad(self, mock_request, name, target, index, size, cause, assistance) -> None:
        test_input = {Input.TARGET: target, Input.INDEX: index, Input.SIZE: size}
        validate(test_input, ListCommentsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
