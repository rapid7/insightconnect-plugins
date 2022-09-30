from datetime import datetime

from insightconnect_plugin_runtime.exceptions import PluginException


def clean_dict(dictionary: dict) -> dict:
    cleaned_dict = dictionary.copy()
    for key, value in dictionary.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean_dict(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif value in [None, "", 0, [], {}]:
            del cleaned_dict[key]
    return cleaned_dict


def iso8601_to_utc_date(iso_date: str) -> str:
    try:
        if "+" in iso_date and not iso_date.endswith("Z"):
            datetime.fromisoformat(iso_date)
            return f"{iso_date.split('+')[0]}Z"
        return iso_date
    except ValueError as error:
        raise PluginException(
            "Invalid date format", "Please provide date in proper format as described in documentation", error
        )


def rename_keys(response: dict, rename_from: str, rename_to: str) -> dict:
    response_copy = response.copy()
    if isinstance(response_copy, list):
        response_copy = [rename_keys(element, rename_from, rename_to) for element in response_copy]
    if not isinstance(response_copy, dict):
        return response_copy
    for key, value in response.items():
        if key == rename_from:
            response_copy[rename_to] = response_copy.pop(rename_from, None)
        elif isinstance(value, (dict, list)):
            response_copy[key] = rename_keys(value, rename_from, rename_to)
    return response_copy
