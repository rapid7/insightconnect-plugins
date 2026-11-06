import re
from typing import Optional

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class Kind:
    INVALID_CREDENTIALS = "invalid_credentials"
    ACCOUNT_BLOCKED = "account_blocked"
    NO_CREDITS = "no_credits"
    NOT_ENTITLED = "not_entitled"
    PLAN_LIMIT = "plan_limit"
    BAD_REQUEST = "bad_request"
    LIST_TOO_LARGE = "list_too_large"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    END_OF_DATA = "end_of_data"
    DATE_NOT_AVAILABLE = "date_not_available"
    RESERVED_IP = "reserved_ip"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    UPSTREAM_TIMEOUT = "upstream_timeout"
    RATE_LIMITED = "rate_limited"
    SERVER_ERROR = "server_error"
    NETWORK = "network"
    TIMEOUT = "timeout"
    TLS = "tls"
    REDIRECT = "redirect"
    INVALID_RESPONSE = "invalid_response"
    UNEXPECTED = "unexpected"


# Failures that are expected to clear on their own and are worth retrying with backoff
RETRYABLE_KINDS = frozenset({Kind.RATE_LIMITED, Kind.SERVER_ERROR, Kind.NETWORK, Kind.TIMEOUT, Kind.UPSTREAM_TIMEOUT})

SERVICE_LOOKUP = "lookup"
SERVICE_FEED = "feed"
SERVICE_STATUS = "status"

_SUPPORT = "If the problem persists, contact support@whoisfreaks.com"

_TEXT = {
    Kind.INVALID_CREDENTIALS: (
        "WhoisFreaks rejected the API key",
        "Verify the API key in the plugin connection. If the key was rotated or deactivated, update the connection "
        "with an active key from the WhoisFreaks dashboard",
    ),
    Kind.ACCOUNT_BLOCKED: (
        "The WhoisFreaks account is blocked",
        f"WhoisFreaks blocked the account because of suspicious activity. {_SUPPORT}",
    ),
    Kind.NO_CREDITS: (
        "The WhoisFreaks account has no remaining credits or no active plan",
        "Top up API credits or upgrade the plan in the WhoisFreaks dashboard. Run the Get Account Usage action to "
        "check the remaining balance",
    ),
    Kind.NOT_ENTITLED: (
        "The requested data is not included in the WhoisFreaks subscription",
        "Newly registered domain feeds, threat feeds and lookup credits are sold separately. Add the product to the "
        "WhoisFreaks subscription, or disable the workflow that uses it",
    ),
    Kind.PLAN_LIMIT: (
        "The WhoisFreaks plan limit was reached",
        f"The plan request or download limit is exhausted, or the subscription was cancelled. Renew or upgrade the "
        f"plan in the WhoisFreaks dashboard. {_SUPPORT}",
    ),
    Kind.BAD_REQUEST: (
        "WhoisFreaks rejected the request parameters",
        "Check the action inputs against the action documentation and try again",
    ),
    Kind.LIST_TOO_LARGE: (
        "The request contains too many items",
        "Bulk requests accept at most 100 items. Split the list into smaller requests",
    ),
    Kind.FORBIDDEN: (
        "WhoisFreaks does not provide this lookup for the requested domain",
        "WHOIS is not available for some TLDs and for inactive TLDs. Use the Historical WHOIS action for these "
        "domains",
    ),
    Kind.NOT_FOUND: (
        "WhoisFreaks has no record for the request",
        "Check the input value. No record exists for it in WhoisFreaks",
    ),
    Kind.END_OF_DATA: (
        "No more feed data is available for the requested date",
        "This is the normal end of a feed date",
    ),
    Kind.DATE_NOT_AVAILABLE: (
        "The requested feed date is not available",
        "The date is outside the availability window published by the WhoisFreaks status endpoint",
    ),
    Kind.RESERVED_IP: (
        "WhoisFreaks does not look up private, reserved or bogon IP addresses",
        "Only public IP addresses can be looked up",
    ),
    Kind.METHOD_NOT_ALLOWED: (
        "WhoisFreaks does not accept this request method for the endpoint",
        f"This indicates a plugin defect. {_SUPPORT}",
    ),
    Kind.UPSTREAM_TIMEOUT: (
        "The registry WHOIS or DNS server did not answer WhoisFreaks in time",
        "This is usually temporary. Try again later",
    ),
    Kind.RATE_LIMITED: (
        "The WhoisFreaks rate limit was reached",
        "The plugin waited for the rate limit window and retried. Reduce the number of concurrent workflows using "
        "this API key, or ask WhoisFreaks for a higher rate limit",
    ),
    Kind.SERVER_ERROR: (
        "WhoisFreaks returned a temporary server error",
        f"The plugin retried the request. Try again later. {_SUPPORT}",
    ),
    Kind.NETWORK: (
        "Could not connect to WhoisFreaks",
        "Check that the orchestrator can reach the WhoisFreaks host over HTTPS (TCP 443), including any proxy and "
        "DNS settings",
    ),
    Kind.TIMEOUT: (
        "WhoisFreaks did not respond in time",
        "Check network connectivity from the orchestrator and try again later",
    ),
    Kind.TLS: (
        "The TLS connection to WhoisFreaks could not be verified",
        "A TLS-inspecting proxy is usually the cause. Make the orchestrator trust the proxy certificate authority, "
        "or exempt the WhoisFreaks hosts from inspection",
    ),
    Kind.REDIRECT: (
        "WhoisFreaks answered with an unexpected redirect",
        "Redirects are not followed so that the API key is never sent to another host. Check for a proxy or "
        f"captive portal between the orchestrator and WhoisFreaks. {_SUPPORT}",
    ),
    Kind.INVALID_RESPONSE: (
        "WhoisFreaks returned a response that could not be read",
        f"Try again later. {_SUPPORT}",
    ),
    Kind.UNEXPECTED: (
        "WhoisFreaks returned an unexpected response",
        f"Try again later. {_SUPPORT}",
    ),
}

