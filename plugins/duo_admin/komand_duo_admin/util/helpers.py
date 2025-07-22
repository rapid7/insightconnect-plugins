from typing import Union
from insightconnect_plugin_runtime.helper import return_non_empty


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    return return_non_empty(item_to_clean.copy())


def convert_fields_to_string(provided_logs: list) -> list:
    fields = ["isEncryptionEnabled", "isFirewallEnabled", "isPasswordSet"]
    for log in provided_logs:
        access_device = log.get("accessDevice", {})
        if access_device:
            for field in fields:
                obtained_field = access_device.get(field)
                if isinstance(obtained_field, bool):
                    access_device[field] = str(obtained_field)
            log["accessDevice"] = access_device
    return provided_logs

def convert_string_to_bool(string: str):
    if isinstance(string, str):
        string = string.strip().lower()
        if string == 'true':
            return True
        elif string == 'false':
            return False
    return string
