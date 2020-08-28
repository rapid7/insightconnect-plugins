import komand
from .schema import ScreenshotInput, ScreenshotOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import base64
import time
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Screenshot(komand.Action):
    CHROME_PATH = '/usr/bin/chromium'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='screenshot',
                description=Component.DESCRIPTION,
                input=ScreenshotInput(),
                output=ScreenshotOutput())

    def screenshot_to_file(self, driver):
        with tempfile.NamedTemporaryFile(suffix=".png") as t:
            driver.save_screenshot(t.name)
            with open(t.name, "rb") as file:
                contents = file.read()
                file_str = base64.b64encode(contents).decode('ascii')
        return file_str

    def run(self, params={}):
        with tempfile.TemporaryDirectory() as tempdir:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=%s" % self.WINDOW_SIZE)
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument(f"--user-data-dir={tempdir}")
            chrome_options.binary_location = self.CHROME_PATH

            url = params.get(Input.URL, "")
            delay = params.get(Input.DELAY, 0)
            if not url.lower().startswith('http'):
                raise PluginException(cause="Input Error:", assistance="URLs need to start with 'http'")
            driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH, options=chrome_options)
            driver.get(url)
            time.sleep(delay)
            full_page = params.get(Input.FULL_PAGE, False)
            if full_page:
                try:
                    body = driver.find_element_by_tag_name('body')
                    img_str = body.screenshot_as_base64
                except Exception:
                    img_str = self.screenshot_to_file(driver)
            else:
                img_str = self.screenshot_to_file(driver)
            driver.quit()
        return {Output.SCREENSHOT: img_str}
