import insightconnect_plugin_runtime
from .schema import RunBotOnDemandInput, RunBotOnDemandOutput, Input, Output, Component

# Custom imports below


class RunBotOnDemand(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_bot_on_demand",
            description=Component.DESCRIPTION,
            input=RunBotOnDemandInput(),
            output=RunBotOnDemandOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.run_bot_on_demand(params.get(Input.BOTID))}
