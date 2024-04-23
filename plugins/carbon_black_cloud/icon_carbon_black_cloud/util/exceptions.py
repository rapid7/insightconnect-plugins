from insightconnect_plugin_runtime.exceptions import PluginException


class RateLimitException(PluginException):
    """Raise when we hit get rate limited so the task can delay running again."""
