import insightconnect_plugin_runtime
from .schema import GetMissingSoftwareUpdatesInput, GetMissingSoftwareUpdatesOutput, Input, Output, Component
# Custom imports below


class GetMissingSoftwareUpdates(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_missing_software_updates',
                description=Component.DESCRIPTION,
                input=GetMissingSoftwareUpdatesInput(),
                output=GetMissingSoftwareUpdatesOutput())

    def run(self, params={}):
        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        self.logger.info("Attempting to find machine id: " + machine_id)
        return {
            Output.UPDATES: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_missing_software_updates(machine_id)
            ).get("value")
        }
