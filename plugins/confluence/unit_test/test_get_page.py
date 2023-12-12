import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from parameterized import parameterized
from komand_confluence.actions.get_page.schema import GetPageInput, Input, GetPageOutput
from komand_confluence.actions.get_page import GetPage
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


class TestGetPage(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetPage())

    @parameterized.expand(
        [
            ("Test Page", "Test Space", "get_page"),
            ("Test Home Page", "Test Space", "get_page_home"),
            ("Test Not Found", "Test Space", "get_page_not_found"),
        ]
    )
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page(
        self,
        page: str,
        space: str,
        expected_filename: str,
        mock_get_id: Mock,
        mock_get_page: Mock,
    ) -> None:
        test_input = {Input.PAGE: page, Input.SPACE: space}
        validate(test_input, GetPageInput.schema)
        response = self.action.run(test_input)
        expected = Util.load_data(expected_filename, "expected")
        self.assertEqual(expected, response)
        validate(response, GetPageOutput.schema)

    @parameterized.expand([("Test Page", "Test Not Found")])
    @mock.patch("atlassian.Confluence.get_page_id", side_effect=Util.mocked_requests)
    @mock.patch("atlassian.Confluence.get_page_by_id", side_effect=Util.mocked_requests)
    def test_get_page_failure(
        self, page: str, space: str, mock_get_id: Mock, mock_get_page: Mock
    ) -> None:
        cause = "Something unexpected occurred. See error log for details."
        assistance = "Please check your input and connection details."
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.PAGE: page, Input.SPACE: space})
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
