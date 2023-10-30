from typing import Dict


def inputs_to_query_params(input_dict: Dict) -> Dict:
    """
    Takes a dict of input parameters and returns a dict of query parameters, useful when plugin inputs names do not
    match the API query parameters exactly.
    :param input_dict: dict of input parameters
    :return: dict of query parameters
    """
    query_params = {}
    for key, value in input_dict.items():
        if value is not None:
            query_params[key] = value

    return query_params
