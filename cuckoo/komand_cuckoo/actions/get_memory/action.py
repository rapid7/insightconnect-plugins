import komand
from .schema import GetMemoryInput, GetMemoryOutput
# Custom imports below
import json
import requests
import base64


class GetMemory(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_memory',
                description='Returns one memory dump file associated with the specified task ID',
                input=GetMemoryInput(),
                output=GetMemoryOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        pid = params.get('pid', '')
        endpoint = server + "/memory/get/%d/%s" % (task_id, pid)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            if r.headers['Content-Type'].startswith("application/octet-stream"):
                content = r.content
                return {'contents': base64.b64encode(content).decode('UTF-8')}
            else:
                return r.json()
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['contents'] = ''
        return out
