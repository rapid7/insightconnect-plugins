from insightconnect_plugin_runtime.exceptions import PluginException


class GNRequestFailure(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message["message"]

        raise PluginException(
            cause="Received HTTP %d status code from GreyNoise. Verify your input and try again." % self.status_code,
            assistance="If the issue persists please contact GreyNoise support.",
            data=f"{self.status_code}, {self.message}",
        )


class GNValueError(Exception):
    def __init__(self, message):
        self.message = message

        raise PluginException(
            cause="Received HTTP 404 status code from GreyNoise." "Input provided was not found, please try another.",
            assistance="If the issue persists please contact GreyNoise support.",
            data=f"{self.message}",
        )
