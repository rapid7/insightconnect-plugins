import insightconnect_plugin_runtime
from .schema import Input, Output, Component, GetMachineVulnerabilitiesInput, GetMachineVulnerabilitiesOutput
# Custom imports below


class GetMachineVulnerabilities(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_machine_vulnerabilities',
            description=Component.DESCRIPTION,
            input=GetMachineVulnerabilitiesInput(),
            output=GetMachineVulnerabilitiesOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        self.logger.info(f"Attempting to get vulnerabilities for machine ID: {machine_id}")

        return {
            Output.VULNERABILITIES: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_machine_vulnerabilities(machine_id).get("value")
            )
        }
