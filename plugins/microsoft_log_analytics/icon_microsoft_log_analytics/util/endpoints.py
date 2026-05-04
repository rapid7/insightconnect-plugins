class Endpoint:
    # Base endpoints for Azure services
    RESOURCE_MANAGEMENT = "https://management.azure.com"
    RESOURCE_LOG_API = "https://api.loganalytics.io"

    # Authentication endpoints
    GET_AUTH_TOKEN = "https://login.microsoftonline.com/{}/oauth2/token"  # nosec

    # Workspace management endpoints
    GET_SHARED_KEY = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/sharedKeys?api-version={}"
    )
    GET_WORKSPACE_ID = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}?api-version={}"
    )

    # Log data endpoints
    SEND_LOG_DATA = "https://{}.ods.opinsights.azure.com/api/logs?api-version={}"
    GET_LOG_DATA = RESOURCE_LOG_API + "/{}/workspaces/{}/query"

    # Saved search endpoints
    GET_SAVED_SEARCH = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/savedSearches/{}?api-version={}"
    )
    DELETE_SAVED_SEARCH = GET_SAVED_SEARCH
    CREATE_OR_UPDATE_SAVED_SEARCH = GET_SAVED_SEARCH
    LIST_ALL_SEARCHES = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/savedSearches?api-version={}"
    )

    # API version constants
    API_VERSION_SAVED_SEARCH = "2025-07-01"
