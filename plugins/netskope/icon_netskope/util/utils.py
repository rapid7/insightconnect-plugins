import time
from typing import Union, Callable, List, Dict, Any
from insightconnect_plugin_runtime.exceptions import PluginException


def backoff_function(attempt: int) -> float:
    """backoff_function. Back-off function used in rate_limiting retry decorator.

    :param attempt: Current attempt value in retry function.
    :type attempt: int

    :returns: time sleep value for next connection attempt.
    :rtype: float
    """

    return 2 ** (attempt * 0.6)


def rate_limiting(max_tries: int) -> Callable:
    """This decorator allows to work API call with rate limiting by using exponential backoff function. Decorator needs to have
    max_tries argument entered obligatory

    :param max_tries: Maximum number of retries calling API function
    :type max_tries: int

    :returns: API call function data
    :rtype: dict
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
                            f"Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"
                        )
                        retry = True
            return func(self, *args, **kwargs)

        return _wrapper

    return _decorate


def remove_json_version_from_data(
    input_list_of_dicts: Union[List[Dict[str, Any]], Dict[str, Any]]
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """Method allows to remove json_version key from Get All URL lists action's output.

    :param input_list_of_dicts: Input dictionary from which all keys will be removed
    :type input_list_of_dicts: List[dict]

    :returns: API call function data without json_version keys
    :rtype: List[dict]
    """

    if isinstance(input_list_of_dicts, list):
        for element in input_list_of_dicts:
            if "json_version" in element.get("data"):
                element.get("data", {}).pop("json_version")
    elif isinstance(input_list_of_dicts, dict):
        if "json_version" in input_list_of_dicts.get("data"):
            input_list_of_dicts.get("data", {}).pop("json_version")
    return input_list_of_dicts
