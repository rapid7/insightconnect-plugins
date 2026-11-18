import json
import random
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional
from urllib.parse import urlsplit

import requests

from icon_whoisfreaks.util import constants
from icon_whoisfreaks.util.errors import (
    RETRYABLE_KINDS,
    SERVICE_FEED,
    SERVICE_LOOKUP,
    SERVICE_STATUS,
    Kind,
    WhoisFreaksError,
    classify,
    from_transport_exception,
    redact,
)


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int
    base_delay: float
    max_delay: float


LOOKUP_RETRY = RetryPolicy(max_attempts=4, base_delay=2.0, max_delay=60.0)
FEED_RETRY = RetryPolicy(max_attempts=4, base_delay=5.0, max_delay=300.0)


@dataclass
class LookupResult:
    status_code: int
    data: Any = None
    found: bool = True
    message: str = ""

    @property
    def data_dict(self) -> dict:
        return self.data if isinstance(self.data, dict) else {}


@dataclass
class _Request:
    method: str
    url: str
    operation: str
    service: str
    timeout: tuple
    retry: RetryPolicy
    max_bytes: int
    params: Optional[dict] = None
    body: Optional[dict] = None
    send_key: bool = True
    passthrough: frozenset = field(default_factory=frozenset)


@dataclass
class _RawResponse:
    status_code: int
    headers: Any
    body: bytes


_STATUS_MESSAGES = {
    206: "Partial record: WhoisFreaks returned incomplete data from the upstream server",
    210: "Cached record: the live upstream server did not answer, so WhoisFreaks returned its cached record",
}


def _query_value(value: Any) -> Any:
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


def _clean_params(params: Optional[dict]) -> Optional[dict]:
    if not params:
        return None
    return {key: _query_value(value) for key, value in params.items() if value is not None and value != ""}


def _error_message(body: bytes) -> str:
    text = body.decode("utf-8", errors="replace").strip()
    try:
        data = json.loads(text)
    except ValueError:
        return text[:300]
    if isinstance(data, dict):
        return str(data.get("message") or data.get("error") or "")[:500]
    return text[:300]


