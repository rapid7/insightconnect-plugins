from typing import Any, Dict


def return_non_empty(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    """Cleans up a dictionary recurisvely from None values and empty dictionaries.

    Args:
        input_dict (Dict[str, Any]): input dictionary

    Returns:
        Dict[str, Any]: sanitized dictionary
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value:
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            else:
                temp_dict[key] = value
    return temp_dict
