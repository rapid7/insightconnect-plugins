import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_gitlab.actions.create_issue import CreateIssue
from icon_gitlab.actions.create_issue.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestCreateIssue(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(CreateIssue())
        self.params = {Input.TITLE: "Example Title"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_create_issue(self, mock_post: MagicMock) -> None:
        mocked_request(mock_post)
        response = self.action.run(self.params)

        expected = {Output.ISSUE: {}}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
