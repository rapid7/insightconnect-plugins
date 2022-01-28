from icon_ibm_qradar.util.constants.constant import HTTPS


class URL:
    """Url class to handle the URL endpoints."""

    def __init__(self, host_url, endpoint):
        """Initialize the URL class.

        :param host_url: Hostname
        :param endpoint: Target Endpoint
        """
        self.host_url = host_url
        self.endpoint = endpoint

        self.basic_url = f"{self.host_url}/{self.endpoint}"

    def get_basic_url(self) -> str:
        """To get the basic URL."""
        return self.basic_url

    def set_basic_url(self, basic_url: str):
        """To Set the basic URL."""
        self.basic_url = basic_url
