import insightconnect_plugin_runtime
from .schema import GetInstalledSoftwareInput, GetInstalledSoftwareOutput, Input, Output, Component

# Custom imports below


class GetInstalledSoftware(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_installed_software",
            description=Component.DESCRIPTION,
            input=GetInstalledSoftwareInput(),
            output=GetInstalledSoftwareOutput(),
        )

    def run(self, params={}):
        self.logger.info("Running...")
        return {
            Output.SOFTWARE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_installed_software(
                    self.connection.client.find_machine_id(params.get(Input.MACHINE))
                ).get("value")
            )
        }
