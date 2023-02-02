import json
from typing import Dict


def refactor_message(message: Dict) -> Dict:
    """
    Takes message and returning it as formatted json
    :param message: event["message"] from query's result_response
    :returns: new_message: Formatted json
    """
    new_message = json.loads(str(message).replace("\n", "\\n").replace("'", '"'))
    return new_message
