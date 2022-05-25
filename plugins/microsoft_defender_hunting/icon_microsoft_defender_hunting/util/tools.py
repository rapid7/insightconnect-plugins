import datetime
import time
from typing import Any, Callable, Dict, List, Tuple, Union

from insightconnect_plugin_runtime.exceptions import PluginException


class Defaults:
    DEFAULT_TRIGGER_INTERVAL = 60


class Message:
    BAD_REQUEST_MESSAGE = "Bad request error occured."
    RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"

    RESOURCE_WAS_NOT_FOUND_CAUSE = "Resource was not found on the server!"
    RESOURCE_WAS_NOT_FOUND_ASSISTANCE = (
        "Please verify that the item exists. If so, please contact support for more information."
    )


def backoff_function(attempt: int) -> float:
    """backoff_function. Back-off function used in rate_limiting retry decorator

    :param attempt: Current attempt value in retry function
    :type attempt: int

    :returns: time sleep value for next connection attempt
    :rtype: float
    """

    return 2 ** (attempt * 0.6)


def rate_limiting(max_tries: int) -> Union[dict, None]:
    """rate_limiting. This decorator allows to work API call with rate limiting by using exponential backoff function. Decorator needs to have
    max_tries argument entered obligatory

    :param max_tries: Maximum number of retries calling API function
    :type max_tries: int

    :returns: API call function data or None
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
                    delay = backoff_function(attempts_counter)
                    if error.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                        self.logger.info(
                            Message.RETRY_MESSAGE.format(
                                delay=delay, attempts_counter=attempts_counter, max_tries=max_tries
                            )
                        )
                        retry = True
            return func(self, *args, **kwargs)

        return _wrapper

    return _decorate
