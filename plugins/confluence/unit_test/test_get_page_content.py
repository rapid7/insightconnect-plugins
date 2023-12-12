import sys
import os

from unit_test.util import Util

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from parameterized import parameterized
from unittest import TestCase
from komand_confluence.actions.get_page_content import GetPageContent
from komand_confluence.actions.get_page_content.schema import (
    GetPageContentInput,
    GetPageContentOutput,
    Input,
)
from jsonschema import validate
from insightconnect_plugin_runtime.exceptions import PluginException


class TestGetPageContent(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetPageContent())

    @parameterized.expand(
        [
            ("Test Page", "Test Space", "get_page_content"),
            ("Test Not Found", "Test Space", "get_page_content_not_found"),
        ]
    )
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page_content(
        self,
        page: str,
        space: str,
        expected_filename: str,
        mock_get_id: Mock,
        mock_get_page: Mock,
    ) -> None:
        test_input = {Input.PAGE: page, Input.SPACE: space}
        validate(test_input, GetPageContentInput.schema)
        response = self.action.run(test_input)
        expected = Util.load_data(expected_filename, "expected")
        self.assertEqual(expected, response)
        validate(response, GetPageContentOutput.schema)

    @parameterized.expand([("Test Page", "Test Not Found")])
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page_content_failure(
        self, page: str, space: str, mock_get_id: Mock, mock_get_page: Mock
    ) -> None:
        cause = "Something unexpected occurred. See error log for details."
        assistance = "Please check your input and connection details."
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.PAGE: page, Input.SPACE: space})
        self.assertEqual(cause, error.exception.cause)
