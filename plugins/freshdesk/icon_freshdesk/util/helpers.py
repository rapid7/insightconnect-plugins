import base64
from re import sub
from typing import Union

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_freshdesk.util.constants import Attachment, Ticket, TicketField
import magic


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


def create_attachments_form(attachments: list) -> list:
    form_data = []
    for attachment in attachments:
        name = attachment.get(Attachment.NAME)
        try:
            content = base64.b64decode(attachment.get(Attachment.CONTENT))
        except Exception as error:
            raise PluginException(
                cause="Byte conversion issue.",
                assistance="Please provide valid attachment content and try again. If the issue persists, please contact support.",
            )
        if not name or not content:
            continue
        mime_type = magic.from_buffer(content, mime=True)
        if not mime_type:
            mime_type = "text/plain"
        form_data.append(("attachments[]", (name, content, mime_type)))
    return form_data


def add_keys_prefix(dict_to_modify: dict, prefix: str) -> dict:
    return {f"{prefix}{key}": value for key, value in dict_to_modify.items()}


def replace_ticket_fields_name_to_id(
    dict_to_modify: dict, ticket_fields_to_update: list, all_ticket_fields: list
) -> dict:
    for ticket_field in all_ticket_fields:
        ticket_field_name = ticket_field.get(TicketField.NAME)
        if not ticket_field_name in ticket_fields_to_update or not dict_to_modify.get(ticket_field_name):
            continue
        for key, value in ticket_field.get(TicketField.CHOICES).items():
            if isinstance(value, list):
                if dict_to_modify.get(ticket_field_name) in value:
                    dict_to_modify[ticket_field_name] = int(key)
                    break
            if isinstance(value, int):
                if dict_to_modify.get(ticket_field_name) == key:
                    dict_to_modify[ticket_field_name] = int(value)
                    break
        else:
            raise PluginException(
                cause=f"`{ticket_field_name} = {dict_to_modify.get(ticket_field_name)}` was not found.",
                assistance="Please provide valid ticket field value and try again. If the issue persists, please contact support.",
            )
    return dict_to_modify


def replace_ticket_fields_id_to_name(
    dict_to_modify: dict, ticket_fields_to_update: list, all_ticket_fields: list
) -> dict:
    for ticket_field in all_ticket_fields:
        ticket_field_name = ticket_field.get(TicketField.NAME)
        if not ticket_field_name in ticket_fields_to_update:
            continue
        for key, value in ticket_field.get(TicketField.CHOICES).items():
            if isinstance(value, list):
                if str(dict_to_modify.get(ticket_field_name)) == str(key):
                    dict_to_modify[ticket_field_name] = value[0]
                    break
            if isinstance(value, int):
                if str(dict_to_modify.get(ticket_field_name)) == str(value):
                    dict_to_modify[ticket_field_name] = key
                    break

    return dict_to_modify


def camel_to_snake_case(s):
    return "_".join(sub("([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))).split()).lower()


def snake_to_camel_case(s):
    init, *temp = s.split("_")
    return "".join([init.lower(), *map(str.title, temp)])


def convert_dict_keys_case(to_modify: Union[dict, list], case_type: str) -> Union[dict, list]:
    if case_type == "camel_case":
        case_method = snake_to_camel_case
    elif case_type == "snake_case":
        case_method = camel_to_snake_case
    else:
        return to_modify

    if isinstance(to_modify, list):
        return [convert_dict_keys_case(element, case_type) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            if camel_to_snake_case(key) == Ticket.CUSTOM_FIELDS:
                output_dict[case_method(key)] = value
            else:
                output_dict[case_method(key)] = convert_dict_keys_case(value, case_type)
        return output_dict
    else:
        return to_modify
