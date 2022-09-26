import insightconnect_plugin_runtime

from .schema import AddComputerToGroupInput, AddComputerToGroupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddComputerToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_computer_to_group",
            description=Component.DESCRIPTION,
            input=AddComputerToGroupInput(),
            output=AddComputerToGroupOutput(),
        )

    def run(self, params={}):
        computer_group_id = params.get(Input.ID)
        computer_ids = params.get(Input.COMPUTER_IDS)
        response = self.connection.client.add_computer_to_group(computer_group_id, computer_ids)
        return {Output.STATUS: response.status_code}
