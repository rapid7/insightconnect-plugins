from re import match, split, sub
from typing import Any, Dict, List, Tuple, Union

from insightconnect_plugin_runtime.helper import clean

SNAKE_CASE_REGEX = r"\b[a-z0-9]+(_[a-z0-9]+)*\b"
CAMEL_CASE_REGEX = r"\b[a-z0-9]+([A-Z][a-z]+[0-9]*)*\b"
CAMEL_CASE_ACRONYM_REGEX = r"\b[a-z0-9]+([A-Z]+[0-9]*)*\b"
PASCAL_CASE_REGEX = r"\b[A-Z][a-z]+[0-9]*([A-Z][a-z]+[0-9]*)*\b"

ENTITY_EXTRACT_KEY_NAMES = ("roles", "vcardArray", "entities", "publicIds", "handle")

VCARDS_KEY_NAME_MAPPING = (
    ["fn", "fullname"],
    ["adr", "address"],
    ["tel", "phone"],
    ["geo", "geolocation"],
    ["tz", "timezone"],
    ["org", "organization"],
    ["lang", "language"],
)
VCARDS_KEYS_TO_REMOVE = ("version", "n")
VCARDS_STR_TO_SUBTRACT = ("tel:", "geo:")
VCARD_ADDRESS_KEY_NAME = "address"


def to_camel_case(provided_string: str) -> str:
    if match(CAMEL_CASE_REGEX, provided_string):
        return provided_string
    if match(PASCAL_CASE_REGEX, provided_string):
        return provided_string[0].lower() + provided_string[1:]
    if match(CAMEL_CASE_ACRONYM_REGEX, provided_string):
        words = split(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z0-9])(?=[a-z])", provided_string)
        result = "".join([w.title() for w in words])
        return result[0].lower() + result[1:]
    init, *temp = provided_string.split("_")
    result = "".join([init.lower(), *map(str.title, temp)])
    return result


def convert_keys_to_camel(to_modify: Union[dict, list]) -> Union[dict, list]:
    case_method = to_camel_case

    if isinstance(to_modify, list):
        return [convert_keys_to_camel(element) for element in to_modify]
    elif isinstance(to_modify, dict):
        output_dict = {}
        for key, value in to_modify.items():
            output_dict[case_method(key)] = convert_keys_to_camel(value)
        return output_dict
    else:
        return to_modify


def convert_to_snake_case(input_string: str) -> str:
    """
    convert_to_snake_case. Convert input string Camel Case name to Snake Case.

    :param input_string: Input string in Camel case format.
    :type: str

    :return: Converted input value from Camel case to Snake case.
    :rtype: str
    """

    return sub("([a-z0-9])([A-Z])", r"\1_\2", input_string).lower()


