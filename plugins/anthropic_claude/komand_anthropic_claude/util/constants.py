TIMEOUT = 120
API_VERSION = "2023-06-01"
BASE_URL = "https://api.anthropic.com/v1"
FALLBACK_MODEL = "claude-sonnet-4-6"

# HTTP status codes that indicate an invalid or unavailable model
MODEL_ERROR_INDICATORS = ["model:", "model is not", "not available", "deprecated", "does not exist"]

HTTP_ERROR_MAP = {
    400: {
        "cause": "The request was malformed or contained invalid parameters.",
        "assistance": "Verify the input parameters are correct and within allowed limits.",
    },
    401: {
        "cause": "Authentication failed. The API key is invalid or expired.",
        "assistance": "Verify the Anthropic API key is correct and active in your console.",
    },
    403: {
        "cause": "Access denied. The API key does not have permission for this operation.",
        "assistance": "Check that your API key has the required permissions in the Anthropic console.",
    },
    404: {
        "cause": "The requested resource was not found.",
        "assistance": "Verify the endpoint and model name are correct.",
    },
    429: {
        "cause": "Rate limit exceeded.",
        "assistance": "Too many requests have been sent. Wait and retry, or reduce request frequency.",
    },
    500: {
        "cause": "Anthropic API internal server error.",
        "assistance": "This is a temporary issue on Anthropic's side. Retry the request after a brief wait.",
    },
    503: {
        "cause": "Anthropic API is temporarily unavailable.",
        "assistance": "The service is overloaded or under maintenance. Retry after a brief wait.",
    },
}
