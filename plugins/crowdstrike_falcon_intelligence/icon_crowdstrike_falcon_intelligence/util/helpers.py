from re import sub
from typing import Union
import re

from icon_crowdstrike_falcon_intelligence.util.constants import TextCase


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


def camel_to_snake_case(s):
    return "_".join(sub("([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))).split()).lower()


def snake_to_camel_case(s):
    init, *temp = s.split("_")
    return "".join([init.lower(), *map(str.title, temp)])


def convert_dict_keys_case(to_modify: Union[dict, list], case_type: str) -> Union[dict, list]:
    if case_type == TextCase.CAMEL_CASE:
        case_method = snake_to_camel_case
    elif case_type == TextCase.SNAKE_CASE:
        case_method = camel_to_snake_case
    else:
        return to_modify

    if isinstance(to_modify, list):
        return [convert_dict_keys_case(element, case_type) for element in to_modify]
    elif isinstance(to_modify, dict):
        return {case_method(key): convert_dict_keys_case(value, case_type) for key, value in to_modify.items()}
    else:
        return to_modify


def split_utc_date_time(utc_date_time: str) -> (str, str):
    if not utc_date_time or not "T" in utc_date_time or not "+" in utc_date_time:
        return None, None
    splitted_date_time = re.split("T|\+", utc_date_time)
    return splitted_date_time[0], ":".join(splitted_date_time[1].split(":")[:2])
