import komand
from .schema import ViewMachineInput, ViewMachineOutput
# Custom imports below
import json
import requests


class ViewMachine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='view_machine',
                description='Returns details on the analysis machine associated with the given name',
                input=ViewMachineInput(),
                output=ViewMachineOutput())

    def run(self, params={}):
        server = self.connection.server
        machine_name = params.get('machine_name', '')
        endpoint = server + "/machines/view/" + machine_name

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            """
            result = {"machine": {}}
            keys = response['machine'].keys()
            for key in keys:
                if response['machine'][key] is not None:
                    result['machine'][key] = response['machine'][key]
            """
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['machine'] = {'message':'Test passed'}
        return out
