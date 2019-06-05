import komand
from .schema import ListMachinesInput, ListMachinesOutput
# Custom imports below
import json
import requests


class ListMachines(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_machines',
                description='Returns a list with details on the analysis machines available to Cuckoo',
                input=ListMachinesInput(),
                output=ListMachinesOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/machines/list"
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            result = {"machines": []}
            for machine in response['data']:
                keys = machine.keys()
                cleaned_machine = {}
                for key in keys:
                    if machine[key] is not None:
                        cleaned_machine[key] = machine[key]
                result['machines'].append(cleaned_machine)    
            return result

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return {"machines": [self.connection.test()]}

