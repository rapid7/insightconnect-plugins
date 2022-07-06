import json
import xmltodict


def xml_to_json(xml_string: str) -> str:
    if not xml_string:
        return ""
    try:
        return json.dumps(xmltodict.parse(xml_string), indent=2)
    except xmltodict.expat.ExpatError:
        return xml_string


def dict_to_list(item) -> list:
    if isinstance(item, dict):
        return [item]
    return item
