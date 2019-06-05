import komand
from .schema import GetMachineActionInput, GetMachineActionOutput
# Custom imports below


class GetMachineAction(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_machine_action',
                description='Retrieve details about an action taken on a machine',
                input=GetMachineActionInput(),
                output=GetMachineActionOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        action_id = params.get("action_id")

        self.logger.info("Attempting to get action for action ID: " + action_id)
        response = self.connection.get_machine_action(action_id)
        return {"machine_action_response": komand.helper.clean(response)}
