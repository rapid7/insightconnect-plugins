from re import sub, match
from typing import Union

_SNAKE_CASE_REGEX = r"\b[a-z0-9]+(_[a-z0-9]+)*\b"
_CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
_PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"


def clean_dict(dict_to_clean: dict) -> dict:
    if not isinstance(dict_to_clean, dict):
        return dict_to_clean
    cleaned_dict = dict_to_clean.copy()
    for key, value in dict_to_clean.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean_dict(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif value in [None, "", 0, [], {}]:
            del cleaned_dict[key]
    return cleaned_dict


def to_camel_case(string_to_convert: str) -> str:
    string_to_convert = string_to_convert.replace(" ", "_")
    if match(_CAMEL_CASE_REGEX, string_to_convert):
        return string_to_convert
    if match(_PASCAL_CASE_REGEX, string_to_convert):
        return string_to_convert[0].lower() + string_to_convert[1:]
    init, *temp = string_to_convert.split("_")
    result = "".join([init.lower(), *map(str.title, temp)])
    return result


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


def filter_dict_keys(dict_to_modify: dict, keys_to_keep: list):
    if not isinstance(dict_to_modify, dict):
        return dict_to_modify
    return {key: dict_to_modify.get(key) for key in keys_to_keep}
