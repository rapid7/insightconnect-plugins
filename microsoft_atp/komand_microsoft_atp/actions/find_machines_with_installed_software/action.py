import insightconnect_plugin_runtime
from .schema import FindMachinesWithInstalledSoftwareInput, FindMachinesWithInstalledSoftwareOutput, Input, Output, Component
# Custom imports below


class FindMachinesWithInstalledSoftware(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_machines_with_installed_software',
                description=Component.DESCRIPTION,
                input=FindMachinesWithInstalledSoftwareInput(),
                output=FindMachinesWithInstalledSoftwareOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        return {
            Output.MACHINES: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.find_machines(params.get(Input.SOFTWARE)).get("value")
            )
        }
