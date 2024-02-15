import insightconnect_plugin_runtime

from .schema import RegistrantMonitorInput, RegistrantMonitorOutput
from ...util.util import make_request


class RegistrantMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="registrant_monitor",
            description="Searches the ownership (Whois) records of domain names for specific search terms",
            input=RegistrantMonitorInput(),
            output=RegistrantMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.registrant_monitor, **params)
        return response
