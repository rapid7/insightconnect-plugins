import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional, Tuple
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

# HTTP status codes that warrant a retry (transient server/network errors)
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
# HTTP status codes that indicate a permanent failure — no point retrying
NON_RETRYABLE_STATUS_CODES = {400, 401, 403, 404, 422}


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

    def _tag_single_asset(self, object_id: str, http_method: str, tags: List[str]) -> None:
        """Issue one tagging request for a single asset. Raises on failure."""
        url = f"{self.base_url}/graph-api/objects/id/{object_id}/tags"
        request = Request(
            method=http_method,
            url=url,
            headers={"X-Api-Key": self.api_key},
            json=tags,
        )
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

    def _tag_single_asset_with_retry(
        self,
        object_id: str,
        http_method: str,
        tags: List[str],
        max_retries: int,
    ) -> Tuple[str, Optional[str]]:
        """
        Tag one asset, retrying up to max_retries times on transient errors.

        Returns (object_id, None) on success or (object_id, error_message) on
        permanent failure. Never raises.
        """
        last_error: Optional[str] = None
        for attempt in range(max_retries + 1):
            try:
                self._tag_single_asset(object_id, http_method, tags)
                return object_id, None
            except PluginException as exc:
                last_error = exc.cause
                status = exc.data.status_code if isinstance(exc.data, Response) else None

                # Non-retryable: bad request, auth, not-found — fail immediately.
                if status in NON_RETRYABLE_STATUS_CODES:
                    return object_id, f"[{status}] {exc.cause}"

                if attempt < max_retries:
                    # Honour Retry-After on 429; otherwise exponential back-off.
                    if status == 429 and isinstance(exc.data, Response):
                        delay = float(exc.data.headers.get("Retry-After", 2**attempt))
                    else:
                        delay = float(2**attempt)
                    self.logger.warning(
                        f"Attempt {attempt + 1}/{max_retries + 1} failed for asset {object_id} "
                        f"(status={status}), retrying in {delay:.0f}s: {exc.cause}"
                    )
                    time.sleep(delay)
            except Exception as exc:
                last_error = str(exc)
                if attempt < max_retries:
                    delay = float(2**attempt)
                    self.logger.warning(
                        f"Attempt {attempt + 1}/{max_retries + 1} unexpected error for asset {object_id}, "
                        f"retrying in {delay:.0f}s: {exc}"
                    )
                    time.sleep(delay)

        return object_id, last_error

    def tag_assets(
        self,
        object_ids: List[str],
        tags: List[str],
        operation: str,
        max_workers: int = 10,
        max_retries: int = 3,
    ) -> Dict[str, Any]:
        """
        Add, set, or remove tags on multiple assets in bulk.

        Requests are issued concurrently (up to max_workers at a time) and each
        asset is retried up to max_retries times on transient errors before being
        recorded as a failure.

        operation must be one of:
          "add"    -> POST   /graph-api/objects/id/{id}/tags  (append tags, duplicates ignored)
          "set"    -> PUT    /graph-api/objects/id/{id}/tags  (replace all tags)
          "remove" -> DELETE /graph-api/objects/id/{id}/tags  (remove specified tags)
        """
        method_map = {"add": "POST", "set": "PUT", "remove": "DELETE"}
        http_method = method_map[operation]

        success_count = 0
        failures: List[Dict[str, str]] = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self._tag_single_asset_with_retry, oid, http_method, tags, max_retries): oid
                for oid in object_ids
            }
            for future in as_completed(futures):
                try:
                    oid, error = future.result()
                except Exception as exc:
                    # Should not happen — _tag_single_asset_with_retry never raises.
                    oid = futures[future]
                    self.logger.warning(f"Unexpected executor error for asset {oid}: {exc}")
                    failures.append({"object_id": oid, "error": str(exc)})
                    continue

                if error is None:
                    success_count += 1
                else:
                    self.logger.warning(f"Failed to tag asset {oid}: {error}")
                    failures.append({"object_id": oid, "error": error})

        return {
            "success_count": success_count,
            "failure_count": len(failures),
            "failures": failures,
        }
