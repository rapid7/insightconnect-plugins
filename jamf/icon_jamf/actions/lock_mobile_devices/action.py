import komand
from .schema import LockMobileDevicesInput, LockMobileDevicesOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException


class LockMobileDevices(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lock_mobile_devices',
            description=Component.DESCRIPTION,
            input=LockMobileDevicesInput(),
            output=LockMobileDevicesOutput())

    def run(self, params={}):
        base_url = self.connection.base_url
        devices_id = ",".join(params.get(Input.DEVICES_ID))
        endpoint = f'/JSSResource/mobiledevicecommands/command/DeviceLock/id/{devices_id}'
        url = f'{base_url}/{endpoint}'

        result = self.connection.session.post(url)

        if result.status_code != 201:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=result.text)

        return {
            Output.STATUS: result.status_code
        }
