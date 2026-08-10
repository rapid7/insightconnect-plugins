# Base URL for every IPGeolocation.io v3 endpoint.
BASE_URL = "https://api.ipgeolocation.io/v3"

# Endpoint paths, relative to BASE_URL.
ENDPOINT_IPGEO = "/ipgeo"
ENDPOINT_IPGEO_BULK = "/ipgeo-bulk"
ENDPOINT_SECURITY = "/security"
ENDPOINT_SECURITY_BULK = "/security-bulk"
ENDPOINT_ASN = "/asn"
ENDPOINT_ABUSE = "/abuse"

# The bulk endpoints accept at most 50,000 entries per request.
MAX_BULK_ENTRIES = 50000

# HTTP behaviour.
DEFAULT_TIMEOUT = 120
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 2
MAX_RETRY_AFTER_SECONDS = 60
RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

# Response headers worth surfacing in the plugin log.
HEADER_CREDITS_CHARGED = "X-Credits-Charged"
HEADER_SUCCESSFUL_RECORDS = "X-Successful-Record"

# Values accepted by the include parameter on /v3/ipgeo and /v3/ipgeo-bulk.
# All of them require a paid subscription. Unknown values are ignored silently
# by the API, so the plugin validates them rather than letting a typo look like
# a plan restriction.
INCLUDE_MODULES_IPGEO = (
    "security",
    "abuse",
    "hostname",
    "liveHostname",
    "hostnameFallbackLive",
    "geo_accuracy",
    "dma_code",
    "user_agent",
    "*",
)

# Values accepted by the include parameter on /v3/asn.
INCLUDE_MODULES_ASN = (
    "peers",
    "upstreams",
    "downstreams",
    "routes",
    "whois_response",
)

# Languages accepted by the lang query parameter. Anything other than English
# requires a paid subscription.
SUPPORTED_LANGUAGES = (
    "en",
    "de",
    "ru",
    "ja",
    "fr",
    "cn",
    "es",
    "cs",
    "it",
    "ko",
    "fa",
    "pt",
    "ar",
)

# Cause text per HTTP status, taken from the IPGeolocation.io error tables.
STATUS_CAUSES: dict[int, str] = {
    400: "IPGeolocation.io rejected the request as malformed.",
    401: "IPGeolocation.io rejected the API key or the requested data.",
    403: "IPGeolocation.io refused access to this resource.",
    404: "IPGeolocation.io has no record for the requested IP, domain, or ASN.",
    405: "The endpoint was called with an unsupported HTTP method.",
    413: "The request payload was larger than IPGeolocation.io accepts.",
    415: "IPGeolocation.io rejected the content type of the request.",
    423: "The requested address is a bogon or private address and cannot be looked up.",
    429: "The IPGeolocation.io usage limit for this subscription has been reached.",
    499: "IPGeolocation.io closed the request before it completed.",
}

# Assistance text per HTTP status.
STATUS_ASSISTANCE: dict[int, str] = {
    400: (
        "Verify that the IP address, domain, or ASN is valid, that a bulk request contains between "
        "1 and 50,000 entries, and that the selected language is supported."
    ),
    401: (
        "Verify the API key is correct and the subscription is active. Security, ASN Lookup, abuse, hostname, "
        "geo accuracy, DMA code, user agent, bulk, domain lookups, and non-English responses all "
        "require a paid subscription."
    ),
    403: "Verify that the subscription includes this endpoint and that the account is in good standing.",
    404: "Verify the IP address, domain, or ASN. It may not exist in the IPGeolocation.io database.",
    405: "This is a plugin defect. Report it to the plugin maintainer.",
    413: "Send fewer entries per bulk request.",
    415: "This is a plugin defect. Report it to the plugin maintainer.",
    423: (
        "Provide a public, routable address. Private ranges such as 10.0.0.0/8, 172.16.0.0/12, and "
        "192.168.0.0/16, along with loopback and reserved ranges, cannot be looked up."
    ),
    429: (
        "Wait for the quota to reset, or upgrade the IPGeolocation.io subscription."
    ),
    499: "Retry the action. If it keeps happening, reduce the size of the request.",
}

DEFAULT_CAUSE = "IPGeolocation.io returned an unexpected response."
DEFAULT_ASSISTANCE = "Verify the connection and inputs, then retry the action."
