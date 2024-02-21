import insightconnect_plugin_runtime
from .schema import NameServerMonitorInput, NameServerMonitorOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class NameServerMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="name_server_monitor",
            description=Component.DESCRIPTION,
            input=NameServerMonitorInput(),
            output=NameServerMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.name_server_monitor, **params)
        return response
