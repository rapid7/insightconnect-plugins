from insightconnect_plugin_runtime.exceptions import PluginException
from re import sub, match, split
from typing import Union
from icon_happyfox.util.constants import TextCase, Cause, Assistance
from datetime import datetime
import base64
import mimetypes

_CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
_CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"
_PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"


def camel_to_snake_case(provided_string: str) -> str:
    return "_".join(
        sub("([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", provided_string.replace("-", " "))).split()
    ).lower()


def to_camel_case(provided_string: str) -> str:
    if match(_CAMEL_CASE_REGEX, provided_string):
        return provided_string
    if match(_PASCAL_CASE_REGEX, provided_string):
        return provided_string[0].lower() + provided_string[1:]
    if match(_CAMEL_CASE_ACRONYM_REGEX, provided_string):
        words = split(r"(?<=[a-z\d])(?=[A-Z])|(?<=[A-Z\d])(?=[a-z])", provided_string)
        result = "".join([word.title() for word in words])
        return result[0].lower() + result[1:]
    init, *temp = provided_string.split("_")
    return "".join([init.lower(), *map(str.title, temp)])


def convert_dict_keys_case(to_modify: Union[dict, list], case_type: str) -> Union[dict, list]:
    if case_type == TextCase.CAMEL_CASE:
        case_method = to_camel_case
    elif case_type == TextCase.SNAKE_CASE:
        case_method = camel_to_snake_case
    else:
        return to_modify

    if isinstance(to_modify, list):
        return [convert_dict_keys_case(element, case_type) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            output_dict[case_method(key)] = convert_dict_keys_case(value, case_type)
        return output_dict
    else:
        return to_modify


def clean_dict(dict_to_clean: dict) -> dict:
    if not isinstance(dict_to_clean, dict):
        return dict_to_clean
    cleaned_dict = dict_to_clean.copy()
    for key, value in dict_to_clean.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean_dict(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif value is False:
            continue
        elif value in [None, "", 0, [], {}]:
            del cleaned_dict[key]
    return cleaned_dict


def parse_date_from_datetime(date_time: str) -> str:
    date_time = date_time.replace("Z", "")
    return str(datetime.fromisoformat(date_time).date())


def prepare_ticket_payload(parameters: dict) -> dict:
    custom_fields = parameters.get("customFields")
    due_date = parameters.get("dueDate")
    if not parameters.get("text") and not parameters.get("html"):
        raise PluginException(
            cause=Cause.NO_TEXT_AND_HTML,
            assistance=Assistance.NO_TEXT_AND_HTML,
        )
    json_data = convert_dict_keys_case(parameters, TextCase.SNAKE_CASE)
    json_data.pop("custom_fields")
    if due_date:
        json_data["due_date"] = parse_date_from_datetime(due_date)
    if custom_fields:
        json_data.update(custom_fields)
    return clean_dict(json_data)


def prepare_attachments(provided_attachments: list) -> list:
    attachments = []
    if provided_attachments:
        for attachment in provided_attachments:
            filename = attachment.get("filename")
            mime_type = mimetypes.guess_type(filename)[0]
            if not mime_type:
                mime_type = "text/plain"
            attachments.append(("attachments", (filename, base64.b64decode(attachment.get("content")), mime_type)))
    return attachments


def compare_custom_fields(provided_custom_fields: dict, available_custom_fields: list):
    keys = provided_custom_fields.keys()
    available_keys = []
    for custom_field in available_custom_fields:
        available_keys.append(custom_field.get("id"))
    for key in keys:
        if key not in available_keys:
            raise PluginException(
                cause=Cause.CUSTOM_FIELD_NOT_FOUND.format(key=key),
                assistance=Assistance.CUSTOM_FIELD_NOT_FOUND.format(available_custom_fields=available_custom_fields),
            )
