import os

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import return_non_empty
from typing import Union
import re


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    return return_non_empty(item_to_clean.copy())


def sanitise_url(file_url: str) -> str:
    # Sanitise URLs to help guard against path traversal
    sanitised_url = file_url.replace("%2e%2e%2f", "../")
    sanitised_url = sanitised_url.replace("../", "")
    sanitised_url = sanitised_url.replace("%2e%2e%5C", "..\\")
    sanitised_url = sanitised_url.replace("..\\", "")
    sanitised_url = os.path.normpath(sanitised_url)
    return sanitised_url


class Helper:
    @staticmethod
    def join_or_empty(joined_array: list) -> str:
        return ",".join(joined_array)


def check_password_meets_requirements(password: str):
    """
    A method to determine if password meets required format (minimum length and no whitespace)
    :param password: The password to check
    """
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$", password):
        raise PluginException(
            cause="Invalid password.",
            assistance="The password must be 10 or more characters with a mix of upper and lower case letters, numbers,"
            " and symbols.",
        )
