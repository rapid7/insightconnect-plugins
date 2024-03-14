import insightconnect_plugin_runtime
from .schema import ListMachinesInput, ListMachinesOutput, Component


class ListMachines(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_machines",
            description=Component.DESCRIPTION,
            input=ListMachinesInput(),
            output=ListMachinesOutput(),
        )

    def run(self, params={}):
        endpoint = "/machines/list"
        response = self.connection.api.send(endpoint)
        result = {"machines": []}
        for machine in response.get("data", []):
            keys = machine.keys()
            cleaned_machine = {}
            for key in keys:
                if machine.get(key) is not None:
                    cleaned_machine[key] = machine.get(key)
            result["machines"].append(cleaned_machine)
        return result
