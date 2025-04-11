import os
import time

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import return_non_empty
from typing import Union, Callable
import re
import logging


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


def backoff_function(attempt: int) -> float:
    """backoff_function. Back-off function used in rate_limiting retry decorator.

    :param attempt: Current attempt value in retry function.
    :type attempt: int

    :returns: time sleep value for next connection attempt.
    :rtype: float
    """

    return 2 ** (attempt * 0.6)


def rate_limiting(max_tries: int, back_off_function: Callable = backoff_function) -> Union[dict, None]:
    """rate_limiting. This decorator allows to work API call with rate limiting by using exponential backoff function.
    Decorator needs to have max_tries argument entered obligatory.

    :param max_tries: Maximum number of retries calling API function.
    :type max_tries: int

    :param back_off_function: Backoff function for time delay. Defaults to backoff_function.
    :type back_off_function: Callable

    :returns: API call function data or None.
    :rtype: Union[dict, None]
    """

    def _decorate(func: Callable):
        def _wrapper(self, *args, **kwargs):
            retry = True
            attempts_counter, delay = 0, 0
            while retry and attempts_counter < max_tries:
                if attempts_counter:
                    time.sleep(delay)
                try:
                    retry = False
                    return func(self, *args, **kwargs)
                except PluginException as error:
                    attempts_counter += 1
                    delay = back_off_function(attempts_counter)
                    if error.cause in [
                        PluginException.causes[PluginException.Preset.RATE_LIMIT],
                        PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE],
                    ]:
                        logging.info(
                            "%s Retrying in %.1f seconds (%d/%d)", error.cause, delay, attempts_counter, max_tries
                        )
                        retry = True
            return func(self, *args, **kwargs)

        return _wrapper

    return _decorate


def format_subdomain(instance: str) -> str:
    """
    If an input subdomain contains a scheme or the SentinelOne second-level domain, strip these values
    """

    # Remove leading and trailing whitespace
    instance = instance.strip()

    # Remove the scheme if it exists
    if instance.startswith("http://"):
        instance = instance[7:]
    elif instance.startswith("https://"):
        instance = instance[8:]

    # Remove the SentinelOne domain suffix
    if ".sentinelone.net" in instance:
        instance = instance.replace(".sentinelone.net", "")

    # Remove any trailing slashes
    return instance.rstrip("/")


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
