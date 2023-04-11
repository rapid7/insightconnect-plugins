import insightconnect_plugin_runtime
from .schema import QuarantineMultipleInput, QuarantineMultipleOutput, Input, Output, Component

# Custom imports below


class QuarantineMultiple(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_multiple",
            description=Component.DESCRIPTION,
            input=QuarantineMultipleInput(),
            output=QuarantineMultipleOutput(),
        )

    def run(self, params={}):
        agent_array = params.get(Input.AGENT_ARRAY)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        agent_array = self.connection.api.convert_hostnames_to_id(agent_array)

        if quarantine_state:
            successful_quarantine, unsuccessful_quarantine = self.connection.api.quarantine_list(
                agent_id_list=agent_array
            )
        else:
            successful_quarantine, unsuccessful_quarantine = self.connection.api.unquarantine_list(
                agent_id_list=agent_array
            )

        success = bool(successful_quarantine)

        return {
            Output.SUCCESS: success,
            Output.SUCCESSFUL_QUARANTINE: successful_quarantine,
            Output.UNSUCCESSFUL_QUARANTINE: unsuccessful_quarantine,
        }
