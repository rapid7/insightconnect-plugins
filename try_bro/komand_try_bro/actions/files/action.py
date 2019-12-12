import komand
from .schema import FilesInput, FilesOutput
from komand.exceptions import PluginException
# Custom imports below
import json
import requests


class Files(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='files',
                description='Get logs by ID',
                input=FilesInput(),
                output=FilesOutput())

    def run(self, params={}):
        server = self.connection.server
        job = params.get('job')
        files={}
        res = requests.get(server + '/files/' + job)
        log = res.json()
        if len(log['files']) == 0:
          raise PluginException(cause='Run: Job ID has no data')
        for i in log['files'].keys():
          files[i] = log['files'][i].split('\n')
        return { 'files': files }

    def test(self):
        server = self.connection.server
        res = requests.get(server)
        if res.status_code != 200:
          raise PluginException(cause='Test: Unsuccessful HTTP status code returned')
        return {}
