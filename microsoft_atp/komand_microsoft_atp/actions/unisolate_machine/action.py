import insightconnect_plugin_runtime
from .schema import UnisolateMachineInput, UnisolateMachineOutput, Input, Output, Component
# Custom imports below


class UnisolateMachine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unisolate_machine',
                description=Component.DESCRIPTION,
                input=UnisolateMachineInput(),
                output=UnisolateMachineOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        comment = params.get(Input.COMMENT)

        self.logger.info("Attempting to unisolate machine id: " + machine_id)
        return {
            Output.MACHINE_ISOLATION_RESPONSE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.unisolate_machine(machine_id, comment)
            )
        }
