import komand
from .schema import IsolateMachineInput, IsolateMachineOutput
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

        machine_id = params.get("machine_id")
        isolation_type = params.get("isolation_type")
        comment = params.get("comment")

        self.logger.info("Attempting to isolate machine id: " + machine_id)
        response = self.connection.isolate_machine(machine_id, isolation_type, comment)
        return {"machine_isolation_response": komand.helper.clean(response)}

    def test(self):
        self.connection.test()
        payload = self.connection.fake_isolation_response()
        return {"machine_isolation_response": payload}
