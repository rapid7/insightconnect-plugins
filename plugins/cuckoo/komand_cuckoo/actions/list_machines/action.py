import insightconnect_plugin_runtime
from .schema import ListMachinesInput, ListMachinesOutput, Input, Output

# Custom imports below
import requests


class ListMachines(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_machines",
            description="Returns a list with details on the analysis machines available to Cuckoo",
            input=ListMachinesInput(),
            output=ListMachinesOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        endpoint = f"{server}/machines/list"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            result = {"machines": []}
            for machine in response.get("data", []):
                keys = machine.keys()
                cleaned_machine = {}
                for key in keys:
                    if machine.get(key) is not None:
                        cleaned_machine[key] = machine.get(key)
                result["machines"].append(cleaned_machine)
            return result

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
