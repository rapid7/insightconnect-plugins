import insightconnect_plugin_runtime
from .schema import ListMachinesInput, ListMachinesOutput, Component, Output


class ListMachines(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_machines",
            description=Component.DESCRIPTION,
            input=ListMachinesInput(),
            output=ListMachinesOutput(),
        )

    def run(self, params={}):
        endpoint = "machines/list"
        response = self.connection.api.send(endpoint)
        return {Output.MACHINES: response.get("machines", [])}
