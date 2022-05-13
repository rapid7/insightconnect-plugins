class Endpoint:
    RESOURCE_SECURITY = "https://api.security.microsoft.com"

    GET_AUTH_TOKEN = "https://login.microsoftonline.com/{}/oauth2/token"  # nosec

    LIST_INCIDENTS = RESOURCE_SECURITY + "/api/incidents"
    GET_INCIDENT = LIST_INCIDENTS + "/{}"
    UPDATE_INCIDENT = GET_INCIDENT

    ADVANCED_HUNTING = RESOURCE_SECURITY + "/api/advancedhunting/run"
