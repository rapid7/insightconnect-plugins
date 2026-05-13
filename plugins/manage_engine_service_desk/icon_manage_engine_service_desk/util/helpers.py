import json

from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import (
    Priority,
    Request,
    Response,
    ResponseStatus,
    Status,
    Time,
    User,
)


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


def clean_dict(dictionary: dict) -> dict:
    cleaned_dict = dictionary.copy()
    for key, value in dictionary.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean_dict(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif isinstance(value, bool):
            if not value:
                del cleaned_dict[key]
        elif value in [None, "", 0, [], {}]:
            del cleaned_dict[key]
    return cleaned_dict


def remove_other_keys(input_dict: dict, keys_to_keep: list) -> dict:
    if not isinstance(input_dict, dict):
        return input_dict
    return {key: input_dict.get(key) for key in keys_to_keep}


def safe_get(data, *keys, default=None):
    """Safely traverse nested dicts/lists that may contain None values.

    Examples:
        safe_get(response, "request", "id") -> response["request"]["id"] or default
        safe_get(response, "response_status", "status") -> handles None at any level
        safe_get(response, "created_time", "display_value") -> handles null timestamps
    """
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        elif isinstance(data, list) and isinstance(key, int) and key < len(data):
            data = data[key]
        else:
            return default
        if data is None:
            return default
    return data


def normalize_note_response(response: dict) -> dict:
    """Normalize Cloud API 'request_note' key to 'note' so actions can use a consistent key."""
    if "request_note" in response and "note" not in response:
        response["note"] = response.pop("request_note")
    return response


def transform_request(request: dict) -> dict:
    """Normalize a raw API request object to the plugin's output schema.

    Filters user, priority, and status objects to only the fields defined in
    the output schema, and extracts the display_value string from timestamp fields.
    """
    for user_field in [Request.TECHNICIAN, Request.CREATED_BY, Request.REQUESTER]:
        request[user_field] = remove_other_keys(request.get(user_field) or {}, [User.ID, User.NAME, User.IS_VIPUSER])

    request[Request.PRIORITY] = remove_other_keys(request.get(Request.PRIORITY) or {}, [Priority.NAME, Priority.ID])
    request[Request.STATUS] = remove_other_keys(request.get(Request.STATUS) or {}, [Status.NAME, Status.ID])
    request[Request.CREATED_TIME] = safe_get(request, Request.CREATED_TIME, Time.DISPLAY_VALUE)
    request[Request.DUE_BY_TIME] = safe_get(request, Request.DUE_BY_TIME, Time.DISPLAY_VALUE)
    return remove_other_keys(request, Request().get_all_attributes())
