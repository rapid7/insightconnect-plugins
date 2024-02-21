import insightconnect_plugin_runtime
from .schema import BrandMonitorInput, BrandMonitorOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class BrandMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="brand_monitor",
            description=Component.DESCRIPTION,
            input=BrandMonitorInput(),
            output=BrandMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = util.make_request(self.connection.api.brand_monitor, **params)
        return response
