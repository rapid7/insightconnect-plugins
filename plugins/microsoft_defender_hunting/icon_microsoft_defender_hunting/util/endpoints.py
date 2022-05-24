class Endpoint:
    RESOURCE_SECURITY = "https://api.security.microsoft.com"

    GET_AUTH_TOKEN = "https://login.microsoftonline.com/{}/oauth2/token"  # nosec

    ADVANCED_HUNTING = RESOURCE_SECURITY + "/api/advancedhunting/run"
