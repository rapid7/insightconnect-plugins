import komand
from .schema import FilenameLookupInput, FilenameLookupOutput
# Custom imports below
from komand.exceptions import ConnectionTestException
import requests


class FilenameLookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='filename_lookup',
                description='Search for a Windows filename by name to obtain process behavioral analytics',
                input=FilenameLookupInput(),
                output=FilenameLookupOutput())

    def run(self, params={}):
        ret = {}
        server = self.connection.server
        token = self.connection.token
        url = server + '/v1/private/insights/%s' % params.get('filename')
        headers = {'X-Api-Key': token}
        response = requests.get(url, headers=headers)

        if response.status_code == 403:
            raise Exception("Invalid API key provided. Verify your API key configured in your connection is correct.")
        elif response.status_code == 404:
            raise Exception("Unable to reach instance at {url}. Verify the server at the URL configured in your plugin connection is correct.")
        elif response.status_code == 429:
            raise Exception("The account configured in your plugin connection is currently rate-limited. Adjust the time between requests in the plugin action configuration if possible or consider adding a Sleep plugin step between attempts.")
        elif response.status_code == 503:
            raise Exception("Server error occurred. Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.")
        elif response.status_code != 200:
            raise Exception(f"Unhandled error occurred: {response.content}")

        ret = response.json()

        ret['host_prev'] = float(ret['host_prev']) if 'host_prev' in ret else 0
        ret['eps'] = float(ret['eps']) if 'eps' in ret else 0

        conversion = [
            ['paths', 'path'],
            ['parents', 'parent'],
            ['children', 'child'],
            ['grandparents', 'grandparent'],
            ['hashes', 'hash'],
            ['network', 'port'],
        ]
        for item in conversion:
            if item[0] in ret:
                self.convert_array(ret[item[0]], item[1])
            else:
                ret[item[0]] = []

        if 'message' in ret and 'description' not in ret:
            ret['description'] = ret['message']
            del ret['message']

        return ret

    def convert_array(self, arr, name):
        for idx, val in enumerate(arr):
            arr[idx] = {name: val[0], 'score': float(val[1])}
