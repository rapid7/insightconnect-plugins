import insightconnect_plugin_runtime
from .schema import QuarantineMultipleInput, QuarantineMultipleOutput, Input, Output, Component
import logging
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
        successful_quarantine, unsuccessful_quarantine = self.connection.api.quarantine_list(
            agent_hostnames=agent_array, advertisement_period=interval, quarantine=quarantine_state
        )
        logging.info(f"FINITO? {successful_quarantine} {unsuccessful_quarantine}")
        return {
            Output.COMPLETED: successful_quarantine,
            Output.FAILED: unsuccessful_quarantine,
        }
