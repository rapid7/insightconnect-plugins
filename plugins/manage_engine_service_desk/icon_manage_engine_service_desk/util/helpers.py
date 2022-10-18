import json

from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus


def prepare_input_data(params: dict) -> dict:
    return {"input_data": json.dumps(clean(params))}


def replace_status_code(response: dict) -> dict:
    try:
        response[Response.RESPONSE_STATUS]["manage_engine_status_code"] = response.get(
            Response.RESPONSE_STATUS, {}
        ).pop(ResponseStatus.STATUS_CODE)
        return response
    except KeyError:
        return response


def map_ids_to_integer(response: dict) -> dict:
    if not isinstance(response, dict):
        return response
    mapped_response = response.copy()
    for key, value in response.items():
        if isinstance(value, dict):
            mapped_response[key] = map_ids_to_integer(value)
        if isinstance(value, list):
            mapped_response[key] = [map_ids_to_integer(element) for element in value]
        if key.endswith("id") and isinstance(value, str):
            try:
                mapped_response[key] = int(value)
            except ValueError:
                continue
    return mapped_response


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


def remove_other_keys(input_dict: dict, keys_to_keep: list) -> dict:
    if not isinstance(input_dict, dict):
        return input_dict
    return {key: input_dict.get(key) for key in keys_to_keep}
