import insightconnect_plugin_runtime
from .schema import MaxInput, MaxOutput, Input, Output, Component

# Custom imports below


class Max(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="max", description=Component.DESCRIPTION, input=MaxInput(), output=MaxOutput()
        )

    def run(self, params={}):
        numbers = params.get(Input.NUMBERS)
        return {"max": max(numbers)}
