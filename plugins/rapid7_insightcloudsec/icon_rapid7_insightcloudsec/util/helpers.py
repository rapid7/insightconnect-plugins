from datetime import datetime


def parse_date_from_datetime(date_time: str) -> str:
    date_time = date_time.replace("Z", "")
    return str(datetime.fromisoformat(date_time).date())


def process_list(list_to_process: list) -> list:
    new_list = []
    for item in list_to_process:
        if isinstance(item, dict):
            new_list.append(dict_keys_to_camel_case(item))
    return new_list


def dict_keys_to_camel_case(dictionary: dict) -> dict:
    old_keys = list(dictionary.keys())
    new_keys = []
    for key in old_keys:
        split_key = key.split("_")
        new_key = split_key[0]
        if len(split_key) > 1:
            for i, value in enumerate(split_key):
                if i > 0:
                    new_key += value.capitalize()
        new_keys.append(new_key)
    new_dict = {}
    for i, key in enumerate(old_keys):
        key_value = dictionary.get(key)
        if isinstance(key_value, dict):
            key_value = dict_keys_to_camel_case(key_value)
        if isinstance(key_value, list):
            for j, value in enumerate(key_value):
                if isinstance(value, dict):
                    key_value[j] = dict_keys_to_camel_case(value)
                else:
                    break
        new_dict[new_keys[i]] = key_value
    return new_dict
