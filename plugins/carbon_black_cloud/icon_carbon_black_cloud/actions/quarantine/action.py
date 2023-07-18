import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component

# Custom imports below
from icon_carbon_black_cloud.util.utils import Util


class Quarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine",
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agent = params.get(Input.AGENT, "")
        whitelist = params.get(Input.WHITELIST, [])
        quarantine_state = params.get(Input.QUARANTINE_STATE)
        # END INPUT BINDING - DO NOT REMOVE

        # This API returns 204 no content if successful, we have to assume the state was applied on a successful call
        response = self.connection.update_quarantine_state(agent, whitelist, quarantine_state)
        return {Output.QUARANTINED: response}
