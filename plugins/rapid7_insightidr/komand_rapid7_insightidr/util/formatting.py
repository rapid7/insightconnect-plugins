import json
from typing import Dict


def refactor_message(message: Dict) -> Dict:
    """
    Taking message and returning it as formatted json
    Args:
        message: event["message"] from query's result_response

    Returns:
        new_message: Formatted json
    """
    new_message = json.loads(str(message).replace("\n", "\\n").replace("'", '"'))
    return new_message
