import time
from functools import wraps
from typing import Callable

from insightconnect_plugin_runtime.exceptions import PluginException


class Message:
    ADDRESS_GROUP_NOT_FOUND_CAUSE = "The address group does not exist in SonicWall."
    ADDRESS_GROUP_NOT_FOUND_ASSISTANCE = "Please enter valid names and try again."

    ADDRESS_OBJECT_NOT_FOUND_CAUSE = "The address object '{}' was not found in SonicWall."
    ADDRESS_OBJECT_NOT_FOUND_ASSISTANCE = "Please make sure that you entered the correct name and try again."

    ZONE_NOT_FOUND_CAUSE = "The zone: '{zone_name}' does not exist in SonicWall."
    ZONE_NOT_FOUND_ASSISTANCE = "Please enter valid zone name and try again."


def retry_login(max_tries: int) -> Callable:
    """retry_login. This decorator allows to retry login while the session is held by different login API.
    Decorator needs to have max_tries argument entered obligatory.

    :param max_tries: Maximum number of retries calling API function.
    :type max_tries: int

    :returns: API call function data or None.
    :rtype: Callable
    """

    def _decorate(function_: Callable):
        @wraps(function_)
        def _wrapper(self, *args, **kwargs):
            retry = True
            attempts_counter = 0
            while retry and attempts_counter < max_tries:
                if attempts_counter:
                    time.sleep(1)
                try:
                    retry = False
                    return function_(self, *args, **kwargs)
                except PluginException as error:
                    attempts_counter += 1
                    if error.cause == PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]:
                        self.logger.info(f"Retrying to login... ({attempts_counter}/{max_tries})")
                        self.login()
                        retry = True
            return function_(self, *args, **kwargs)

        return _wrapper

    return _decorate
