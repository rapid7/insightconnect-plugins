import insightconnect_plugin_runtime

from .schema import IpMonitorInput, IpMonitorOutput
from ...util.util import make_request


class IpMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_monitor",
            description="Searches the daily activity of all our monitored TLDs on any given IP address",
            input=IpMonitorInput(),
            output=IpMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.ip_monitor, **params)
        return response
