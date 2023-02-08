from typing import Union
from icon_topdesk.util.constants import (
    INCIDENT_FIELDS_WITH_ITEM_ID,
    INCIDENT_FIELDS_WITH_ITEM_NAME,
    INCIDENT_FIELDS_WITH_EMAIL,
    INCIDENT_FIELDS_WITH_NUMBER,
    SKIP_FIELDS,
)


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
        elif value in [None, "", [], 0, {}, "None"] and not isinstance(value, bool):
            del cleaned_dict[key]
    return cleaned_dict


def prepare_incident_payload(parameters: dict) -> dict:
    payload = {}
    for key in parameters.keys():
        value = parameters.get(key)
        if key in INCIDENT_FIELDS_WITH_ITEM_ID:
            payload[key] = {"id": value}
        elif key in INCIDENT_FIELDS_WITH_ITEM_NAME:
            payload[key] = {"name": value}
        elif key in INCIDENT_FIELDS_WITH_NUMBER:
            payload[key] = {"number": value}
        elif key in INCIDENT_FIELDS_WITH_EMAIL:
            payload[key] = {"email": value}
        elif key == "caller":
            payload[key] = prepare_incident_payload(value)
        elif key not in SKIP_FIELDS:
            payload[key] = value
    return clean(payload)
