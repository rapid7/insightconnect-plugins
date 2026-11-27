TIMEOUT = 60

AUTH_ENDPOINT = "/auth/token"
TICKETS_ENDPOINT = "/api/tickets"
ACTIONS_ENDPOINT = "/api/Actions"
ATTACHMENT_ENDPOINT = "/api/Attachment"

HTTP_ERROR_MAP = {
    400: {
        "cause": "Bad request sent to the Halo ITSM API.",
        "assistance": "Check your input parameters and try again.",
    },
    401: {
        "cause": "Invalid credentials provided.",
        "assistance": "Verify that the Client ID and Client Secret are correct and have not expired.",
    },
    403: {
        "cause": "Permission denied.",
        "assistance": "Ensure the API application has the required permissions and scopes.",
    },
    404: {
        "cause": "Resource not found.",
        "assistance": "Verify the resource exists and the identifier is correct.",
    },
    429: {
        "cause": "API rate limit exceeded.",
        "assistance": "Reduce request frequency or try again later.",
    },
    500: {
        "cause": "Internal server error from Halo ITSM.",
        "assistance": "Try again later. If the issue persists, contact Halo ITSM support.",
    },
    503: {
        "cause": "Halo ITSM service unavailable.",
        "assistance": "The service is temporarily unavailable. Try again later.",
    },
}
