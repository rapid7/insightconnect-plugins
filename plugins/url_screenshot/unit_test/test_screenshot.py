import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_url_screenshot.actions.screenshot import Screenshot
from icon_url_screenshot.actions.screenshot.schema import Output
from icon_url_screenshot.util.messages import ExceptionMessages
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from utils import MockDriver


class TestScreenshot(TestCase):
    def setUp(self) -> None:
        self.action = Screenshot()

    @parameterized.expand(
        [
            ({"url": "http://www.example.com", "delay": 0, "full_page": False}, "MTIzNDU="),
            ({"url": "https://www.example.com", "delay": 0, "full_page": True}, "screenshot_as_base64"),
        ]
    )
    @patch("selenium.webdriver.chrome.webdriver.WebDriver.__new__", side_effect=MockDriver)
    def test_screenshot(self, input_data: Dict[str, Any], expected: str, mock_driver: MagicMock) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.SCREENSHOT: expected})
        mock_driver.assert_called_once()

    @parameterized.expand(
        [
            (
                {"url": "www.example.com"},
                ExceptionMessages.URL_START_HTTP_HTTPS_CAUSE,
                ExceptionMessages.URL_START_HTTP_HTTPS_ASSISTANCE,
            ),
            (
                {"url": "https://driver"},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
        ]
    )
    @patch("selenium.webdriver.chrome.webdriver.WebDriver.__new__", side_effect=MockDriver)
    def test_screenshot_error(
        self, input_data: Dict[str, Any], cause: str, assistance: str, mock_driver: MagicMock
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
