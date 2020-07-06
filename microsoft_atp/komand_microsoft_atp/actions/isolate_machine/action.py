import komand
from .schema import IsolateMachineInput, IsolateMachineOutput, Input, Output
# Custom imports below


class IsolateMachine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='isolate_machine',
                description='Isolate a machine from the network, but keep the connection to Windows ATP open',
                input=IsolateMachineInput(),
                output=IsolateMachineOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = params.get(Input.MACHINE_ID)
        isolation_type = params.get(Input.ISOLATION_TYPE)
        comment = params.get(Input.COMMENT)

        self.logger.info("Attempting to isolate machine id: " + machine_id)
        response = self.connection.isolate_machine(machine_id, isolation_type, comment)
        return {Output.MACHINE_ISOLATION_RESPONSE: komand.helper.clean(response)}