_KEY_IN_QUERY = re.compile(r"(?i)(api[_-]?key=)[^&\s\"']+")


def redact(text: object, secrets: tuple = ()) -> str:
    """Remove API keys from text that may be logged or shown to users."""
    result = str(text)
    for secret in secrets:
        if secret and len(secret) >= 4:
            result = result.replace(secret, "********")
    return _KEY_IN_QUERY.sub(r"\1********", result)


class WhoisFreaksError(PluginException):
    """A classified WhoisFreaks failure. kind drives retry and workflow behaviour."""

    def __init__(
        self,
        kind: str,
        operation: str,
        status_code: Optional[int] = None,
        api_message: str = "",
        detail: str = "",
        safe_to_retry_post: bool = False,
    ):
        self.kind = kind
        self.operation = operation
        self.status_code = status_code
        self.api_message = api_message
        self.safe_to_retry_post = safe_to_retry_post
        cause, assistance = _TEXT.get(kind, _TEXT[Kind.UNEXPECTED])
        cause = f"{operation}: {cause}"
        if detail:
            cause = f"{cause} ({detail})"
        if api_message:
            cause = f"{cause}. WhoisFreaks said: {api_message}"
        data = f"HTTP {status_code}" if status_code else ""
        super().__init__(cause=cause, assistance=assistance, data=data)


def _classify_400(text: str, service: str) -> str:
    if "apikey" in text or "api key" in text:
        return Kind.INVALID_CREDENTIALS
    if service == SERVICE_FEED and "date" in text and "available" in text:
        return Kind.DATE_NOT_AVAILABLE
    return Kind.BAD_REQUEST


