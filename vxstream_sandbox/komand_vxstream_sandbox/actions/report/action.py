import komand
from .schema import ReportInput, ReportOutput
# Custom imports below
import requests
import urllib.parse


class Report(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='report',
                description='Retrieve report by providing SHA256 hash',
                input=ReportInput(),
                output=ReportOutput())

    def run(self, params={}):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        state_url = server + "/state/%s" % urllib.parse.quote(params.get('hash'))
        report_url = server + "/result/%s" % urllib.parse.quote(params.get('hash'))
        user_agent = {'User-Agent': 'VxStream Sandbox'}
        env_id = params.get('env_id')
        params = {}
        if env_id:
            params['environmentId'] = env_id
        output = { 'found': False }

        response = requests.get(state_url, params=params, headers=user_agent, verify=False, auth=requests.auth.HTTPBasicAuth(api_key, secret))
        data = response.json()
        if data['response_code'] == 0 and data['response']['state'] == 'SUCCESS':
            params['type'] = 'json'
            res = requests.get(report_url, headers=user_agent, params=params, verify=False, auth=requests.auth.HTTPBasicAuth(api_key, secret))
            output = res.json()
            output['found'] = True

        output['response_code'] = data['response_code']
        output['state'] = data['response']['state']

        if 'analysis' not in output:
            return output

        for apicall in output['analysis']['runtime']['targets']['target']['apicalls']['chronology']['apicall']:
            if not isinstance(apicall['parameters']['parameter'], list):
                apicall['parameters']['parameter'] = [apicall['parameters']['parameter']]

        for category in output['analysis']['final']['signatures']['category']:
            if not isinstance(category['signature'], list):
                category['signature'] = [category['signature']]

        return komand.helper.clean(output)


    def test(self):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        digest = "d6dcfa69ef0e437fbcc60a1ea4f03019e4814fa90b789e0e80d5179022e2b118"
        state_url = server + "/state/%s" % digest
        report_url = server + "/result/%s" % digest
        user_agent = {'User-Agent': 'VxStream Sandbox'}
        env_id = "100"
        params = {'type': 'json', 'environmentId': env_id}
        output = {}

        response = requests.get(state_url, params={'environmentId': env_id}, headers=user_agent, verify=False, auth=requests.auth.HTTPBasicAuth(api_key, secret))
        data = response.json()
        if data['response_code'] != 0:
            self.logger.error("API returned response code %d. Check that the API key and secret are correct." % data['response_code'])
            raise Exception('VxStream Sandbox - "Report" - Invalid credentials')

        output['response_code'] = data['response_code']

        return komand.helper.clean(output)
