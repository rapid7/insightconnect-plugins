DEFAULT_TIMEOUT = 10
ENCODE_TYPE = "utf-8"

OBSERVATION_TYPES = [
    "OBSERVATION_TYPE_UNKNOWN",
    "CB_ANALYTICS",
    "INDICATOR_OF_ATTACK",
    "TAMPER",
    "TAU_INTELLIGENCE",
    "USB_DEVICE_CONTROL",
    "WATCHLIST",
    "BLOCKED_HASH",
    "INTRUSION_DETECTION_SYSTEM",
    "CONTAINER_RUNTIME",
    "HOST_BASED_FIREWALL",
    "NETWORK_TRAFFIC_ANALYSIS",
    "CONTEXTUAL_ACTIVITY",
]

ERROR_HANDLING = {
    400: {"cause": "400 Bad Request", "assistance": "Verify that your request adheres to API documentation."},
    401: {
        "cause": "Authentication Error. Please verify connection details are correct.",
        "assistance": "Please verify that your Secret Key and API ID values in the plugin connection are correct.",
    },
    403: {
        "cause": "The specified object cannot be accessed or changed. If it has a Custom access level, check it has been assigned the correct RBAC permissions. "
        "If it is an API, SIEM or LIVE_RESPONSE type key, verify it is the right key type for the "
        "API in use.",
    },
    404: {
        "cause": "The requested URL can not be found. Ensure your organization key and URL in your connection is correct.",
        "assistance": "Verify that your request contains objects that haven't been deleted. Verify that the "
        "organization key in the URL is correct.",
    },
    409: {
        "cause": "Either the name you chose already exists, or there is an unacceptable character used.",
        "assistance": "Change any spaces in the name to underscores. Look through your list of API Keys and see if "
        "there is an existing key with the same name.",
    },
}
