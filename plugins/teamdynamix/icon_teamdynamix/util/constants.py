"""Constants for the TeamDynamix plugin."""

# Request defaults
TIMEOUT = 30
DEFAULT_MAX_RESULTS = 25

# API path prefix
API_BASE_PATH = "/TDWebApi/api"
AUTH_ADMIN_ENDPOINT = "/TDWebApi/api/auth/loginadmin"
AUTH_USER_ENDPOINT = "/TDWebApi/api/auth/login"

# HTTP error map — maps status codes to user-friendly cause/assistance pairs
HTTP_ERROR_MAP = {
    400: {
        "cause": "TeamDynamix rejected the request due to invalid input.",
        "assistance": "Verify all required fields are provided and have valid values. "
        "Check that IDs (TypeID, StatusID, PriorityID, AccountID) exist in your TeamDynamix instance.",
    },
    401: {
        "cause": "Authentication failed or token expired.",
        "assistance": "Verify your BEID and Web Services Key are correct and the admin service account is active.",
    },
    403: {
        "cause": "Access denied by TeamDynamix.",
        "assistance": "The admin service account does not have permission to perform this operation. "
        "Verify the account has appropriate permissions in TDAdmin.",
    },
    404: {
        "cause": "The requested resource was not found in TeamDynamix.",
        "assistance": "Verify the ticket ID and application ID are correct and the resource exists.",
    },
    429: {
        "cause": "TeamDynamix API rate limit exceeded.",
        "assistance": "Too many requests have been made. Wait and retry. "
        "TeamDynamix limits most endpoints to 60 calls per IP per 60 seconds.",
    },
    500: {
        "cause": "TeamDynamix encountered an internal server error.",
        "assistance": "This is a server-side issue. Retry the request or contact TeamDynamix support if it persists.",
    },
    503: {
        "cause": "TeamDynamix service is temporarily unavailable.",
        "assistance": "The service may be undergoing maintenance. Retry after a short delay.",
    },
}
