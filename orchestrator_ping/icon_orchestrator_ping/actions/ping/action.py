import komand
from .schema import PingInput, PingOutput, Input, Output, Component

# Custom imports below


class Ping(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ping",
            description=Component.DESCRIPTION,
            input=PingInput(),
            output=PingOutput(),
        )

    def run(self, params={}):
        input_message = params[Input.MESSAGE]
        return {Output.MESSAGE: input_message}
