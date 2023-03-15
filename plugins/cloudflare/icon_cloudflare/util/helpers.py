from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union
import validators
from re import match, fullmatch, split
from icon_cloudflare.util.constants import Assistance, Cause

_CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
_CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"
_PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"


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


def convert_dict_keys_to_camel_case(to_modify: Union[dict, list]) -> Union[dict, list]:
    if isinstance(to_modify, list):
        return [convert_dict_keys_to_camel_case(element) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            output_dict[to_camel_case(key)] = convert_dict_keys_to_camel_case(value)
        return output_dict
    else:
        return to_modify


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    cleaned_dict = item_to_clean.copy()
    for key, value in item_to_clean.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif value in [None, "", [], 0, {}] and not isinstance(value, bool):
            del cleaned_dict[key]
    return cleaned_dict


def set_configuration(target: str) -> dict:
    if validators.ipv4(target):
        return {"value": target, "target": "ip"}
    if validators.ipv6(target):
        return {"value": target, "target": "ip6"}
    if (validators.ipv4_cidr(target) and target.endswith(("/16", "/24"))) or (
        validators.ipv6_cidr(target) and target.endswith(("/32", "/48", "/64"))
    ):
        return {"value": target, "target": "ip_range"}
    if fullmatch("^[a-zA-Z]{2}$", target):
        return {"value": target, "target": "country"}
    if fullmatch("^(AS|as|As|aS)\d+$", target):
        return {"value": target, "target": "asn"}
    raise PluginException(cause=Cause.INVALID_TARGET.format(target=target), assistance=Assistance.INVALID_TARGET)
