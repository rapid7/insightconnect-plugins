from typing import Any, Dict, Union

import yaml


def extract_output_from_stdout(input_stdout: str, output_prefix: str) -> Union[Dict[str, Any], None]:
    """
    Extract output from a string representing standard output.

    This function parses the provided `input_stdout` string and extracts any output data
    that start with the specified `output_prefix`. The extracted output is returned as a
    dictionary where the keys are the extracted output lines without the prefix.

    :param input_stdout: The string representing the standard output to extract from.
    :type: str

    :param output_prefix: The prefix indicating the lines to extract from `input_stdout`.
    :type: str

    :return: A dictionary containing the extracted output.
    :rtype: Union[Dict[str, Any], None]
    """

    if output_prefix in input_stdout:
        function_output = yaml.safe_load(input_stdout[input_stdout.index(output_prefix) + len(output_prefix) :])
        if isinstance(function_output, str) and function_output.lower().strip() == "none":
            return None
        return function_output
    return None