def convert_dict_to_snake_case(
    input_dict: Union[List[Dict[str, Any]], Dict[str, Any]],
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    convert_dict_to_snake_case. Recursively convert a dictionary or nested dictionary keys from Camel to Snake case.

    :param input_dict: Input dictionary for keys to be converted to Snake case.
    :type: Union[List[Dict[str, Any]], Dict[str, Any]]

    :return: Dictionary of all key names converted from Camel to Snake case.
    :type: Union[List[Dict[str, Any]], Dict[str, Any]]
    """

    if isinstance(input_dict, list):
        return [
            convert_dict_to_snake_case(element) if isinstance(element, (dict, list)) else element
            for element in input_dict
        ]
    return {
        convert_to_snake_case(key): convert_dict_to_snake_case(value) if isinstance(value, (dict, list)) else value
        for key, value in input_dict.items()
    }


def extract_keys_from_dict(input_dict: dict, keys_list: list) -> dict:
    return dict((key, input_dict[key]) for key in keys_list if key in input_dict)


def extract_asn_result(result: dict) -> dict:
    return extract_keys_from_dict(
        result, ["asn", "asn_cidr", "asn_country_code", "asn_date", "asn_description", "asn_registry"]
    )


def remove_unnecessary_vcard_prefix(
    value: Any, subtract_values: Union[List[str], Tuple[str]] = VCARDS_STR_TO_SUBTRACT
) -> Any:
    """
    remove_unnecessary_vcard_prefix. Method removes unnecessary prefixes from data specified in a List[str] or Tuple[str].

    :param value:
    :type: Any

    :param subtract_values:
    :type: Union[List[str], Tuple[str]]

    :return: Returns the values without unnecessary prefixes specified in the subtract_values list from string.
    :rtype: Any
    """

    for str_to_subtract in subtract_values:
        if isinstance(value, str) and str_to_subtract in value:
            return value.replace(str_to_subtract, "")
    return value


def rename_dict_keys(input_dict: Dict[str, Any], mapping_rename_list: List[List[str]]) -> Dict[str, Any]:
    """
    rename_dict_keys. Renames a dict key according to a mapping rename list.

    :param input_dict: Input dictionary for the keys to be renamed.
    :type: Dict[str, Any]

    :param mapping_rename_list:
    :type: List[Union[List[str], Tuple[str]]]

    :return: Input dictionary with all keys renamed according to mapping_rename_list.
    :rtype: Dict[str, Any]
    """

    vcards = input_dict.copy()
    for rename_list in mapping_rename_list:
        old_keyname, new_keyname = rename_list[0], rename_list[1]
        if old_keyname in vcards:
            vcards[new_keyname] = vcards.pop(old_keyname)
    return vcards


def parse_vcards(
    vcards: List[List[Union[str, Dict[str, Any]]]],
    address_keyname: str = VCARD_ADDRESS_KEY_NAME,
    keys_to_remove: Union[List[str], Tuple[str]] = VCARDS_KEYS_TO_REMOVE,
) -> Dict[str, Any]:
    """
    parse_vcards. The method parses the vcardArray data structure into key-value dicts.

    :param vcards: Input RDAP vcard entity array.
    :type: List[List[Union[str, Dict[str,Any]]]]

    :param address_keyname: Name of the address key to be parsed.
    :type: str

    :param keys_to_remove: Rename unnecessary keys.
    :type: Union[List[str], Tuple[str]]

    :return: Parsed vcard as dictionary.
    :rtype: Dict[str, Any]
    """

    vcards = rename_dict_keys(
        {vcard[0]: remove_unnecessary_vcard_prefix(vcard[-1]) for vcard in vcards}, VCARDS_KEY_NAME_MAPPING
    )
    vcards[address_keyname] = parse_address_information(vcards.get(address_keyname, [""] * 7))
    for key in keys_to_remove:
        vcards.pop(key, None)
    return clean(vcards)


def parse_address_information(vcard_address: List[str]) -> Union[Dict[str, Any], None]:
    """
    parse_address_information. The method parses all address details from the entity object.
    It returns a dictionary containing non-empty address details data.
    If there is an empty address vcard array, the method returns None.

    :param vcard_address: Vcard address specified array containing address details data.
    :type: List[str]

    :return: Dictionary of parsed address information.
    :rtype: Union[Dict[str, Any], None]
    """

    address_array = vcard_address.copy()
    if len(address_array) < 7:
        address_array += [""] * (7 - len(address_array))

    parsed_address = clean(
        {
            "postOfficeBox": address_array[0],
            "extendedAddress": address_array[1],
            "streetAddress": address_array[2],
            "locality": address_array[3],
            "region": address_array[4],
            "postalCode": address_array[5],
            "countryName": address_array[6],
        }
    )
    return parsed_address if parsed_address else None


def parse_entities(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    parse_entities. Recursively parses entity objects coming from the RDAP response.
    The parsed entities look nicer and are easier to get data from, i.e

    [{
        "roles": ["registrar"],
        "kind": "individual",
        "title": "Research Scientist",
        "role": "Project Lead",
        "email": "user@example.com",
        "fullname": "Joe User",
        "address": {
            "extended_address": "Suite 1234",
            "street_address": "Somewhere",
            "locality": "Sample",
            "region": "Other 1",
            "postal_code": "Test 1",
            "country_name": "Example Country Name 1",
        },
        "phone": "+1-555-555-1234",
        "organization": "Example",
        "language": "en",
    }]

    :param entities: List of RDAP response entity objects.
    :type: List[Dict[str, Any]]

    :return: List of parsed entities.
    :rtype: List[Dict[str, Any]]
    """

    output_list_of_entities = []
    for entity in entities:
        entity = unpack_entities(entity)
        parsed_entity = {}
        for key, value in entity.items():
            parsed_entity.update({key: value})
            if key == "vcardArray":
                parsed_entity.update(parse_vcards(value[1]))
                del parsed_entity[key]
            elif key == "entities":
                output_list_of_entities += parse_entities(value)
                del parsed_entity[key]
        if "roles" in parsed_entity and len(parsed_entity.keys()) > 1:
            output_list_of_entities.append(parsed_entity)
    return output_list_of_entities[::-1]


def unpack_entities(
    entity: Dict[str, Any], key_names: Union[List[str], Tuple[str]] = ENTITY_EXTRACT_KEY_NAMES
) -> Dict[str, Any]:
    """
    unpack_entities. Unpacks the entities from the entity object by extracting the specified keys.

    :param entity: Entity RDAP object.
    :type: Dict[str, Any]

    :param key_names: List of key names to be extracted.
    :type: Union[List[str], Tuple[str]]

    :return: Extracted entity object with specified keys.
    :rtype: Dict[str, Any]
    """

    return extract_keys_from_dict(entity, key_names)


def extract_public_ids(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    parse_public_ids. Extract all public IDs from entities and extend to the general list of public IDs, if any..

    :param entities: Enter a parsed list of entity objects from which to extract public IDs.
    :type: List[Dict[str, Any]]

    :return: List of extracted public IDs.
    :rtype: List[Dict[str, Any]]
    """

    output_list_of_public_ids = []
    for entity in entities:
        output_list_of_public_ids += entity.pop("publicIds", [])
    return output_list_of_public_ids


def extract_nameservers(nameservers: List[Dict[str, Any]]) -> List[str]:
    """
    extract_nameservers. Extracts the nameservers from the nameserver object and converts it to a list of strings.
    Returns the list of nameservers.

    :param nameservers: Nameserver RDAP object containing the ldhName key in it's structure.
    :type: List[Dict[str, Any]]

    :return: List of extracted nameservers.
    :rtype: List[str]
    """

    return clean([nameserver.get("ldhName") for nameserver in nameservers])


def return_non_empty(input_dict: Dict[str, Any]) -> Union[Dict[Any, Any], Any]:
    """
    return_non_empty. Cleans the dictionary recursively.

    :param input_dict: Input dictionary to be cleaned.
    :type input_dict: Dict[str, Any]

    :return: Returns a cleaned up dictionary containing only no empty values.
    :rtype: Union[Dict[Any, Any], None]
    """

    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None and value != "" and value != []:
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            elif isinstance(value, list):
                return_value = [
                    return_non_empty(element) if isinstance(element, dict) else element for element in value
                ]
                return_value = list(filter(None, return_value))
                if return_value:
                    temp_dict[key] = return_value
            else:
                temp_dict[key] = value
    return temp_dict
