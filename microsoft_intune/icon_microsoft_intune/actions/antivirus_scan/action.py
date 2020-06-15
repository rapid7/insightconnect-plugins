import insightconnect_plugin_runtime
from .schema import AntivirusScanInput, AntivirusScanOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class AntivirusScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='antivirus_scan',
            description=Component.DESCRIPTION,
            input=AntivirusScanInput(),
            output=AntivirusScanOutput())

    def run(self, params={}):
        devices = self.connection.api.search_managed_devices(params.get(Input.DEVICE))

        if not devices:
            raise PluginException(cause='Resource not found.',
                                  assistance='Unable to find a device using device details provided.')

        success = False
        for device in devices:
            if params.get(Input.UPDATE, False):
                self.connection.api.windows_defender_update_signatures(device['id'])

            if self.connection.api.windows_defender_scan(device['id']):
                success = True

        if success:
            return {
                Output.SUCCESS: True
            }

        raise PluginException(preset=PluginException.Preset.UNKNOWN)
