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
        interval = params.get(Input.INTERVAL)

        if quarantine_state:
            successful_quarantine, unsuccessful_quarantine = self.connection.api.quarantine_list(
                agent_id_list=agent_array, advertisement_period=interval
            )
        else:
            successful_quarantine, unsuccessful_quarantine = self.connection.api.unquarantine_list(
                agent_id_list=agent_array
            )

        # Establish true or false for if there are any unsuccessful quarantines
        all_operations_succeeded = not unsuccessful_quarantine

        return {
            Output.SUCCESS: successful_quarantine,
            Output.FAILURE: unsuccessful_quarantine,
            Output.ALL_OPERATIONS_SUCCEEDED: all_operations_succeeded,
        }
