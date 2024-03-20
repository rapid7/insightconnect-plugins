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

    def run(self):
        endpoint = "machines/list"
        response = self.connection.api.send(endpoint)
        machines = response.get("machines")
        for machine in machines:
            resultserver_port = machine.get("resultserver_port")
            if resultserver_port:
                machine["resultserver_port"] = int(resultserver_port)
        return {Output.MACHINES: response.get("machines", [])}
