from icon_bitwarden.util.constants import ValueType


available_statuses = {"-1-Revoked": -1, "0-Invited": 0, "1-Accepted": 1, "2-Confirmed": 2}

available_types = {"0-Owner": 0, "1-Admin": 1, "2-User": 2, "3-Manager": 3}


def switch_member_status_and_type(member: dict, to_type: str) -> dict:
    """Replaces member fields 'status' and 'type':
    ex. 'status': 0 -> 'status': '0-Invited'
        'status': '0-Invited' -> 'status': 0
        'type': 0 -> 'type': '0-Owner'
        'type': '0-Owner' -> 'type': 0
    """
    member_status = member.get("status")
    member_type = member.get("type")

    if member_status is not None:
        if to_type == ValueType.STRING and isinstance(member_status, int):
            member["status"] = dict(map(reversed, available_statuses.items())).get(member_status)
        if to_type == ValueType.INTEGER and isinstance(member_status, str):
            member["status"] = available_statuses.get(member_status)

    if member_type is not None:
        if to_type == ValueType.STRING and isinstance(member_type, int):
            member["type"] = dict(map(reversed, available_types.items())).get(member_type)
        if to_type == ValueType.INTEGER and isinstance(member_type, str):
            member["type"] = available_types.get(member_type)

    return member


def clean_dict(dict_to_clean: dict) -> dict:
    if not isinstance(dict_to_clean, dict):
        return dict_to_clean
    cleaned_dict = dict_to_clean.copy()
    for key, value in dict_to_clean.items():
        if isinstance(value, dict):
            cleaned_dict[key] = clean_dict(value)
            if cleaned_dict[key] == {}:
                del cleaned_dict[key]
        elif value in [None, "", [], {}]:
            del cleaned_dict[key]
    return cleaned_dict
