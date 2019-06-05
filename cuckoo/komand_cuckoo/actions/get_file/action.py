import komand
from .schema import GetFileInput, GetFileOutput
# Custom imports below
import json
import requests
import base64


class GetFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file',
                description='Returns the binary content of the file matching the specified SHA256 hash',
                input=GetFileInput(),
                output=GetFileOutput())

    def run(self, params={}):
        server = self.connection.server
        sha256 = params.get('sha256', '')
        endpoint = server + "/files/get/" + sha256
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            if r.headers['Content-Type'].startswith("application/octet-stream"):
                content = r.content  
                return {'contents': base64.b64encode(content).decode('UTF-8')}
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['contents'] = ''
        return out
