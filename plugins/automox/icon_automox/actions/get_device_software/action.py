import insightconnect_plugin_runtime
from .schema import GetDeviceSoftwareInput, GetDeviceSoftwareOutput, Input, Output, Component
# Custom imports below


class GetDeviceSoftware(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_device_software',
                description=Component.DESCRIPTION,
                input=GetDeviceSoftwareInput(),
                output=GetDeviceSoftwareOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
