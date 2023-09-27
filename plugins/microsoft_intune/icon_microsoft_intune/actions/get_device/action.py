import insightconnect_plugin_runtime
from .schema import GetDeviceInput, GetDeviceOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device", description=Component.DESCRIPTION, input=GetDeviceInput(), output=GetDeviceOutput()
        )

    def run(self, params={}):
        return {Output.DEVICE: clean(self.connection.api.get_device(params.get(Input.DEVICEID)))}
