import time
from typing import Union, Callable

from insightconnect_plugin_runtime.exceptions import PluginException


class Message:
    BAD_REQUEST_MESSAGE = "Bad request error occured."
    CONFLICTED_STATE_OF_OBJECT_MESSAGE = "Conflicted state of the object"
    RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"


def backoff_function(attempt: int) -> float:
    """Back-off function used in rate_limiting retry decorator

    :param attempt: Current attempt value in retry function
    :type attempt: int

    :returns: time sleep value for next connection attempt
    :rtype: float
    """

    return 2 ** (attempt * 0.6)


def rate_limiting(max_tries: int) -> Union[dict, None]:
    """This decorator allows to work API call with rate limiting by using exponential backoff function. Decorator needs to have
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


def clean_query_output(query_response_input: dict) -> dict:
    """This function allows to change list of lists rows query output

    :param query_response_input: query API response input
    :type query_response_input: dict

    :returns: API call function data
    :rtype: dict
    """

    cleaned_output = query_response_input
    for table in cleaned_output.get("tables"):
        columns = table.get("columns")
        rows = table.get("rows")
        new_rows = [{columns[index].get("name"): _row[index] for index in range(0, len(_row))} for _row in rows]
        table["rows"] = new_rows
    return cleaned_output
