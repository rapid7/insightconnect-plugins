import komand
from .schema import SubmitInput, SubmitOutput
# Custom imports below
import base64
import requests


class Submit(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit',
                description='Submit file for analysis',
                input=SubmitInput(),
                output=SubmitOutput())

    def run(self, params={}):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret

        output = {}
        data = {}
        if params.get('customcmdline'):
            data['customcmdline'] = params['customcmdline']

        if params.get('promptfill_password'):
            customcmdline = data.get('customcmdline') or ''
            customcmdline += '/VX:promptfill ' + params['promptfill_password']
            data['customcmdline'] = customcmdline 
      
        if params.get('scriptlogging'):
            data['scriptlogging'] = 1 

        if params.get('hybridanalysis'):
            data['hybridanalysis'] = 1 

        if params.get('experimentalantievasion'):
            data['experimentalantievasion'] = 1 

        if params.get('filename'):
            data['submitname'] = params['filename']

        data['environmentId'] = params.get('env_id') or 100

        url = server + '/submit'
        user_agent = {'User-Agent': 'VxStream Sandbox'}
        _file = base64.b64decode(params['file'])
        files = {"file": _file}

        self.logger.info("Posting request %s with %s", url, data)

        response = requests.post(url, data=data, headers=user_agent, files=files, verify=False, auth=requests.auth.HTTPBasicAuth(api_key, secret))

        if response.status_code == 200:
            data = response.json()
            self.logger.info("got response: %s", data)
            output['response_code'] = data['response_code']
            if data['response_code'] == 0:
                output['hash'] = data['response']['sha256']
                output['submission_url'] = self.connection.base_url() + '/sample/' + output['hash']
            else:
                output['error'] = data['response']['error']
        
        return output

    def test(self):
        return {
            'response_code': 200
        } 
