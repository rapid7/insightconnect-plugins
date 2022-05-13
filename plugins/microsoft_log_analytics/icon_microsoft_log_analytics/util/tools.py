import time
from typing import Union, Callable, List, Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException


class Defaults:
    DEFAULT_TRIGGER_SEARCH_INTERVAL = 900


class Message:
    BAD_REQUEST_MESSAGE = "Bad request error occured."
    SAVED_SEARCH_NOT_FOUND_CAUSE = "Resource has been not found."
    SAVED_SEARCH_NOT_FOUND_ASSISTANCE = (
        "Please verify that the item exists. If so, please contact support for more information."
    )
    CONFLICTED_STATE_OF_OBJECT_MESSAGE = "Conflicted state of the object"
    RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"

    DELETE_SAVED_SEARCH_MESSAGE = "Saved search {} has been deleted"


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


def return_non_empty_query_output(query_response_input: dict) -> dict:
    """This function returns query response output with not empty rows

    :param query_response_input: query API response input
    :type query_response_input: dict

    :returns: API call function data
    :rtype: dict
    """

    return {"tables": list(filter(lambda x: x.get("rows"), query_response_input.get("tables")))}


def remove_keys_from_saved_search(
    sub_dictionaries: List[str], keys: List[str], input_list_of_dicts_or_dict: Union[List[dict], dict]
) -> Union[List[dict], dict]:
    """Method removes version keys from List All Saved Searches action's output.

    :param input_list_of_dicts_or_dict: Input dictionary from which all keys will be removed
    :type input_list_of_dicts_or_dict: Union[List[dict], dict]

    :returns: API call function data without keys in dictionaries and sub-dictionaries
    :rtype: Union[List[dict], dict]
    """

    if isinstance(input_list_of_dicts_or_dict, list):
        for key in keys:
            for dictionary in sub_dictionaries:
                for element in input_list_of_dicts_or_dict:
                    if key in element:
                        element.pop(key)
                    if key in element.get(dictionary):
                        element.get(dictionary).pop(key)
    elif isinstance(input_list_of_dicts_or_dict, dict):
        for key in keys:
            for dictionary in sub_dictionaries:
                if key in input_list_of_dicts_or_dict:
                    input_list_of_dicts_or_dict.pop(key)
                if key in input_list_of_dicts_or_dict.get(dictionary):
                    input_list_of_dicts_or_dict.get(dictionary).pop(key)
    return input_list_of_dicts_or_dict


def add_names_to_saved_searches_list(input_saved_search_list: List[dict]) -> List[dict]:
    """Add names to all elements in list of Saved Searches if doesn't exist.

    :param input_saved_search_list: Input list of dictionary that contains Saved Searches
    :type input_saved_search_list: List[dict]

    :returns: API call function data with added name keys if neccessary
    :rtype: List[dict]
    """

    for element in input_saved_search_list:
        if "name" not in element:
            element["name"] = element.get("id").split("/")[-1]
    return input_saved_search_list


def return_non_empty(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    """return_non_empty. Cleans up recusively the dictionary
    :param input_dict:
    :type input_dict: Dict[str, Any]
    :rtype: Dict[Any, Any]
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None and value != "" and value != []:
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            else:
                temp_dict[key] = value
    return temp_dict
