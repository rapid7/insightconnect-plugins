import komand
from .schema import GetMachineInformationInput, GetMachineInformationOutput, Input, Output, Component
# Custom imports below


class GetMachineInformation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_machine_information',
                description=Component.DESCRIPTION,
                input=GetMachineInformationInput(),
                output=GetMachineInformationOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = params.get(Input.MACHINE_ID)

        self.logger.info("Attempting to get information for machine ID: " + machine_id)
        response = self.connection.get_machine_information(machine_id)

        return {Output.MACHINE: komand.helper.clean(response)}

