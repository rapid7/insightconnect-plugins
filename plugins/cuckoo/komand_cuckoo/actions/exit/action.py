import insightconnect_plugin_runtime
from .schema import ExitInput, ExitOutput, Component, Output

# Custom imports below


class Exit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="exit",
            description=Component.DESCRIPTION,
            input=ExitInput(),
            output=ExitOutput(),
        )

    def run(self, params={}):
        endpoint = "exit"
        response = self.connection.api.send(endpoint)
        message = response.get("message", "")
        return {Output.MESSAGE: message}
