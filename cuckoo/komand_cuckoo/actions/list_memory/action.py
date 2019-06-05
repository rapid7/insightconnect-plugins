import komand
from .schema import ListMemoryInput, ListMemoryOutput
# Custom imports below
import json
import requests


class ListMemory(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_memory',
                description='Returns a list of memory dump files or one memory dump file associated with the specified task ID',
                input=ListMemoryInput(),
                output=ListMemoryOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/memory/list/%d" % (task_id)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()            
            return response
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['dump_files'] = ['Test passed']
        return out