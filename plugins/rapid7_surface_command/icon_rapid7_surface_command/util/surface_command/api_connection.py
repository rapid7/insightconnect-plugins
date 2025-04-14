import logging
from requests import Request, Response

import furl

from insightconnect_plugin_runtime.exceptions import (
    APIException,
    HTTPStatusCodes,
    PluginException,
    ResponseExceptionData,
)
from insightconnect_plugin_runtime.helper import make_request


REGION_MAP = {
    "United States": "us",
    "United States 2": "us2",
    "United States 3": "us3",
    "Europe": "eu",
    "Canada": "ca",
    "Australia": "au",
    "Japan": "ap",
}


class ApiConnection:
    """
    ApiConnection(api_key, region_string, logger)

    A class to connect to the Surface Command API. This class provides convenience methods to perform actions
    on Surface Command.
    """

    def __init__(
        self,
        api_key: str,
        region_string: str,
        logger: logging.Logger,
        timeout: int = 90,
    ) -> None:
        """
        Init the connection and set the region
        """
        self.api_key = api_key
        self.logger = logger
        region = REGION_MAP.get(region_string)
        self.url = (
            f"https://{region}.api.insight.rapid7.com/surface/graph-api/objects/table"
        )
        self.timeout = timeout

    def run_query(self, query_id: str) -> dict:
        """
        Execute Surface Command Query
        """
        url = furl.furl(self.url).set(args={"format": "json"})
        request = Request(
            method="post",
            url=url,
            headers={"X-Api-Key": f"{self.api_key}"},
            json={"query_id": query_id},
        )

        try:
            response = make_request(
                _request=request,
                timeout=self.timeout,  # Timeout is properly handled here
                exception_custom_configs={
                    HTTPStatusCodes.UNPROCESSABLE_ENTITY: PluginException(
                        cause="Server was unable to process the request",
                        assistance="Please validate the request to Rapid7 Surface Command",
                    )
                },
                exception_data_location=ResponseExceptionData.RESPONSE,
            )
        except PluginException as exception:
            if isinstance(exception.data, Response):
                raise APIException(
                    cause=exception.cause,
                    assistance=exception.assistance,
                    data=exception.data.text,
                    status_code=exception.data.status_code,
                )
            raise exception

        return response.json()
