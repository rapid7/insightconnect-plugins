import re


def hide_api_key(string):
    """
    ThreatStream queries expose the API key as a URL query parameter. This method hides the API key using a regex that
    substitutes with the replacement the first instance in string of a substring that matches pattern.
    The pattern regex matches the api_key URL query parameter. It captures whether or not another parameter
    follows the api_key value in the group named" "end" with an &. The replacement regex retains the end group.
    """
    pattern = r"api_key=([a-zA-Z0-9]+)(?P<end>\&|$)"
    replacement = r"api_key=********\g<end>"
    return re.sub(pattern, replacement, string)
