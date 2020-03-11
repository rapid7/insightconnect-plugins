from typing import Dict, List, Callable
from urllib.parse import urljoin


def transform(data: Dict, *modifiers: Callable[[Dict], None]) -> Dict:
    """
    Generic functions that allows to generate new dictionary
    by applying any number of modifications on the input dictionary

    :param data: original dictionary
    :param modifiers:  functions to apply on the dictionary
    :return: generated dictionary
    """
    for modify in modifiers:
        modify(data)
    return data


def serialize_fields(fields: [str]) -> [Callable[[Dict], None]]:
    """
    Generate list serialization modifiers(closures)for multiple fields
    """
    modifiers = []
    # generate closures
    for field in fields:
        modifier = serialize_field(field)
        modifiers.append(modifier)
    return modifiers


def serialize_field(field: str) -> Callable[[Dict], None]:
    """
    Generate closure that can serialize specific field  in dictionary
    """

    def f(data: Dict):
        """
        Serialize specific field of type list
        """
        if field in data and isinstance(data[field], List):
            data[field] = ",".join(data[field])

    return f


def normalize_published_field(data: Dict):
    if not data["published_at"]:
        data["published_at"] = "unknown"


def flatten_data_field(data: Dict):
    """Moves nested 'data' field to the root of the dictionary"""
    for k, v in data["data"].items():
        if k not in data:
            data[k] = v


def serialize_alternate_ids(data: Dict):
    """Transforms alternate ids of vulnerability into a joined string"""
    alternate_ids = data.pop("alternate_ids")
    unified_names = [aid["unified_name"] for aid in alternate_ids]
    unified_names = ",".join(unified_names)
    data["alternate_ids"] = unified_names


def generate_link_attr(d: Dict):
    """Generates valid content API URL"""
    d.update({"link": urljoin(
        "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/",
        d.get("identifier"))})
    d.pop("identifier")


def pop_non_relevant_module_fields(data: Dict):
    """
    Removes fields not required for module content action
    :param data:
    :return:
    """
    keys_to_keep = ["title", "description", "content_type", "published_at",
                    "references",
                    "architectures", "authors", "rank", "reliability"]
    for key in list(data):
        if key not in keys_to_keep:
            data.pop(key)


def pop_non_relevant_vuln_fields(data: Dict):
    """Removes fields not required for vulnerability content action"""
    keys_to_keep = ["title", "description", "content_type", "published_at",
                    "references",
                    "severity", "solutions", "alternate_ids"]
    for key in list(data):
        if key not in keys_to_keep:
            data.pop(key)


def pop_non_relevant_search_fields(data: Dict):
    """
    Removes fields not required for search action
    """
    keys_to_keep = ["title", "published_at", "identifier"]
    for key in list(data):
        if key not in keys_to_keep:
            data.pop(key)
