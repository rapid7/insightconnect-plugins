import insightconnect_plugin_runtime
from .schema import UnisolateMachineInput, UnisolateMachineOutput
# Custom imports below


class UnisolateMachine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unisolate_machine',
                description='Restore network connectivity to a machine',
                input=UnisolateMachineInput(),
                output=UnisolateMachineOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = params.get("machine_id")
        comment = params.get("comment")

        self.logger.info("Attempting to unisolate machine id: " + machine_id)
        response = self.connection.unisolate_machine(machine_id, comment)
        return {"machine_isolation_response": insightconnect_plugin_runtime.helper.clean(response)}

    def test(self):
        self.connection.test()
        payload = self.connection.fake_isolation_response()
        return {"machine_isolation_response": payload}
