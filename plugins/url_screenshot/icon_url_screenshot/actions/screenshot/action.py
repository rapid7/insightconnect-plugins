import insightconnect_plugin_runtime

from .schema import ScreenshotInput, ScreenshotOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_url_screenshot.util.constants import CHROME_PATH, WINDOW_SIZE
from icon_url_screenshot.util.messages import ExceptionMessages
import base64
import time
import tempfile

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver as ChromiumWebDriver
from selenium.webdriver.common.by import By


class Screenshot(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="screenshot",
            description=Component.DESCRIPTION,
            input=ScreenshotInput(),
            output=ScreenshotOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        url = params.get(Input.URL, "")
        delay = params.get(Input.DELAY, 0)
        full_page = params.get(Input.FULL_PAGE, False)
        # END INPUT BINDING - DO NOT REMOVE

        if not (url.lower().startswith("http://") or url.lower().startswith("https://")):
            raise PluginException(
                cause=ExceptionMessages.URL_START_HTTP_HTTPS_CAUSE,
                assistance=ExceptionMessages.URL_START_HTTP_HTTPS_ASSISTANCE,
            )

        with tempfile.TemporaryDirectory() as temporary_directory:
            try:
                driver = ChromiumWebDriver(options=self.setup_chromium_options(temporary_directory))
                driver.get(url)
                time.sleep(delay)

                if full_page:
                    try:
                        body = driver.find_element(By.TAG_NAME, "body")
                        base64_image = body.screenshot_as_base64
                    except Exception:
                        base64_image = self.screenshot_to_file(driver)
                else:
                    base64_image = self.screenshot_to_file(driver)
                driver.quit()
            except Exception as error:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.SCREENSHOT: base64_image}

    @staticmethod
    def screenshot_to_file(driver: ChromiumWebDriver) -> str:
        with tempfile.NamedTemporaryFile(suffix=".png") as temporary_file:
            driver.save_screenshot(temporary_file.name)
            with open(temporary_file.name, "rb") as file_:
                file_str = base64.b64encode(file_.read()).decode("ascii")
        return file_str

    @staticmethod
    def setup_chromium_options(
        temporary_directory: str, window_size: str = WINDOW_SIZE, chrome_path: str = CHROME_PATH
    ) -> Options:
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        chrome_options.add_argument(f"--user-data-dir={temporary_directory}")
        chrome_options.add_argument(f"--window-size={window_size}")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        return chrome_options
