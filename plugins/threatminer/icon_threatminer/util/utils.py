import copy
from functools import wraps
from typing import Any, Callable, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_threatminer.util.constants import RESULTS_FIELD_NAME, STATUS_CODE_FIELD_NAME


def convert_str_to_int(api_status_code: str) -> int:
    try:
        return int(api_status_code)
    except ValueError:
        raise PluginException(
            cause="Unexpected status code received from Threatminer",
            assistance="Please contact support",
            data=api_status_code,
        )


def extract_field_from_response(api_resp: Dict[str, Any], field_name: str) -> Any:
    try:
        return api_resp[field_name]
    except KeyError:
        raise PluginException(
            cause=f"No '{field_name}' received from Threatminer",
            assistance="Please contact support",
            data=api_resp,
        )


def convert_status_code_field_to_int(response: Dict[str, Any], field_name: str) -> dict:
    # avoid side effects
    response_copy = copy.deepcopy(response)

    # convert str to int
    response_copy[field_name] = convert_str_to_int(extract_field_from_response(response, field_name))
    return response_copy


def prune_domain(url: str) -> str:
    if url.startswith("http://"):
        return url.replace("http://", "").split("/")[0]
    if url.startswith("https://"):
        return url.replace("https://", "").split("/")[0]
    return url.split("/")[0]


def normalize_response_data(function_: Callable) -> Callable:
    @wraps(function_)
    def wrapper(*args, **kwargs):
        response = convert_status_code_field_to_int(function_(*args, **kwargs), STATUS_CODE_FIELD_NAME)
        results = response.get(RESULTS_FIELD_NAME, [])
        if results and isinstance(results, list):
            try:
                if not isinstance(results[0], dict):
                    response[RESULTS_FIELD_NAME] = [{"value": element} for element in results]
            except IndexError:
                pass
        return response

    return wrapper
