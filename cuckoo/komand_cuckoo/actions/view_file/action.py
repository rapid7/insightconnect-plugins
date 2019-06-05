import komand
from .schema import ViewFileInput, ViewFileOutput
# Custom imports below
import json
import requests


class ViewFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='view_file',
                description='Returns details on the file matching either the specified MD5 hash, SHA256 hash or ID',
                input=ViewFileInput(),
                output=ViewFileOutput())

    def run(self, params={}):
        server = self.connection.server

        if params.get('md5', ''):
            md5 = params.get('md5', '')
            endpoint = server + "/files/view/md5/" + str(md5)
        elif params.get('sha256', ''):
            sha256 = params.get('sha256', '')
            endpoint = server + "/files/view/sha256/" + str(sha256)
        elif params.get('id', ''):
            task_id = params.get('id', '')
            endpoint = server + "/files/view/id/" + str(task_id)

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            """
            result = {'sample': {}}

            keys = response['sample'].keys()
            for key in keys:
                if response['sample'][key] is not None:
                    result['sample'][key] = response['sample'][key]
            """
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['error'] = False
        out['data'] = {'message': 'Test passed'}
        return out
