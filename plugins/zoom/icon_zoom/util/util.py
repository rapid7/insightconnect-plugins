from insightconnect_plugin_runtime.exceptions import PluginException


DEFAULT_TASK_TYPE = "CMEF"


class UserType:
    @staticmethod
    def value_of(user_type: str) -> int:
        return {"Basic": 1, "Licensed": 2}.get(user_type)


oauth_retry_limit_exception = PluginException(
                cause="OAuth authentication retry limit was met.",
                assistance="Ensure your OAuth connection credentials are valid. "
                           "If running a large number of integrations with Zoom, consider "
                           "increasing the OAuth authentication retry limit to accommodate.",
)

authentication_error_exception = PluginException(
                cause="The OAuth token credentials or JWT token provided in the connection configuration is invalid.",
                assistance="Please verify the credentials are correct and try again."
)
