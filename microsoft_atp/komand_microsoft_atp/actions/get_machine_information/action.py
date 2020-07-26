import insightconnect_plugin_runtime
from .schema import GetMachineInformationInput, GetMachineInformationOutput, Input, Output, Component
# Custom imports below


class GetMachineInformation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_machine_information',
                description=Component.DESCRIPTION,
                input=GetMachineInformationInput(),
                output=GetMachineInformationOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        self.logger.info(f"Attempting to get information for machine ID: {machine_id}")

        return {
            Output.MACHINE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_machine_information(machine_id)
            )
        }
