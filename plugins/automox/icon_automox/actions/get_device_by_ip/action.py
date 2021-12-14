import insightconnect_plugin_runtime
from .schema import GetDeviceByIpInput, GetDeviceByIpOutput, Input, Output, Component
# Custom imports below


class GetDeviceByIp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_device_by_ip',
                description=Component.DESCRIPTION,
                input=GetDeviceByIpInput(),
                output=GetDeviceByIpOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
