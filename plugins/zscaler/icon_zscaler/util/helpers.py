from insightconnect_plugin_runtime.exceptions import PluginException
from re import sub, match, split
from typing import Union
from icon_zscaler.util.constants import Assistance, Cause

_SNAKE_CASE_REGEX = r"\b[a-z0-9]+(_[a-z0-9]+)*\b"
_CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
_PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"
_CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"


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


def remove_password_from_result(dictionary: dict) -> dict:
    return {key: value for key, value in dictionary.copy().items() if key != "password"}


def prepare_department(department_api_result: list, given_department_name: str) -> dict:
    for department in department_api_result:
        if department.get("name") == given_department_name:
            return department

    raise PluginException(
        cause=Cause.DEPARTMENT_NOT_FOUND,
        assistance=Assistance.VERIFY_INPUT,
    )


def prepare_groups(groups_api_result: list, given_groups_names: list) -> list:
    result_list = []
    available_names = [item.get("name") for item in groups_api_result]

    for name in given_groups_names:
        if name not in available_names:
            raise PluginException(
                cause=Cause.GROUP_NOT_FOUND,
                assistance=Assistance.VERIFY_INPUT,
            )

    for group in groups_api_result:
        for name in given_groups_names:
            if name == group.get("name"):
                result_list.append(group)

    return result_list


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


def filter_dict_keys(dict_to_modify: dict, keys_to_keep: list) -> dict:
    if not isinstance(dict_to_modify, dict):
        return dict_to_modify
    return {key: dict_to_modify.get(key) for key in keys_to_keep if key in dict_to_modify}


def find_custom_url_category_by_name(url_category_name: str, url_categories_list: list) -> dict:
    if not url_categories_list or not url_category_name:
        raise PluginException(
            cause=Cause.CATEGORY_NOT_FOUND,
            assistance=Assistance.VERIFY_INPUT,
        )
    url_category = list(
        filter(lambda category: category.get("configuredName") == url_category_name, url_categories_list)
    )
    if url_category and url_category[0].get("id"):
        return url_category[0]
    else:
        raise PluginException(
            cause=Cause.CATEGORY_NOT_FOUND,
            assistance=Assistance.VERIFY_INPUT,
        )


def find_url_category_by_id(url_category_id: str, url_categories_list: str) -> dict:
    if not url_categories_list or not url_category_id:
        raise PluginException(
            cause=Cause.CATEGORY_NOT_FOUND,
            assistance=Assistance.VERIFY_INPUT,
        )
    url_category = list(filter(lambda category: category.get("id") == url_category_id, url_categories_list))
    if url_category and url_category[0].get("id"):
        return url_category[0]
    else:
        raise PluginException(
            cause=Cause.CATEGORY_NOT_FOUND,
            assistance=Assistance.VERIFY_INPUT,
        )
