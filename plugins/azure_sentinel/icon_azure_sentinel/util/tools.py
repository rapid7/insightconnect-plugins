from typing import Any, Dict, List


def return_non_empty(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    """return_non_empty. Cleans up recusively the dictionary

    :param input_dict:
    :type input_dict: Dict[str, Any]
    :rtype: Dict[Any, Any]
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None and value != "":
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            elif isinstance(value, list):
                if len(value) > 0:
                    temp_dict[key] = value
            else:
                temp_dict[key] = value
    return temp_dict


def map_output(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    etag = input_dict.get("etag")
    if etag:
        input_dict["etag"] = etag.replace('"', "")
    return input_dict


def map_output_for_list(input_dict: List[Dict]) -> List[Dict]:
    output_list = []
    for element in input_dict:
        output_list.append(map_output(element))
    return output_list
