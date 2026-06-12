TIMEOUT = 60  # HTTP request timeout
DEFAULT_MONITORING_TIMEOUT = 120
DEFAULT_POLLING_INTERVAL = 10
API_VERSION = "2.1"

INTENT_CONTAIN = "contain"
INTENT_UNCONTAIN = "uncontain"
INTENT_STATUS = "status"
INTENT_INFO = "info"

STATUS_CONNECTED = "connected"
STATUS_DISCONNECTED = "disconnected"

RESULT_SUCCESS = "success"
RESULT_ALREADY_ACTIONED = "already_actioned"
RESULT_TIMEOUT = "timeout"
RESULT_ERROR = "error"

# Minimum confidence score (0–1) an agent must reach to be considered a valid match during scoring
CONFIDENCE_THRESHOLD = 0.7

HTTP_ERROR_MAP = {
    400: {"cause": "Bad request sent to SentinelOne API.", "assistance": "Verify the input parameters."},
    401: {
        "cause": "Authentication failed.",
        "assistance": "The API key may be invalid or expired. Verify your credentials.",
    },
    403: {"cause": "Forbidden.", "assistance": "The API key does not have sufficient permissions."},
    404: {"cause": "Resource not found.", "assistance": "The requested endpoint does not exist."},
    429: {"cause": "Rate limit exceeded.", "assistance": "Too many requests. Try again later."},
    500: {
        "cause": "SentinelOne server error.",
        "assistance": "An internal error occurred on the SentinelOne side.",
    },
    503: {
        "cause": "SentinelOne service unavailable.",
        "assistance": "The service is temporarily unavailable. Try again later.",
    },
}
