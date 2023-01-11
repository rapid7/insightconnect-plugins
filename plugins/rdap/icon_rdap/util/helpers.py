from re import sub, match, split
from typing import Union

from insightconnect_plugin_runtime.exceptions import PluginException


_SNAKE_CASE_REGEX = r"\b[a-z0-9]+(_[a-z0-9]+)*\b"
_CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
_CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"
_PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"


def to_camel_case(provided_string: str) -> str:
    if match(_CAMEL_CASE_REGEX, provided_string):
        return provided_string
    if match(_PASCAL_CASE_REGEX, provided_string):
        return provided_string[0].lower() + provided_string[1:]
    if match(_CAMEL_CASE_ACRONYM_REGEX, provided_string):
        words = split(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z0-9])(?=[a-z])", provided_string)
        result = "".join([w.title() for w in words])
        return result[0].lower() + result[1:]
    init, *temp = provided_string.split("_")
    result = "".join([init.lower(), *map(str.title, temp)])
    return result


def convert_keys_to_camel(to_modify: Union[dict, list]) -> Union[dict, list]:
    case_method = to_camel_case

    if isinstance(to_modify, list):
        return [convert_keys_to_camel(element) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            output_dict[case_method(key)] = convert_keys_to_camel(value)
        return output_dict
    else:
        return to_modify


def extract_keys_from_dict(input_dict: dict, keys_list: list) -> dict:
    return dict((key, input_dict[key]) for key in keys_list if key in input_dict)


def extract_asn_result(result: dict) -> dict:
    return extract_keys_from_dict(
        result, ["asn", "asn_cidr", "asn_country_code", "asn_date", "asn_description", "asn_registry"]
    )
