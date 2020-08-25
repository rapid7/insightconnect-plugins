import insightconnect_plugin_runtime
from .schema import SearchDevicesInput, SearchDevicesOutput, Input, Output, Component
# Custom imports below


class SearchDevices(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_devices',
            description=Component.DESCRIPTION,
            input=SearchDevicesInput(),
            output=SearchDevicesOutput())

    def run(self, params={}):
        return {
            Output.DEVICES: self.connection.api.search_managed_devices(params.get(Input.DEVICE))
        }
