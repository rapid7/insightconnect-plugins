from typing import Union
from insightconnect_plugin_runtime.helper import return_non_empty


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    return return_non_empty(item_to_clean.copy())


def convert_pascal_case_to_camel_case(provided_string: str) -> str:
    return provided_string[0].lower() + provided_string[1:]


def convert_to_camel_case(to_modify: Union[dict, list]) -> Union[dict, list]:
    if isinstance(to_modify, list):
        return [convert_pascal_case_to_camel_case(element) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            output_dict[convert_pascal_case_to_camel_case(key)] = convert_to_camel_case(value)
        return output_dict
    else:
        return to_modify
