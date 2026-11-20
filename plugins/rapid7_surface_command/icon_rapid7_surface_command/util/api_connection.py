import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote
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
# Seconds to wait for a Surface Command response; large saved queries can take minutes to run.
# Kept below the 180 second limit the cloud executor enforces on an action.
DEFAULT_TIMEOUT = 170
# Async table jobs: ask for a job straight away, and keep each async action below the cloud's 240 second limit
ASYNC_PREFER = "respond-async, wait=0"
DEFAULT_MAX_WAIT = 180
MAX_WAIT_LIMIT = 200
# Time budget for the requests of one async action, under the 240 second cloud limit. requests applies a timeout
# per read, so a slow download of a large final result can still run somewhat longer.
ACTION_BUDGET = 230
DEFAULT_RETRY_AFTER = 5
UNAVAILABLE_RETRIES = 2
TRANSIENT_STATUS_CODES = {429, 502, 504}
JOB_STATUS_RUNNING = "running"
JOB_STATUS_COMPLETE = "complete"


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
        timeout: int = DEFAULT_TIMEOUT,
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

    def start_query(self, query_id: Optional[str] = None, cypher: Optional[str] = None) -> Dict[str, Any]:
        """
        Start a saved (query_id) or adhoc (cypher) query as an async table job.

        Returns {"status": "running", "job_id": ...} once Surface Command has accepted the job, or
        {"status": "complete", "items": [...]} if the job had already finished (e.g. a cached result).
        Requests and retries are limited to ACTION_BUDGET seconds.
        """
        body = {"query_id": query_id} if query_id else {"cypher": cypher}
        url = furl.furl(self.url).set(args={"format": "csv"})
        deadline = time.monotonic() + ACTION_BUDGET
        retried = False

        while True:
            request = Request(
                method="post",
                url=url,
                headers={"X-Api-Key": f"{self.api_key}", "Prefer": ASYNC_PREFER},
                json=body,
            )
            try:
                response = self._send(request, deadline, allowed_status_codes=[HTTPStatusCodes.SERVICE_UNAVAILABLE])
            except PluginException as exception:
                if exception.preset == PluginException.Preset.TIMEOUT:
                    raise (
                        self._busy_error(exception.data) if retried else self._no_job_error(exception.data)
                    ) from exception
                raise

            if response.status_code == 202:
                return {"status": JOB_STATUS_RUNNING, "job_id": self._job_id_from_response(response), "items": []}
            if response.status_code == 200:
                return {"status": JOB_STATUS_COMPLETE, "job_id": "", "items": _csv_text_to_json_rows(response.text)}
            # Not retried: the query may already be running, and a second POST would start it again
            if response.status_code == HTTPStatusCodes.GATEWAY_TIMEOUT:
                raise self._no_job_error(response.text)
            if response.status_code not in {HTTPStatusCodes.SERVICE_UNAVAILABLE, HTTPStatusCodes.TOO_MANY_REQUESTS}:
                raise self._status_error(response)

            # 503 (too many jobs) or 429: no work was started, so retry while time remains
            delay = self._retry_after(response)
            if time.monotonic() + delay >= deadline:
                raise self._busy_error(response.text)
            self.logger.info(f"Surface Command returned {response.status_code}, retrying in {delay}s")
            time.sleep(delay)
            retried = True

    def get_query_result(self, job_id: str, max_wait: int = DEFAULT_MAX_WAIT) -> Dict[str, Any]:
        """
        Get the rows of an async table job, checking again every Retry-After seconds for up to max_wait seconds
        (capped at MAX_WAIT_LIMIT). Requests and retries are limited to ACTION_BUDGET seconds.

        Returns {"status": "complete", "items": [...]} when the job has finished, or {"status": "running"} if it is
        still running when the wait is over. Raises if the job failed, was cancelled, or has expired.
        """
        url = f"{self.url}/jobs/{quote(job_id, safe='')}"
        start = time.monotonic()
        deadline = start + ACTION_BUDGET
        wait_until = start + min(max(max_wait, 0), MAX_WAIT_LIMIT)
        unavailable = 0

        while True:
            response = self._check_job(url, job_id, deadline)
            if response is None:
                # The check itself ran out of time; the job is still there, so report it as not finished yet
                return {"status": JOB_STATUS_RUNNING, "job_id": job_id, "items": []}
            if response.status_code == 200:
                return {"status": JOB_STATUS_COMPLETE, "job_id": job_id, "items": _csv_text_to_json_rows(response.text)}
            if response.status_code == HTTPStatusCodes.SERVICE_UNAVAILABLE:
                # A job lost while Surface Command restarted keeps answering 503; a gateway blip does not. Settle it
                # within the action budget even after max_wait, so a lost job is never reported as still running.
                unavailable += 1
                delay = self._retry_after(response)
                if unavailable > UNAVAILABLE_RETRIES or time.monotonic() + delay >= deadline:
                    raise PluginException(
                        cause=f"The query job {job_id} failed because Surface Command was unavailable.",
                        assistance="Start the query again with Start a Query.",
                        data=response.text,
                    )
                time.sleep(delay)
                continue
            if response.status_code == 202:
                unavailable = 0  # the job answered, so earlier 503s were gateway blips
            elif time.monotonic() >= wait_until:
                raise self._status_error(response)

            remaining = wait_until - time.monotonic()
            if remaining <= 0:
                return {"status": JOB_STATUS_RUNNING, "job_id": job_id, "items": []}
            time.sleep(min(self._retry_after(response), remaining))

    def _check_job(self, url: str, job_id: str, deadline: float) -> Optional[Response]:
        """GET the job once. Returns None if the check timed out; raises if the job has expired or was cancelled."""
        request = Request(method="get", url=url, headers={"X-Api-Key": f"{self.api_key}"})
        try:
            response = self._send(
                request,
                deadline,
                allowed_status_codes=[
                    HTTPStatusCodes.NOT_FOUND,
                    HTTPStatusCodes.GONE,
                    HTTPStatusCodes.SERVICE_UNAVAILABLE,
                ],
            )
        except PluginException as exception:
            if exception.preset == PluginException.Preset.TIMEOUT:
                self.logger.warning(f"Checking query job {job_id} timed out: {exception.data}")
                return None
            raise
        if response.status_code == HTTPStatusCodes.NOT_FOUND:
            raise PluginException(
                cause=f"The query job {job_id} was not found or has expired.",
                assistance="Query results are kept for 1 hour. Start the query again with Start a Query.",
                data=response.text,
            )
        if response.status_code == HTTPStatusCodes.GONE:
            raise PluginException(
                cause=f"The query job {job_id} was cancelled.",
                assistance="Start the query again with Start a Query.",
                data=response.text,
            )
        return response

    def _send(self, request: Request, deadline: float, allowed_status_codes: List[int]) -> Response:
        """
        Send a table request whose timeout never runs past the deadline. Errors carry the server's status and
        response text, as in run_query; temporary gateway errors (429/502/504) are returned for the caller to retry.
        """
        timeout = max(min(self.timeout or DEFAULT_TIMEOUT, deadline - time.monotonic()), 1)
        try:
            return make_request(
                _request=request,
                timeout=timeout,
                exception_custom_configs={
                    HTTPStatusCodes.UNPROCESSABLE_ENTITY: PluginException(
                        cause="Server was unable to process the request",
                        assistance="Please validate the request to Rapid7 Surface Command",
                    )
                },
                exception_data_location=ResponseExceptionData.RESPONSE,
                allowed_status_codes=allowed_status_codes + list(TRANSIENT_STATUS_CODES),
            )
        except PluginException as exception:
            if isinstance(exception.data, Response):
                raise APIException(
                    cause=exception.cause,
                    assistance=exception.assistance,
                    data=exception.data.text,
                    status_code=exception.data.status_code,
                ) from exception
            raise

    @staticmethod
    def _busy_error(data: Any) -> PluginException:
        return PluginException(
            cause="Surface Command is busy and did not accept the query in time.",
            assistance="Try again later.",
            data=data,
        )

    @staticmethod
    def _no_job_error(data: Any) -> PluginException:
        # Surface Command only returns a job when async table queries are enabled for the organization;
        # otherwise it ignores the Prefer header and runs the whole query in the request, which then times out.
        return PluginException(
            cause="Surface Command did not return a query job before the request timed out.",
            assistance="This usually means async table queries (ASYNC_TABLE_QUERIES) are not enabled for this "
            "organization, in which case the query may still be running. Check the setting, or use Run a Saved Query "
            "or Run an Adhoc Query instead.",
            data=data,
        )

    @staticmethod
    def _status_error(response: Response) -> APIException:
        return APIException(
            cause=f"Surface Command returned HTTP {response.status_code}.",
            assistance="Try again later. If the issue persists, please contact support.",
            data=response.text,
            status_code=response.status_code,
        )

    @staticmethod
    def _job_id_from_response(response: Response) -> str:
        """The job ID is the last segment of the relative Location header (table/jobs/{id}); fall back to the body."""
        location = response.headers.get("Location", "")
        job_id = location.rstrip("/").rsplit("/", 1)[-1] if location else ""
        if not job_id:
            try:
                payload = response.json()
            except ValueError:
                payload = None
            job_id = payload.get("id", "") if isinstance(payload, dict) else ""
        if not job_id:
            raise PluginException(
                cause="Surface Command accepted the query but did not return a job ID.",
                assistance="Please contact support.",
                data=response.text,
            )
        return job_id

    @staticmethod
    def _retry_after(response: Response) -> int:
        try:
            return max(int(response.headers.get("Retry-After", DEFAULT_RETRY_AFTER)), 1)
        except (TypeError, ValueError):
            return DEFAULT_RETRY_AFTER

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
                oid, error = future.result()

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
