import komand
from .schema import IpMonitorInput, IpMonitorOutput
# Custom imports below
from komand_domaintools.util import util


class IpMonitor(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='ip_monitor',
                description='Searches the daily activity of all our monitored TLDs on any given IP address',
                input=IpMonitorInput(),
                output=IpMonitorOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        response = utils.make_request(self.connection.api.ip_monitor, **params)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
