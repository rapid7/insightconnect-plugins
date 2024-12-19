import logging

import furl
import requests

from constants import REGION_MAP
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from insightconnect_plugin_runtime.helper import clean


class ApiConnection:
    """
    ApiConnection(api_key, region_string, logger)

    A class to connect to the Surface Command API. This class provides convenience methods to perform actions
    on Surface Command.
    """

    def __init__(self, api_key: str, region_string: str, logger: logging.Logger) -> None:
        """
        Init the connection and set the region
        """
        self.api_key = api_key
        self.logger = logger
        region = REGION_MAP.get(region_string)
        self.url = f'https://{region}.api.insight.rapid7.com/surface/graph-api/objects/table'

    def run_query(self, query_id: str) -> dict:
        """
        Execute Surface Command Query
        """
        url = furl.furl(self.url).set(args={"format": "json"})
        response = requests.post(
            url,
            headers={
                "X-Api-Key": f"{self.api_key}"
            },
            json={"query_id": query_id},
        )
        response.raise_for_status()
        return response.json()
