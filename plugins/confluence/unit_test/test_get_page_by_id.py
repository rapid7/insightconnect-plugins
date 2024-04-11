import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from jsonschema import validate
from komand_confluence.actions.get_page_by_id import GetPageById
from komand_confluence.actions.get_page_by_id.schema import GetPageByIdInput, GetPageByIdOutput, Input
from parameterized import parameterized

from util import Util


class TestGetPageById(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetPageById())

    @parameterized.expand(
        [
            ("100001", "get_page"),
            ("100002", "get_page_home"),
            ("100003", "get_page_not_found"),
        ]
    )
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page(self, page_id: str, expected_filename: str, mock_get_page: Mock) -> None:
        test_input = {Input.PAGE_ID: page_id}
        validate(test_input, GetPageByIdInput.schema)
        response = self.action.run(test_input)
        expected = Util.load_data(expected_filename, "expected")
        self.assertEqual(expected, response)
        validate(response, GetPageByIdOutput.schema)
