import insightconnect_plugin_runtime
from .schema import IsolateMachineInput, IsolateMachineOutput, Input, Output, Component
# Custom imports below


class IsolateMachine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='isolate_machine',
                description=Component.DESCRIPTION,
                input=IsolateMachineInput(),
                output=IsolateMachineOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        isolation_type = params.get(Input.ISOLATION_TYPE)
        comment = params.get(Input.COMMENT)

        self.logger.info("Attempting to isolate machine id: " + machine_id)
        return {
            Output.MACHINE_ISOLATION_RESPONSE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.isolate_machine(machine_id, isolation_type, comment)
            )
        }
