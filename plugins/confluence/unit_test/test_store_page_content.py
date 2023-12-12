import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from unittest.mock import Mock
from parameterized import parameterized
from unittest import TestCase
from unit_test.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_confluence.actions.store_page_content import StorePageContent
from komand_confluence.actions.store_page_content.schema import StorePageContentOutput, StorePageContentInput, Input
from jsonschema import validate



class TestStorePageContent(TestCase):

    def setUp(self) -> None:
        self.action = Util.default_connector(StorePageContent())

    @parameterized.expand(
        [
            ("Test Page", "Test Space", "<p>Test Content</p>", "store_page_content"),
            ("Test Page New", "Test Space", "<p>Test Content</p>", "store_page_content_new")
        ]
    )
    @mock.patch("atlassian.Confluence.update_page",side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.create_page", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.page_exists", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    def test_get_page_content(self, page: str, space: str, content: str, expected_filename: str, mock_update: Mock, mock_create: Mock, mock_exists: Mock, mock_get_id: Mock) -> None:
        test_input = {Input.PAGE: page, Input.SPACE: space, Input.CONTENT: content}
        validate(test_input, StorePageContentInput.schema)
        response = self.action.run(test_input)
        expected = Util.load_data(expected_filename, "expected")
        self.assertEqual(expected, response)
        validate(response, StorePageContentOutput.schema)


    @parameterized.expand(
        [
            ("Test Page", "Test Space", "<p>Test Content Failure</p>", "test_page_content_failure")
        ]
    )
    @mock.patch("atlassian.Confluence.update_page",side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.create_page", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.page_exists", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    def test_get_page_content_failure(self, page: str, space: str, content: str, expected_filename: str, mock_update: Mock, mock_create: Mock, mock_exists: Mock, mock_get_id: Mock) -> None:
        cause = "Something unexpected occurred. See error log for details."
        assistance = "Please check your input and connection details."
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.PAGE: page, Input.SPACE: space, Input.CONTENT: content})
        self.assertEqual(cause, error.exception.cause)