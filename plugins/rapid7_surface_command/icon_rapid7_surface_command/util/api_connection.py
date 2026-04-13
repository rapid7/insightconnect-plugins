import logging
from typing import Dict, List, Any
from requests import Request, Response

import furl

from insightconnect_plugin_runtime.exceptions import (
    APIException,
    HTTPStatusCodes,
    PluginException,
    ResponseExceptionData,
)
from insightconnect_plugin_runtime.helper import make_request

from icon_rapid7_surface_command.util.util import _csv_text_to_json_rows


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
        self.base_url = f"https://{region_string}.api.insight.rapid7.com/surface"
        self.url = f"{self.base_url}/graph-api/objects/table"
        self.timeout = timeout

    def run_query(self, query_id: str) -> list:
        """
        Execute Saved Surface Command Query
        """
        url = furl.furl(self.url).set(args={"format": "csv"})
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
                ) from exception
            raise exception

        csv_text = response.text
        rows = _csv_text_to_json_rows(csv_text)

        return rows

    def run_adhoc_query(self, cypher: str) -> list:
        """
        Execute Adhoc Surface Command Query
        """
        url = furl.furl(self.url).set(args={"format": "csv"})
        request = Request(
            method="post",
            url=url,
            headers={"X-Api-Key": f"{self.api_key}"},
            json={"cypher": cypher},
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
                ) from exception
            raise exception

        csv_text = response.text
        rows = _csv_text_to_json_rows(csv_text)

        return rows

    def tag_assets(self, object_ids: List[str], tags: List[str], operation: str) -> Dict[str, Any]:
        """
        Add, set, or remove tags on multiple assets in bulk.

        operation must be one of:
          "add"    -> POST   /graph-api/objects/id/{id}/tags  (append tags, duplicates ignored)
          "set"    -> PUT    /graph-api/objects/id/{id}/tags  (replace all tags)
          "remove" -> DELETE /graph-api/objects/id/{id}/tags  (remove specified tags)
        """
        method_map = {"add": "POST", "set": "PUT", "remove": "DELETE"}
        http_method = method_map[operation]

        success_count = 0
        failures: List[Dict[str, str]] = []

        for object_id in object_ids:
            url = f"{self.base_url}/graph-api/objects/id/{object_id}/tags"
            request = Request(
                method=http_method,
                url=url,
                headers={"X-Api-Key": self.api_key},
                json=tags,
            )
            try:
                make_request(
                    _request=request,
                    timeout=self.timeout,
                    exception_custom_configs={
                        HTTPStatusCodes.UNPROCESSABLE_ENTITY: PluginException(
                            cause="Server was unable to process the request",
                            assistance="Please validate the object ID and tags",
                        )
                    },
                    exception_data_location=ResponseExceptionData.RESPONSE,
                )
                success_count += 1
            except PluginException as exception:
                self.logger.warning(f"Failed to tag asset {object_id}: {exception.cause}")
                failures.append({"object_id": object_id, "error": exception.cause})
            except Exception as exception:
                self.logger.warning(f"Unexpected error tagging asset {object_id}: {exception}")
                failures.append({"object_id": object_id, "error": str(exception)})

        return {
            "success_count": success_count,
            "failure_count": len(failures),
            "failures": failures,
        }
