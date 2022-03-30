class Endpoint:
    RESOURCE_MANAGEMENT = "https://management.azure.com"
    RESOURCE_LOG_API = "https://api.loganalytics.io"

    GET_AUTH_TOKEN = "https://login.microsoftonline.com/{}/oauth2/token"  # nosec
    GET_SHARED_KEY = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/sharedKeys?api-version={}"
    )
    GET_WORKSPACE_ID = (
        RESOURCE_MANAGEMENT
        + "/subscriptions/{}/resourcegroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}?api-version={}"
    )

    SEND_LOG_DATA = "https://{}.ods.opinsights.azure.com/api/logs?api-version={}"
    GET_LOG_DATA = RESOURCE_LOG_API + "/{}/workspaces/{}/query"
