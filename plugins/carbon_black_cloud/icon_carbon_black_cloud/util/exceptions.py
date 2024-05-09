from insightconnect_plugin_runtime.exceptions import PluginException


class RateLimitException(PluginException):
    """Raise when we hit get rate limited so the task can delay running again."""


class HTTPErrorException(PluginException):
    def __init__(self, cause=None, assistance=None, data=None, preset=None, status_code=None):
        super().__init__(cause, assistance, data, preset)
        self.status_code = status_code
