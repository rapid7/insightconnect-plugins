import insightconnect_plugin_runtime
from .schema import QuarantineMultipleInput, QuarantineMultipleOutput, Input, Output, Component
# Custom imports below


class QuarantineMultiple(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine_multiple',
                description=Component.DESCRIPTION,
                input=QuarantineMultipleInput(),
                output=QuarantineMultipleOutput())

    def run(self, params={}):
        agent_array = params.get(Input.AGENT_ARRAY)
        quarantine = params.get(Input.QUARANTINE_STATE)

        agent_array = self.connection.api.convert_hostnames_to_id(agent_array)
        success = None

        for agent in agent_array:
            if quarantine:
                success = self.connection.api.quarantine(agent)
            else:
                success = self.connection.api.unquarantine(agent)
        return {Output.SUCCESS: success}
