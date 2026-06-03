TIMEOUT = 30
BOT_FRAMEWORK_SCOPE = "https://api.botframework.com/.default"
BOT_SERVICE_URL = "https://smba.trafficmanager.net/teams"

GRAPH_SCOPE_DEFAULT = "https://graph.microsoft.com/.default"

RESOURCE_URL = {
    "Normal": "https://graph.microsoft.com",
    "GCC": "https://graph.microsoft.com",
    "GCC High": "https://graph.microsoft.us",
    "DoD": "https://graph.microsoft.us",
}

AUTH_URL = {
    "Normal": "https://login.microsoftonline.com",
    "GCC": "https://login.microsoftonline.com",
    "GCC High": "https://login.microsoftonline.us",
    "DoD": "https://login.microsoftonline.us",
}

DEFAULT_MAX_RESULTS = 50

HTTP_ERROR_MAP = {
    400: {
        "cause": "Bad request",
        "assistance": "The request was malformed or contained invalid parameters. Please verify your inputs.",
    },
    401: {
        "cause": "Unauthorized",
        "assistance": "Authentication failed. Please verify your application credentials and permissions.",
    },
    403: {
        "cause": "Forbidden",
        "assistance": "The application does not have sufficient permissions for this operation. "
        "Verify the app registration has the required Microsoft Graph application permissions granted with admin consent.",
    },
    404: {
        "cause": "Resource not found",
        "assistance": "The requested resource was not found. Please verify the IDs or names provided are correct.",
    },
    429: {
        "cause": "Rate limit exceeded",
        "assistance": "Too many requests have been made. Please wait and try again later.",
    },
    500: {
        "cause": "Internal server error",
        "assistance": "Microsoft Graph encountered an internal error. Please try again later.",
    },
    503: {
        "cause": "Service unavailable",
        "assistance": "Microsoft Graph is temporarily unavailable. Please try again later.",
    },
}