class WhoisFreaksClient:
    """HTTP client for the WhoisFreaks lookup and feed APIs.

    The API key is only ever sent in the X-API-KEY header, redirects are never followed and every error is
    classified into a WhoisFreaksError whose message cannot contain the key.
    """

    def __init__(self, api_key: str, logger, sleep: Callable[[float], None] = time.sleep):
        self._api_key = api_key
        self._logger = logger
        self._sleep = sleep
        self._local = threading.local()
        self._throttle_lock = threading.Lock()
        self._throttle_until = 0.0

    # Public API

    def lookup(
        self, operation: str, method: str, path: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> LookupResult:
        request = _Request(
            method=method,
            url=f"{constants.API_BASE_URL}{path}",
            operation=operation,
            service=SERVICE_LOOKUP,
            timeout=constants.LOOKUP_TIMEOUT,
            retry=LOOKUP_RETRY,
            max_bytes=constants.MAX_LOOKUP_BODY_BYTES,
            params=_clean_params(params),
            body=body,
            passthrough=frozenset({Kind.NOT_FOUND}),
        )
        raw = self._send(request)
        if raw.status_code >= 300:
            return LookupResult(raw.status_code, None, False, _error_message(raw.body) or "No record found")
        data = self._parse_json(raw, operation)
        return LookupResult(raw.status_code, data, True, _STATUS_MESSAGES.get(raw.status_code, ""))

    def get_feed_status(self) -> dict:
        request = _Request(
            method="GET",
            url=f"{constants.FILES_BASE_URL}{constants.PATH_FEED_STATUS}",
            operation="Feed status",
            service=SERVICE_STATUS,
            timeout=constants.LOOKUP_TIMEOUT,
            retry=FEED_RETRY,
            max_bytes=constants.MAX_LOOKUP_BODY_BYTES,
            send_key=False,
        )
        data = self._parse_json(self._send(request), request.operation)
        if not isinstance(data, dict):
            raise WhoisFreaksError(Kind.INVALID_RESPONSE, request.operation, detail="expected a JSON object")
        return data

    def get_feed_page(self, operation: str, path: str, params: dict) -> Optional[str]:
        """Return the text of one feed page, or None when WhoisFreaks reports the end of the feed date."""
        request = _Request(
            method="GET",
            url=f"{constants.FILES_BASE_URL}{path}",
            operation=operation,
            service=SERVICE_FEED,
            timeout=constants.FEED_TIMEOUT,
            retry=FEED_RETRY,
            max_bytes=constants.MAX_FEED_BODY_BYTES,
            params=_clean_params(params),
            passthrough=frozenset({Kind.END_OF_DATA}),
        )
        raw = self._send(request)
        if raw.status_code >= 300:
            return None
        text = raw.body.decode("utf-8-sig", errors="replace")
        if text.lstrip()[:1] in ("{", "["):
            return self._feed_json_error(text, raw.status_code, operation)
        return text

    # Request execution

    def _send(self, request: _Request) -> _RawResponse:
        attempt = 0
        while True:
            attempt += 1
            raw = None
            try:
                raw = self._perform(request)
                if raw.status_code < 300:
                    return raw
                error = self._http_error(request, raw)
                if error.kind in request.passthrough:
                    return raw
            except WhoisFreaksError as transport_error:
                error = transport_error
            if not self._should_retry(error, request, attempt):
                raise error
            delay = self._retry_delay(error, raw, attempt, request.retry)
            self._logger.warning(
                "%s: %s (attempt %d of %d), retrying in %.1f seconds",
                request.operation,
                error.kind,
                attempt,
                request.retry.max_attempts,
                delay,
            )
            self._sleep(delay)

    def _perform(self, request: _Request) -> _RawResponse:
        self._wait_for_rate_limit(request.retry.max_delay)
        headers = {"User-Agent": constants.USER_AGENT, "Accept": "application/json, text/csv, text/plain"}
        if request.send_key:
            headers["X-API-KEY"] = self._api_key
        host = urlsplit(request.url).hostname or ""
        try:
            response = self._session().request(
                request.method,
                request.url,
                params=request.params,
                json=request.body,
                headers=headers,
                timeout=request.timeout,
                allow_redirects=False,
                stream=True,
            )
        except requests.RequestException as exception:
            raise from_transport_exception(exception, request.operation, host) from None
        try:
            body = self._read_body(response, request, host)
        finally:
            response.close()
        self._remember_rate_limit(response.headers)
        return _RawResponse(response.status_code, response.headers, body)

    def _read_body(self, response: requests.Response, request: _Request, host: str) -> bytes:
        chunks, size = [], 0
        try:
            for chunk in response.iter_content(chunk_size=65536):
                size += len(chunk)
                if size > request.max_bytes:
                    raise WhoisFreaksError(
                        Kind.INVALID_RESPONSE,
                        request.operation,
                        detail=f"response larger than {request.max_bytes} bytes",
                    )
                chunks.append(chunk)
        except requests.RequestException as exception:
            raise from_transport_exception(exception, request.operation, host) from None
        return b"".join(chunks)

    def _http_error(self, request: _Request, raw: _RawResponse) -> WhoisFreaksError:
        message = redact(_error_message(raw.body), (self._api_key,))
        kind = classify(raw.status_code, message, request.service)
        # 429 responses are never charged and 503 means the request was not processed
        safe_post = raw.status_code in (429, 503)
        return WhoisFreaksError(kind, request.operation, raw.status_code, message, safe_to_retry_post=safe_post)

    @staticmethod
    def _should_retry(error: WhoisFreaksError, request: _Request, attempt: int) -> bool:
        if attempt >= request.retry.max_attempts or error.kind not in RETRYABLE_KINDS:
            return False
        # Bulk POST requests are charged per item, so only retry when WhoisFreaks cannot have processed them
        return request.method != "POST" or error.safe_to_retry_post

    @staticmethod
    def _retry_delay(error: WhoisFreaksError, raw: Optional[_RawResponse], attempt: int, policy: RetryPolicy) -> float:
        delay = policy.base_delay * (2 ** (attempt - 1))
        if error.kind == Kind.RATE_LIMITED and raw is not None:
            reset = _rate_limit_reset_seconds(raw.headers)
            if reset is not None:
                delay = reset
        return min(max(delay, 1.0), policy.max_delay) + random.uniform(0, 1)  # nosec B311 - jitter only

    def _parse_json(self, raw: _RawResponse, operation: str) -> Any:
        try:
            return json.loads(raw.body.decode("utf-8-sig"))
        except ValueError:
            raise WhoisFreaksError(Kind.INVALID_RESPONSE, operation, raw.status_code, detail="not valid JSON") from None

    def _feed_json_error(self, text: str, http_status: int, operation: str) -> Optional[str]:
        """A JSON body from a feed endpoint is always an error, whatever the HTTP status."""
        try:
            data = json.loads(text)
        except ValueError:
            raise WhoisFreaksError(Kind.INVALID_RESPONSE, operation, http_status, detail="malformed JSON") from None
        data = data if isinstance(data, dict) else {}
        status = data.get("status") if isinstance(data.get("status"), int) else http_status
        if status < 300:
            status = 400
        message = redact(str(data.get("message") or data.get("error") or ""), (self._api_key,))[:500]
        kind = classify(status, message, SERVICE_FEED)
        if kind == Kind.END_OF_DATA:
            return None
        raise WhoisFreaksError(kind, operation, status, message)

    # Connection and rate limit handling

    def _session(self) -> requests.Session:
        session = getattr(self._local, "session", None)
        if session is None:
            session = requests.Session()
            self._local.session = session
        return session

    def _remember_rate_limit(self, headers) -> None:
        remaining = headers.get("X-RateLimit-Remaining-Requests")
        reset = _rate_limit_reset_seconds(headers)
        if remaining is None or reset is None:
            return
        try:
            exhausted = int(remaining) <= 0
        except ValueError:
            return
        if exhausted:
            with self._throttle_lock:
                self._throttle_until = time.monotonic() + reset

    def _wait_for_rate_limit(self, max_wait: float) -> None:
        with self._throttle_lock:
            wait = self._throttle_until - time.monotonic()
        if wait > 0:
            wait = min(wait, max_wait)
            self._logger.info("WhoisFreaks rate limit window exhausted, waiting %.1f seconds", wait)
            self._sleep(wait)


def _rate_limit_reset_seconds(headers) -> Optional[float]:
    nanoseconds = headers.get("X-RateLimit-Remaining-Time")
    if nanoseconds is not None:
        try:
            return max(float(nanoseconds) / 1_000_000_000, 0.0)
        except ValueError:
            pass
    retry_after = headers.get("Retry-After")
    if retry_after is not None:
        try:
            return max(float(retry_after), 0.0)
        except ValueError:
            pass
    return None
