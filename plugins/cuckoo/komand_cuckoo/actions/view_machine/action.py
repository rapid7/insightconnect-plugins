import insightconnect_plugin_runtime
from .schema import ViewMachineInput, ViewMachineOutput, Input, Component


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
        return response
