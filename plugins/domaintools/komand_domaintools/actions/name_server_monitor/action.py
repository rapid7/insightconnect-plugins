import insightconnect_plugin_runtime

from .schema import NameServerMonitorInput, NameServerMonitorOutput
from ...util.util import make_request


class NameServerMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="name_server_monitor",
            description="Searches the daily activity of all our monitored TLDs on any given name server. ",
            input=NameServerMonitorInput(),
            output=NameServerMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.name_server_monitor, **params)
        return response
