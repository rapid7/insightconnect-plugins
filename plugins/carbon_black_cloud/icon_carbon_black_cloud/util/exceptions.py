from insightconnect_plugin_runtime.exceptions import PluginException


class RateLimitException(PluginException):
    def __init__(self, cause=None, assistance=None, data=None, preset=None):
        super().__init__(cause, assistance, data, preset)
