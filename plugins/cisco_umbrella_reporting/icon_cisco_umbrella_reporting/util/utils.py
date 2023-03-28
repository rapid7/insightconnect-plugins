from typing import Dict, Any, List, Union


def extract_keys_from_dict(input_dict: Dict[str, Any], keys_list: List[str]) -> Dict[str, Any]:
    """
    extract_keys_from_dict. Extracts key specified from dictionary and returns that in new, modified dictionary.

    :param input_dict: Input dictionary for the keys to be extracted.
    :type: Dict[str, Any]

    :param keys_list: List of keys to be extracted.
    :type: List[str]

    :return: Returns new dictionary containing extracted keys. If keys don't exist on the input_dict the empty dictionary is returned.
    :rtype: Dict[str, Any]
    """

    return dict((key, input_dict[key]) for key in keys_list if key in input_dict)


def convert_date_time_to_iso(date: str, time: str) -> str:
    """
    convert_date_time_to_iso. Converts inserted date and time to ISO format.

    :param date: Input date in format YYYY-MM-DD.
    :type: str

    :param time: Input time in format HH-MM-SS.
    :type: str

    :return: String representation of datetime in ISO format.
    :rtype: str
    """

    return f"{date}T{time}" if date and time else ""


def extract_get_domain_record_keys(input_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    extract_get_domain_record_keys. Renames the output dictionary record structure and maps its output field to a specific pattern.

    :param input_dict: Input dictionary containing activity record element.
    :type: Dict[str, Any]

    :return: Returns mapped new dictionary.
    :rtype: Dict[str, Any]
    """

    return return_non_empty(
        {
            "externalIp": input_dict.get("externalip"),
            "internalIp": input_dict.get("internalip"),
            "datetime": convert_date_time_to_iso(input_dict.get("date"), input_dict.get("time")),
            "timestamp": input_dict.get("timestamp"),
            "queryType": input_dict.get("querytype"),
            "verdict": input_dict.get("verdict"),
            "categories": [category.get("label", "") for category in input_dict.get("categories", [])],
            "domain": input_dict.get("domain"),
            "identities": [
                extract_keys_from_dict(identity, ["id", "label", "deleted"])
                for identity in input_dict.get("identities", [])
            ],
            "threats": input_dict.get("threats"),
            "allApplications": [application.get("label", "") for application in input_dict.get("allapplications", [])],
            "allowedApplications": [
                application.get("label", "") for application in input_dict.get("allowedapplications", [])
            ],
            "blockedApplications": [
                application.get("label", "") for application in input_dict.get("blockedapplications", [])
            ],
        }
    )


def convert_get_domain_output(list_of_dict: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    convert_get_domain_output. Converts the Get Domain output to extracted new list of dictionaries.

    :param list_of_dict: Input list of dictionaries containing activity record elements.
    :type: List[Dict[str, Any]]

    :return: Returns mapped new dictionary.
    :rtype: List[Dict[str, Any]]
    """

    return [extract_get_domain_record_keys(element) for element in list_of_dict]


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
