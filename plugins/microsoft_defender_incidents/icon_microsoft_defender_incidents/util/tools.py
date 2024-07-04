import datetime
import time
from typing import Any, Callable, Dict, List, Tuple, Union

from insightconnect_plugin_runtime.exceptions import PluginException


class Defaults:
    DEFAULT_TRIGGER_INTERVAL = 900


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


def return_non_empty(input_dict: Dict[str, Any]) -> Union[Dict[Any, Any], Any]:
    """return_non_empty. Cleans up recursively the dictionary

    :param input_dict: Input dictionary
    :type input_dict: Dict[str, Any]

    :rtype: Union[Dict[Any, Any], None]
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None and value != "" and value != []:
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            elif isinstance(value, list):
                return_value = [
                    return_non_empty(element) if isinstance(element, dict) else element for element in value
                ]
                return_value = list(filter(None, return_value))
                if return_value:
                    temp_dict[key] = return_value
            else:
                temp_dict[key] = value
    return temp_dict


def request_execution_time(func: Callable) -> Tuple[dict, float]:
    """request_execution_time. Measures time of request

    :param func: Function to be decorated
    :type func: Callable

    :rtype: Tuple[dict, float]
    """

    def _wrap(*args, **kwargs):
        start_request_time = datetime.datetime.now()
        response = func(*args, **kwargs)
        end_request_time = datetime.datetime.now()
        return response, end_request_time - start_request_time

    return _wrap


def remove_keys_from_dict(input_dict: Dict[str, Any], keys_to_remove: List[str]) -> dict:
    """remove_keys_from_dict. Remove keys from dictionary

    :param input_dict: Input dictionary
    :type input_dict: Dict[str, Any]

    :param keys_to_remove: List of keys to be removed from dictionary
    :type keys_to_remove: List[Any]

    :rtype: dict
    """

    output_dict = input_dict.copy()
    for key in keys_to_remove:
        if key in output_dict:
            output_dict.pop(key)
    return output_dict


def fill_required_fields(input_dict: Dict[str, Any]) -> dict:
    """fill_required_fields. Fills required schema fields with empty values if they're not exists

    :param input_dict: Input dictionary
    :type input_dict: Dict[str, Any]

    :rtype: dict
    """

    # Everything in the output is required so I'm updating this to include
    # every output field.
    # n.b. I won't include Incident ID because we can safely assume Incident ID
    # will be present in every call related to incidents.

    required_fields = [
        {"name": "assignedTo", "default": ""},
        {"name": "tags", "default": []},
        {"name": "comments", "default": []},
        {"name": "alerts", "default": []},
        {"name": "incidentName", "default": ""},
        {"name": "classification", "default": "Unknown"},
        {"name": "determination", "default": "NotAvailable"},
        {"name": "status", "default": "Active"},
        {"name": "severity", "default": "Informational"},
    ]

    output_dict = input_dict.copy()
    for field in required_fields:
        if field.get("name") not in output_dict:
            if isinstance(field.get("default"), str):
                output_dict[field.get("name")] = ""
            elif isinstance(field.get("default"), list):
                output_dict[field.get("name")] = []
    return output_dict


def generate_query_params(
    status: str,
    created_time: datetime.datetime = None,
    last_update_time: datetime.datetime = None,
    assigned_to: str = None,
) -> Union[dict, None]:
    """generate_query_params. Generates query params for List Incidents action and Get New Incidents trigger

    :param status: Input status of incidents
    :type status: str

    :param created_time: Time of creation ago of incidents as datetime.datetime object
    :type created_time: datetime.datetime

    :param last_update_time: Time of last update of incidents as datetime.datetime object
    :type last_update_time: datetime.datetime

    :param assigned_to: Member to be assigned to an incident
    :type assigned_to: str

    :rtype: dict
    """

    filter_status = f"status eq '{status}'" if status != "All" else ""
    filter_created_time = f"createdTime ge {created_time.isoformat()}Z" if created_time else ""
    filter_last_update_time = f"lastUpdateTime ge {last_update_time.isoformat()}Z" if last_update_time else ""
    filter_assigned_to = f"assignedTo eq '{assigned_to}'" if assigned_to else ""

    filter_parameters = (filter_status, filter_created_time, filter_last_update_time, filter_assigned_to)
    if not any(filter_parameters):
        return None
    filter_output = ""
    for filter_parameter in filter_parameters:
        if filter_parameter:
            filter_output += filter_parameter + " and "
    if len(filter_output) > 2 and filter_output.split(" ")[-2] == "and":
        filter_output = filter_output[:-5]
    return {"$filter": filter_output}