_RULES_401 = (
    ("suspicious", Kind.ACCOUNT_BLOCKED),
    ("blocked", Kind.ACCOUNT_BLOCKED),
    ("domainer package", Kind.NOT_ENTITLED),
    ("database subscription", Kind.NOT_ENTITLED),
    ("download limit", Kind.PLAN_LIMIT),
    ("credit", Kind.NO_CREDITS),
    ("subscription plan", Kind.NO_CREDITS),
)


def _classify_401(text: str, service: str) -> str:
    if "api record not found" in text:
        return Kind.END_OF_DATA if service == SERVICE_FEED else Kind.INVALID_CREDENTIALS
    for needle, kind in _RULES_401:
        if needle in text:
            return kind
    return Kind.INVALID_CREDENTIALS


def _classify_403(text: str, service: str) -> str:
    if service == SERVICE_FEED or "subscription" in text or "access denied" in text:
        return Kind.NOT_ENTITLED
    return Kind.FORBIDDEN


def _classify_404(text: str, service: str) -> str:
    if "internal server error" in text or service == SERVICE_STATUS:
        return Kind.SERVER_ERROR
    if service == SERVICE_FEED:
        return Kind.DATE_NOT_AVAILABLE
    return Kind.NOT_FOUND


def _classify_413(text: str, service: str) -> str:
    if "list size" in text or "body size" in text:
        return Kind.LIST_TOO_LARGE
    if service == SERVICE_FEED or "access" in text:
        return Kind.NOT_ENTITLED
    return Kind.NO_CREDITS


def _classify_5xx(text: str, status_code: int) -> str:
    if status_code == 502 and "provide" in text:
        return Kind.BAD_REQUEST
    if status_code in (501, 505):
        return Kind.UNEXPECTED
    return Kind.SERVER_ERROR


_CLASSIFIERS = {400: _classify_400, 401: _classify_401, 403: _classify_403, 404: _classify_404, 413: _classify_413}

_FIXED = {
    402: Kind.NO_CREDITS,
    405: Kind.METHOD_NOT_ALLOWED,
    408: Kind.UPSTREAM_TIMEOUT,
    412: Kind.PLAN_LIMIT,
    423: Kind.RESERVED_IP,
    429: Kind.RATE_LIMITED,
    499: Kind.SERVER_ERROR,
}


def classify(status_code: int, message: str, service: str) -> str:
    """Map a WhoisFreaks HTTP status and error message to an error kind."""
    text = (message or "").lower()
    if status_code in _CLASSIFIERS:
        return _CLASSIFIERS[status_code](text, service)
    if status_code in _FIXED:
        return _FIXED[status_code]
    if 300 <= status_code < 400:
        return Kind.REDIRECT
    if status_code >= 500:
        return _classify_5xx(text, status_code)
    if 400 <= status_code < 500:
        return Kind.BAD_REQUEST
    return Kind.UNEXPECTED


def from_transport_exception(exception: requests.RequestException, operation: str, host: str) -> WhoisFreaksError:
    """Classify a requests exception without exposing its message, which can contain the request URL."""
    name = type(exception).__name__
    if isinstance(exception, requests.exceptions.SSLError):
        return WhoisFreaksError(Kind.TLS, operation, detail=f"{name} for {host}")
    if isinstance(exception, requests.exceptions.ConnectTimeout):
        return WhoisFreaksError(Kind.TIMEOUT, operation, detail=f"connecting to {host}", safe_to_retry_post=True)
    if isinstance(exception, requests.exceptions.Timeout):
        return WhoisFreaksError(Kind.TIMEOUT, operation, detail=f"waiting for {host}")
    if isinstance(exception, requests.exceptions.TooManyRedirects):
        return WhoisFreaksError(Kind.REDIRECT, operation, detail=host)
    # A connection that was never established cannot have delivered the request, so a POST is safe to retry
    never_sent = any(marker in repr(exception.args) for marker in ("NewConnectionError", "NameResolutionError"))
    return WhoisFreaksError(Kind.NETWORK, operation, detail=f"{name} for {host}", safe_to_retry_post=never_sent)
