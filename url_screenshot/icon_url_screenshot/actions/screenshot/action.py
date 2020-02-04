import komand
from .schema import ScreenshotInput, ScreenshotOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import os
import uuid
import base64
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Screenshot(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='screenshot',
                description=Component.DESCRIPTION,
                input=ScreenshotInput(),
                output=ScreenshotOutput())

    def run(self, params={}):
        CHROME_PATH = '/usr/bin/chromium'
        CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
        WINDOW_SIZE = "1920,1080"

        name = "/tmp/{}{}".format(str(uuid.uuid1()), ".png")

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = CHROME_PATH

        url = params.get(Input.URL, "")
        delay = params.get(Input.DELAY, 0)
        if not url.lower().startswith('http'):
            raise PluginException(cause='Input Error:', assistance='URLs need to start with "http"')
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
        driver.get(url)
        time.sleep(delay)
        driver.save_screenshot(name)
        driver.close()

        with open(name, "rb") as file:
            contents = file.read()
            file_str = base64.b64encode(contents).decode('ascii')

        os.remove(name)

        return {Output.SCREENSHOT: file_str}
