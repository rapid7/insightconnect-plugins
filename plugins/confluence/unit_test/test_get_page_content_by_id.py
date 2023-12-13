import sys
import os

from parameterized import parameterized

from util import Util

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_confluence.actions.get_page_content_by_id import GetPageContentById
from komand_confluence.actions.get_page_content_by_id.schema import (
    GetPageContentByIdInput,
    GetPageContentByIdOutput,
    Input,
)
from jsonschema import validate


class TestGetPageContentById(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetPageContentById())

    @parameterized.expand([("100001", "get_page_content"), ("100003", "get_page_content_not_found")])
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page_content(self, page_id: str, expected_filename: str, mock_get_page_content: Mock) -> None:
        test_input = {Input.PAGE_ID: page_id}
        validate(test_input, GetPageContentByIdInput.schema)
        response = self.action.run(test_input)
        expected = Util.load_data(expected_filename, "expected")
        self.assertEqual(expected, response)
        validate(response, GetPageContentByIdOutput.schema)
