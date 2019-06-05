import komand
from .schema import GetPcapInput, GetPcapOutput
# Custom imports below
import json
import requests
import base64


class GetPcap(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_pcap',
                description='Returns the content of the PCAP associated with the given task',
                input=GetPcapInput(),
                output=GetPcapOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/pcap/get/" + str(task_id)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            ctype = r.headers['Content-Type']
            if ctype.startswith("application/x-tar") or ctype.startswith("application/octet-stream") or ctype.startswith("application/json") or ctype.startswith("application/vnd.tcpdump.pcap"):
                content = r.content
                return {'contents': base64.b64encode(content).decode('UTF-8')}
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['contents'] = ''
        return out
