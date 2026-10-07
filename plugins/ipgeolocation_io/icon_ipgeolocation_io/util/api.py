import logging
import time
from typing import Any, Dict, List, Optional, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import JSONDecodeError, RequestException, Timeout

from .constants import (
    BASE_URL,
    DEFAULT_ASSISTANCE,
    DEFAULT_CAUSE,
    DEFAULT_TIMEOUT,
    ENDPOINT_ABUSE,
    ENDPOINT_ASN,
    ENDPOINT_IPGEO,
    ENDPOINT_IPGEO_BULK,
    ENDPOINT_SECURITY,
    ENDPOINT_SECURITY_BULK,
    HEADER_CREDITS_CHARGED,
    HEADER_SUCCESSFUL_RECORDS,
    MAX_RETRIES,
    MAX_RETRY_AFTER_SECONDS,
    RETRY_BACKOFF_SECONDS,
    RETRYABLE_STATUS_CODES,
    STATUS_ASSISTANCE,
    STATUS_CAUSES,
)


class IPGeolocationAPI:
    """Thin client over the IPGeolocation.io v3 REST API."""

    def __init__(self, api_key: str, logger: logging.Logger, timeout: int = DEFAULT_TIMEOUT):
        self.api_key = api_key
        self.logger = logger
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    # ------------------------------------------------------------------
    # Public endpoint wrappers
    # ------------------------------------------------------------------

    def test_connection(self) -> Dict[str, Any]:
        """
        Look up the orchestrator's own public IP to prove the key works.

        /v3/ipgeo is the only endpoint available on every subscription tier, so
        it is the only safe choice for a connection test. The call costs one
        credit.
        """

        return self.get(ENDPOINT_IPGEO)

    def ip_geolocation(self, params: Dict[str, Any], user_agent: Optional[str] = None) -> Dict[str, Any]:
        headers = {"User-Agent": user_agent} if user_agent else None
        return self.get(ENDPOINT_IPGEO, params=params, headers=headers)

    def ip_geolocation_bulk(self, ips: List[str], params: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.post(ENDPOINT_IPGEO_BULK, ips=ips, params=params)

    def ip_security(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return self.get(ENDPOINT_SECURITY, params=params)

    def ip_security_bulk(self, ips: List[str], params: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.post(ENDPOINT_SECURITY_BULK, ips=ips, params=params)

    def asn_lookup(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return self.get(ENDPOINT_ASN, params=params)

    def abuse_contact(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return self.get(ENDPOINT_ABUSE, params=params)

    # ------------------------------------------------------------------
    # Transport
    # ------------------------------------------------------------------

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        return self._call("GET", endpoint, params=params, headers=headers)

    def post(
        self, endpoint: str, ips: List[str], params: Optional[Dict[str, Any]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        return self._call("POST", endpoint, params=params, json_body={"ips": ips})

    def _call(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Send one request, retrying transient failures, and return parsed JSON.

        The API key travels as a query parameter, so it is deliberately never
        included in any log line or exception message.
        """

        url = f"{BASE_URL}{endpoint}"
        query = {key: value for key, value in (params or {}).items() if value is not None}
        query["apiKey"] = self.api_key

        loggable = {key: value for key, value in query.items() if key != "apiKey"}
        self.logger.info(f"Calling {method} {endpoint} with parameters {loggable}")

        last_error: Optional[Exception] = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = self.session.request(
                    method,
                    url,
                    params=query,
                    json=json_body,
                    headers=headers,
                    timeout=self.timeout,
                )
            except Timeout as error:
                last_error = error
                self.logger.info(f"Request to {endpoint} timed out on attempt {attempt} of {MAX_RETRIES}")
                if attempt == MAX_RETRIES:
                    raise PluginException(preset=PluginException.Preset.TIMEOUT, data=str(error))
                self._sleep(attempt)
                continue
            except RequestsConnectionError as error:
                last_error = error
                self.logger.info(f"Could not reach {endpoint} on attempt {attempt} of {MAX_RETRIES}")
                if attempt == MAX_RETRIES:
                    raise PluginException(
                        preset=PluginException.Preset.SERVICE_UNAVAILABLE,
                        data=str(error),
                    )
                self._sleep(attempt)
                continue
            except RequestException as error:
                raise PluginException(
                    cause="The request to IPGeolocation.io could not be sent.",
                    assistance="Verify the orchestrator has outbound HTTPS access to api.ipgeolocation.io.",
                    data=str(error),
                )

            self._log_usage(response)

            if response.status_code in RETRYABLE_STATUS_CODES and attempt < MAX_RETRIES:
                delay = self._retry_delay(response, attempt)
                self.logger.info(
                    f"IPGeolocation.io returned {response.status_code}. "
                    f"Retrying in {delay} second(s), attempt {attempt} of {MAX_RETRIES}"
                )
                time.sleep(delay)
                continue

            if response.status_code not in (200, 201):
                self._raise_for_status(response)

            return self._parse(response)

        # Only reachable when every attempt raised a retryable transport error.
        raise PluginException(
            preset=PluginException.Preset.SERVICE_UNAVAILABLE,
            data=str(last_error) if last_error else "No response received from IPGeolocation.io.",
        )

    # ------------------------------------------------------------------
    # Response handling
    # ------------------------------------------------------------------

    @staticmethod
    def _parse(response: requests.Response) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        try:
            return response.json()
        except (JSONDecodeError, ValueError):
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=response.text[:1000],
            )

    def _log_usage(self, response: requests.Response) -> None:
        """Surface the credit headers so operators can reconcile usage."""

        credits_charged = response.headers.get(HEADER_CREDITS_CHARGED)
        if credits_charged:
            self.logger.info(f"IPGeolocation.io charged {credits_charged} credit(s) for this request")

        successful_records = response.headers.get(HEADER_SUCCESSFUL_RECORDS)
        if successful_records:
            self.logger.info(
                f"IPGeolocation.io returned data for {successful_records} entries. "
                "The remaining entries were invalid, private, or bogon addresses."
            )

    @staticmethod
    def _extract_message(response: requests.Response) -> Optional[str]:
        """Pull the API's own error text out of the body, when there is one."""

        try:
            body = response.json()
        except (JSONDecodeError, ValueError):
            text = (response.text or "").strip()
            return text[:500] or None

        if isinstance(body, dict):
            for key in ("message", "error", "detail"):
                value = body.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()

        return None

    def _raise_for_status(self, response: requests.Response) -> None:
        status = response.status_code
        message = self._extract_message(response)

        cause = STATUS_CAUSES.get(status, DEFAULT_CAUSE)
        assistance = STATUS_ASSISTANCE.get(status, DEFAULT_ASSISTANCE)

        if status >= 500:
            cause = f"IPGeolocation.io returned a server error ({status})."
            assistance = (
                "This is a problem on the IPGeolocation.io side. Check https://status.ipgeolocation.io "
                "and retry the action."
            )

        if message:
            cause = f"{cause} The API reported: {message}"

        self.logger.error(f"IPGeolocation.io responded with HTTP {status}")

        raise PluginException(cause=cause, assistance=assistance, data=message or response.text[:1000])

    # ------------------------------------------------------------------
    # Retry helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _sleep(attempt: int) -> None:
        time.sleep(RETRY_BACKOFF_SECONDS**attempt)

    @staticmethod
    def _retry_delay(response: requests.Response, attempt: int) -> int:
        """Honour Retry-After when the server sends a usable one, else back off."""

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(max(int(float(retry_after)), 1), MAX_RETRY_AFTER_SECONDS)
            except (TypeError, ValueError):
                pass

        return min(RETRY_BACKOFF_SECONDS**attempt, MAX_RETRY_AFTER_SECONDS)
