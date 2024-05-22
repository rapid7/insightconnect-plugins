from typing import Union
from insightconnect_plugin_runtime.helper import return_non_empty

from urllib.parse import urlparse


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    return return_non_empty(item_to_clean.copy())


def get_hostname(hostname: str) -> str:
    return hostname.replace("https://", "").replace("http://", "")


def validate_url(url: str) -> bool:
    """
    Check domain against allowedHost list for Okta.
    Return True if Okta URL is valid, False otherwise
    :param url: The URL to check
    :type: str

    :return: boolean indicating if URL is valid
    :rtype: bool
    """
    if not url.startswith(("http://", "https://")):
        prefix = "https://"
        url = prefix + url

    domain = urlparse(url).netloc

    # checks to validate domain and ensure a subdomain is present
    if not domain.endswith((".okta.com", ".oktapreview.com", ".okta-emea.com")):
        return False

    return True
