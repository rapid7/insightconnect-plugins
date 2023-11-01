from typing import Dict


def clean_ax_response(resp: Dict) -> Dict:
    """
    Remove null values from the action set
    :param resp:
    :return:
    """
    return dict(filter(lambda k: k[1] is not None, resp.items()))
