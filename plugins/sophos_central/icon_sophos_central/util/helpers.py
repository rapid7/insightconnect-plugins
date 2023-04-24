from typing import Union


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
        elif value in [None, "", [], 0, {}] and not isinstance(value, bool):
            del cleaned_dict[key]
    return cleaned_dict
