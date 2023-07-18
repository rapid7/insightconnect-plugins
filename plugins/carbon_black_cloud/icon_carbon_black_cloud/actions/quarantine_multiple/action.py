import insightconnect_plugin_runtime
from .schema import QuarantineMultipleInput, QuarantineMultipleOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class QuarantineMultiple(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_multiple",
            description=Component.DESCRIPTION,
            input=QuarantineMultipleInput(),
            output=QuarantineMultipleOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agents = params.get(Input.AGENTS, [])
        whitelist = params.get(Input.WHITELIST, [])
        quarantine_state = params.get(Input.QUARANTINE_STATE)
        # END INPUT BINDING - DO NOT REMOVE

        completed = []
        failed = []
        for agent in agents:
            try:
                self.connection.update_quarantine_state(agent, whitelist, quarantine_state)
                completed.append(agent)
            except PluginException as error:
                failed.append({"input_key": agent, "error": str(error)})
        return {Output.COMPLETED: completed, Output.FAILED: failed}
