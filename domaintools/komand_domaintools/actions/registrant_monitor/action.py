import komand
from .schema import RegistrantMonitorInput, RegistrantMonitorOutput
# Custom imports below
from komand_domaintools.util import util


class RegistrantMonitor(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='registrant_monitor',
                description='Searches the ownership (Whois) records of domain names for specific search terms',
                input=RegistrantMonitorInput(),
                output=RegistrantMonitorOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        response = utils.make_request(self.connection.api.registrant_monitor, **params)
        #return { 'response': response.data() }
        return response

    def test(self):
        """TODO: Test action"""
        return {}
