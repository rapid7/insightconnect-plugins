import komand
from .schema import NameServerMonitorInput, NameServerMonitorOutput
# Custom imports below
from komand_domaintools.util import util


class NameServerMonitor(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='name_server_monitor',
                description='Searches the daily activity of all our monitored TLDs on any given name server. ',
                input=NameServerMonitorInput(),
                output=NameServerMonitorOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        response = utils.make_request(self.connection.api.name_server_monitor, **params)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
