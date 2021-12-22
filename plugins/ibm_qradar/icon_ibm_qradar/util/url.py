"""Includes the Url class."""
from icon_ibm_qradar.util.constants.constant import HTTPS


class URL:
    """Url class to handle the url end points."""

    def __init__(self, hostname, endpoint):
        """Initialize of URL class.

        :param hostname: Hostname
        :param endpoint: Target Endpoint
        """
        self.hostname = hostname
        self.endpoint = endpoint

    def get_basic_url(self):
        """To structure the basic url for the qradar."""
        basic_url = f"{HTTPS}://{self.hostname}/{self.endpoint}"
        return basic_url
