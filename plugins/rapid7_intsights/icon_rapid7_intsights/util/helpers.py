from re import match, split
from typing import Union
from icon_rapid7_intsights.util.constants import accepted_empty_fields

CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"
CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"


def to_camel_case(provided_string: str) -> str:
    if match(CAMEL_CASE_REGEX, provided_string):
        return provided_string
    if match(PASCAL_CASE_REGEX, provided_string):
        return provided_string[0].lower() + provided_string[1:]
    if match(CAMEL_CASE_ACRONYM_REGEX, provided_string):
        words = split(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z0-9])(?=[a-z])", provided_string)
        result = "".join([w.title() for w in words])
        return result[0].lower() + result[1:]
    init, *temp = provided_string.split("_")
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
        elif value and isinstance(value, list):
            if isinstance(value[0], dict):
                cleaned_dict[key] = [clean(item.copy()) for item in value]
        elif key in accepted_empty_fields:
            continue
        elif value in [None, "", [], 0, {}] and not isinstance(value, bool):
            del cleaned_dict[key]
    return cleaned_dict
