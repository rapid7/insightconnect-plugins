from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

STUB_IMAGE_BASE64 = b"12345"


class MockBody:
    def __init__(self) -> None:
        ...

    @property
    def screenshot_as_base64(self) -> str:
        return "screenshot_as_base64"


class MockDriver:
    def __init__(self, *args, **kwargs) -> None:
        ...

    def get(self, url: str) -> None:
        if "driver" in url:
            raise WebDriverException

    def quit(self) -> None:
        ...

    @staticmethod
    def find_element(by_: By, input_str: str) -> MockBody:
        return MockBody()

    @staticmethod
    def save_screenshot(filename: str) -> bool:
        with open(filename, "wb") as file_:
            file_.write(STUB_IMAGE_BASE64)
        return True
