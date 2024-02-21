import insightconnect_plugin_runtime
from .schema import IpMonitorInput, IpMonitorOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class IpMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_monitor",
            description=Component.DESCRIPTION,
            input=IpMonitorInput(),
            output=IpMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.ip_monitor, **params)
        return response
