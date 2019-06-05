import komand
from .schema import UsageInput, UsageOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Usage(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='usage',
                description='Check your usage of the MxToolBox API',
                input=UsageInput(),
                output=UsageOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "usage"
        if token != "" and token != None:
            return utils.query_api(request_url, token)
        else:
            return { 'response': {'Errors': [{'Error': 'This call requires a token to identify the requested account'}]}}

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "usage"
        if token != "" and token != None:
            return utils.test_api(request_url, token)
        else:
            return { 'response': {'Errors': [{'Error': 'This call requires a token to identify the requested account'}]}}
