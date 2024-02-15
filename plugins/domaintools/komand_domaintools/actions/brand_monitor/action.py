import insightconnect_plugin_runtime

from .schema import BrandMonitorInput, BrandMonitorOutput
from ...util.util import make_request


class BrandMonitor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="brand_monitor",
            description="Searches across all new domain registrations worldwide",
            input=BrandMonitorInput(),
            output=BrandMonitorOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        response = make_request(self.connection.api.brand_monitor, **params)
        return response
