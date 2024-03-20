import insightconnect_plugin_runtime
from .schema import ViewMachineInput, ViewMachineOutput, Input, Component, Output


class ViewMachine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="view_machine",
            description=Component.DESCRIPTION,
            input=ViewMachineInput(),
            output=ViewMachineOutput(),
        )

    def run(self, params={}):
        machine_name = params.get(Input.MACHINE_NAME, "")
        endpoint = f"machines/view/{machine_name}"
        response = self.connection.api.send(endpoint)
        machine = response.get("machine", {})
        resultserver_port = machine.get("resultserver_port")
        if resultserver_port:
            machine["resultserver_port"] = int(resultserver_port)
        return {Output.MACHINE: machine}
