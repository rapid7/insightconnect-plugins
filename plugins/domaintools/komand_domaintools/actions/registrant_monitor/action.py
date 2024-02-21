import insightconnect_plugin_runtime
from .schema import RegistrantMonitorInput, RegistrantMonitorOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class RegistrantMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="registrant_monitor",
            description=Component.DESCRIPTION,
            input=RegistrantMonitorInput(),
            output=RegistrantMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.registrant_monitor, **params)
        return response
